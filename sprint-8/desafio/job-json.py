import sys
import re
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql.functions import lit

# Função para extrair a data do caminho do arquivo
def extract_date_from_path(path):
    match = re.search(r'/(\d{4})/(\d{2})/(\d{2})/', path)
    if match:
        year, month, day = match.groups()
        return f"{year}/{month}/{day}"
    return None

# Parâmetros do job
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_RAW_TMDB_MOVIES', 'S3_OUTPUT_PATH_TRUSTED'])

# Inicializa o contexto
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Leitura do arquivo JSON com opções adicionais
data_frame = spark.read.option("multiline", "true").json(args['S3_INPUT_PATH_RAW_TMDB_MOVIES'])

# Adiciona a coluna 'origem' com o valor 'tmdb'
data_frame = data_frame.withColumn("origem", lit("tmdb"))

# Extrai a data do caminho de entrada
date_path_movies = extract_date_from_path(args['S3_INPUT_PATH_RAW_TMDB_MOVIES'])

# Define o caminho base para a saída
base_output_path = args['S3_OUTPUT_PATH_TRUSTED']

# Define o caminho de saída final
output_path_movies = f"{base_output_path}/TMDB/{date_path_movies}"

# Salvando no formato Parquet com opções adicionais
data_frame.write.mode('overwrite').parquet(output_path_movies)

# Finaliza o job
job.commit()
