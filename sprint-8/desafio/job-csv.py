import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from pyspark.sql.functions import lit, col, to_date, concat

# Função para salvar DataFrame em Parquet
def save_as_parquet(df, output_path: str):
    if df is not None and df.count() > 0:
        df.write.mode('overwrite').parquet(output_path)
        print(f"DataFrame salvo em: {output_path}")
    else:
        print(f"DataFrame vazio ou não inicializado: Nenhum dado para salvar em {output_path}")

# Parâmetros do job
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_LOCAL_MOVIES', 'S3_OUTPUT_PATH_TRUSTED'])

# Inicialização do contexto Spark e Glue
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos dos dados
S3_INPUT_PATH_LOCAL_MOVIES = args['S3_INPUT_PATH_LOCAL_MOVIES']
S3_OUTPUT_PATH_TRUSTED = args['S3_OUTPUT_PATH_TRUSTED']

# Definição do esquema
common_schema = StructType([
    StructField("id", StringType(), True),
    StructField("tituloPrincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", IntegerType(), True),
    StructField("tempoMinutos", IntegerType(), True),
    StructField("genero", StringType(), True),
    StructField("notaMedia", DoubleType(), True),
    StructField("numeroVotos", IntegerType(), True),
    StructField("generoArtista", StringType(), True),
    StructField("personagem", StringType(), True),
    StructField("nomeArtista", StringType(), True),
    StructField("anoNascimento", IntegerType(), True),
    StructField("anoFalecimento", IntegerType(), True),
    StructField("profissao", StringType(), True),
    StructField("titulosMaisConhecidos", StringType(), True)
])

# Inicialização do DataFrame
movies_df = None

# Lista de IDs para filtragem
lista_id = ['tt0068646', 'tt0099674', 'tt0071562', 'tt0111161', 'tt0108052', 'tt0109830',
            'tt0120689', 'tt0118799', 'tt0120815', 'tt0102926', 'tt1675434', 'tt1028532',
            'tt0816692', 'tt1454029', 'tt0454921', 'tt0203019', 'tt7286456', 'tt0167404',
            'tt0052618', 'tt2638144', 'tt2119532', 'tt0059742', 'tt1517451', 'tt0047522',
            'tt0075265', 'tt1781769', 'tt0026071', 'tt0118623', 'tt0086250', 'tt0023427',
            'tt0056218', 'tt0368008', 'tt0101540', 'tt0055824', 'tt0082934', 'tt0038854',
            'tt1403865', 'tt0065126', 'tt0119683', 'tt1707386', 'tt0072308', 'tt2554270']

# Leitura dos dados CSV com esquema definido
try:
    movies_df = spark.read.schema(common_schema).csv(S3_INPUT_PATH_LOCAL_MOVIES, sep='|', header=True)

    # Filtrar apenas os IDs desejados
    movies_df = movies_df.filter(movies_df['id'].isin(lista_id))

    # Preencher valores ausentes com null
    for field in common_schema.fields:
        movies_df = movies_df.withColumn(field.name, col(field.name).cast(field.dataType))

    # Adicionar coluna 'origem'
    movies_df = movies_df.withColumn("origem", lit("csv"))

    # Renomear colunas conforme especificado
    movies_df = movies_df.withColumnRenamed("tituloPrincipal", "titulo") \
                         .withColumnRenamed("tituloOriginal", "titulo_original") \
                         .withColumnRenamed("anoLancamento", "ano_lancamento") \
                         .withColumnRenamed("notaMedia", "media_votos") \
                         .withColumnRenamed("numeroVotos", "numero_votos") \
                         .withColumnRenamed("tempoMinutos", "tempo_duracao") \
                         .withColumnRenamed("generoArtista", "genero_artista") \
                         .withColumnRenamed("anoNascimento", "ano_nascimento") \
                         .withColumnRenamed("titulosMaisConhecidos", "titulos_conhecidos")

    # Corrigir o campo ano_lancamento para formato de data
    movies_df = movies_df.withColumn("ano_lancamento",
                                     to_date(concat(col("ano_lancamento").cast(StringType()), lit("-01-01")),
                                             "yyyy-MM-dd"))

except Exception as e:
    print(f"Erro ao ler os dados: {str(e)}")

# Salvar o DataFrame em múltiplos arquivos Parquet
output_path_parquet = S3_OUTPUT_PATH_TRUSTED + '/CSV/'
save_as_parquet(movies_df, output_path_parquet)

# Commit do job
job.commit()
