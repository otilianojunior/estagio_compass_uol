import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType


# Função para salvar DataFrame em Parquet
def save_as_parquet(df, output_path: str):
    if df.count() > 0:
        df.write.mode('overwrite').parquet(output_path)
        print(f"DataFrame salvo em: {output_path}")
    else:
        print(f"DataFrame vazio: Nenhum dado para salvar em {output_path}")


# Parâmetros do job
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_LOCAL_MOVIES', 'S3_INPUT_PATH_LOCAL_SERIES',
                                     'S3_OUTPUT_PATH_TRUSTED'])

# Inicialização do contexto Spark e Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos dos dados
S3_INPUT_PATH_LOCAL_MOVIES = args['S3_INPUT_PATH_LOCAL_MOVIES']
S3_INPUT_PATH_LOCAL_SERIES = args['S3_INPUT_PATH_LOCAL_SERIES']
S3_OUTPUT_PATH_TRUSTED = args['S3_OUTPUT_PATH_TRUSTED']

# Definição do esquema comum
common_schema = StructType([
    StructField("id", StringType(), True),
    StructField("tituloPincipal", StringType(), True),
    StructField("tituloOriginal", StringType(), True),
    StructField("anoLancamento", IntegerType(), True),
    StructField("anoTermino", IntegerType(), True),
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

# Leitura dos dados CSV com esquema definido
try:
    movies_df = spark.read.schema(common_schema).csv(S3_INPUT_PATH_LOCAL_MOVIES, sep='|', header=True)
    series_df = spark.read.schema(common_schema).csv(S3_INPUT_PATH_LOCAL_SERIES, sep='|', header=True)

    # Verificar o número de linhas e as primeiras linhas dos DataFrames
    print("First few rows of Movies DataFrame:")
    movies_df.show(5)

    print("First few rows of Series DataFrame:")
    series_df.show(5)

except Exception as e:
    print(f"Erro ao ler os dados: {str(e)}")

# Verificar e salvar os DataFrames em formato Parquet
movies_output_path = (S3_OUTPUT_PATH_TRUSTED + 'movies')
series_output_path = (S3_OUTPUT_PATH_TRUSTED + 'series')

save_as_parquet(movies_df, movies_output_path)

save_as_parquet(series_df, series_output_path)

# Commit do job
job.commit()
