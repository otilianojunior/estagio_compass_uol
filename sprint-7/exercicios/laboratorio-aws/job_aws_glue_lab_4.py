import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import upper, col


# Função para imprimir o schema do DataFrame
def print_schema(df):
    df.printSchema()


# Função para imprimir a quantidade de linhas do DataFrame
def print_row_count(df):
    row_count = df.count()
    print(f"Quantidade de linhas no DataFrame: {row_count}")


# Função para imprimir a contagem de nomes agrupados por ano e sexo
def print_grouped_counts(df):
    grouped_df = df.groupBy('ano', 'sexo').count()
    # Ordenar o DataFrame pelo ano em ordem decrescente
    sorted_df = grouped_df.orderBy('ano', ascending=False)
    # Mostrar o resultado
    print("Contagem de nomes agrupados por ano e sexo:")
    sorted_df.show()


# Função para encontrar o nome com mais registros para um determinado sexo
def print_most_frequent_name(df, sexo):
    filtered_df = df.filter(col('sexo') == sexo)
    name_counts = filtered_df.groupBy('nome', 'ano').count()
    # Encontrar o nome com mais registros
    most_frequent = name_counts.orderBy('count', ascending=False).first()

    if most_frequent:
        name, year, count = most_frequent
        print(f"O nome {sexo} com mais registros é '{name}' com {count} registros no ano {year}.")
    else:
        print(f"Não foram encontrados registros para sexo {sexo}.")


# Função para imprimir o total de registros por ano
def print_total_records_by_year(df):
    total_counts_df = df.groupBy('ano').count()
    # Ordenar por ano em ordem crescente e pegar as primeiras 10 linhas
    sorted_df = total_counts_df.orderBy('ano', ascending=True).limit(10)
    print("Total de registros por ano (primeiras 10 linhas):")
    sorted_df.show()


# @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Ler o arquivo CSV do S3
input_path = args['S3_INPUT_PATH']
df = spark.read.format("csv").option("header", "true").load(input_path)

# Atualizar a coluna 'nome' para deixar todos os dados em maiúsculo
df = df.withColumn('nome', upper(df['nome']))

# Chamar a função para imprimir o schema
print_schema(df)

# Chamar a função para imprimir a quantidade de linhas
print_row_count(df)

# Chamar a função para imprimir a contagem de nomes agrupados por ano e sexo
print_grouped_counts(df)

# Chamar a função para encontrar o nome feminino com mais registros
print_most_frequent_name(df, 'F')

# Chamar a função para encontrar o nome masculino com mais registros
print_most_frequent_name(df, 'M')

# Chamar a função para imprimir o total de registros por ano
print_total_records_by_year(df)

# Salvar o DataFrame atualizado no S3 como JSON, particionado por 'sexo' e 'ano'
output_path = args['S3_TARGET_PATH']
df.write.format("json").partitionBy("sexo", "ano").save(output_path)

# Realizar o commit do job
job.commit()
