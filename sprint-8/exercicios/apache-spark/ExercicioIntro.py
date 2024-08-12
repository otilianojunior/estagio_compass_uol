# Importa as bibliotecas
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf, expr
from pyspark.sql.types import StringType
import random

# Inicializa o SparkSession
spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

# ------------------------------------------------------------------------

# ETAPA 1 - Lê o arquivo CSV e exibe as 5 linhas
df_nomes = spark.read.csv('../geracao-dados/data/nomes_aleatorios.txt', header=False, inferSchema=True)
print('----- ETAPA 1 -----')
df_nomes.show(5)

# ------------------------------------------------------------------------

# ETAPA 2 - Renomeia a coluna para Nome e mostra o Schema
df_nomes = df_nomes.withColumnRenamed("_c0", "Nome")
print('----- ETAPA 2 -----')
df_nomes.printSchema()

# ------------------------------------------------------------------------

# Define as listas de valores possíveis para as colunas novas
escolaridades = ['Fundamental', 'Medio', 'Superior']

paises = [
    'Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 'Guiana', 'Paraguai', 'Peru', 'Suriname',
    'Uruguai', 'Venezuela'
]


# Define funções UDF para gerar valores aleatórios
def random_escolaridade():
    return random.choice(escolaridades)


def random_pais():
    return random.choice(paises)


# Registra as funções UDF
udf_escolaridade = udf(random_escolaridade, StringType())
udf_pais = udf(random_pais, StringType())

# ------------------------------------------------------------------------


# ETAPA 3 - Cria uma coluna 'Escolaridade' com valores aleatórios
df_nomes = df_nomes.withColumn('Escolaridade', udf_escolaridade())


# ------------------------------------------------------------------------

# ETAPA 4 - Cria uma coluna 'Pais' com valores aleatórios
df_nomes = df_nomes.withColumn('Pais', udf_pais())

# ------------------------------------------------------------------------

# ETAPA 5 - Cria uma coluna 'AnoNascimento' com valores aleatórios entre 1945 e 2010
df_nomes = df_nomes.withColumn('AnoNascimento', expr("floor(rand() * (2010 - 1945 + 1)) + 1945"))

# ------------------------------------------------------------------------

# ETAPA 6 - Filtrar os dados
df_select = df_nomes.filter(col('AnoNascimento') >= 2000)
# Mostrar os resultados
print('----- ETAPA 6 -----')
df_select.show(10)

# ------------------------------------------------------------------------

# ETAPA 7 - Cria uma visão temporária para consulta SQL
df_nomes.createOrReplaceTempView('pessoas')

# Executa a consulta SQL para selecionar pessoas que nasceram neste século (2000-2024)
df_pessoas = spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000")

# Mostrar os resultados da consulta SQL
print('----- ETAPA 7 -----')
df_pessoas.show(10)

# ------------------------------------------------------------------------
# ETAPA 8 - Contar o número de pessoas nascidas entre 1980 e 1995
df_filtro_data = df_nomes.select('AnoNascimento').filter(col('AnoNascimento').between(1980, 1995))
count_filtro_data = df_filtro_data.count()

print('----- ETAPA 8 -----')
print(f"Número de pessoas nascidas entre 1980 e 1995: {count_filtro_data}")

# ------------------------------------------------------------------------
# ETAPA 9 - Conta o numero de pessoas nascidas entre 1980 e 1995 usando o SQL
df_nomes.createOrReplaceTempView('filtro_data')
# Executa a consulta SQL para contar o número de pessoas nascidas entre 1980 e 1995
df_filtro_data_sql = spark.sql(""
                               "SELECT COUNT(*) AS count_pessoas "
                               "FROM filtro_data "
                               "WHERE AnoNascimento BETWEEN 1980 AND 1995")

# Mostrar o resultado da contagem
print('----- ETAPA 9 -----')
df_filtro_data_sql.show()

# ------------------------------------------------------------------------
# ETAPA 10 - Cria uma visão temporária para consulta SQL
df_nomes.createOrReplaceTempView('filtro_geracoes')

# Executa a consulta SQL para contar o número de pessoas por país e geração
df_geracoes = spark.sql("""
                        SELECT
                            Pais,
                            CASE
                                WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
                                WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
                                WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Milenniais (Geração Y)'
                                WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
                                ELSE 'Desconhecido'
                            END AS Geracao,
                            COUNT(*) AS Quantidade
                        FROM
                            pessoas
                        GROUP BY
                            Pais, Geracao
                        ORDER BY
                            Pais ASC,
                            Geracao ASC,
                            Quantidade ASC
                    """)

# Mostrar todas as linhas em ordem crescente de país, geração e quantidade
print('----- ETAPA 10 -----')
df_geracoes.show(truncate=False)
