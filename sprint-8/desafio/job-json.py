import sys
import re
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession


# Função para extrair a data do caminho do arquivo
def extract_date_from_path(path):
    match = re.search(r'/(\d{4})/(\d{2})/(\d{2})/', path)
    if match:
        year, month, day = match.groups()
        return f"{year}/{month}/{day}"
    return None


# Parâmetros do job
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_RAW_TMDB_MOVIES', 'S3_INPUT_PATH_RAW_TMDB_SERIES',
                                     'S3_OUTPUT_PATH_TRUSTED'])

# Inicialização do SparkContext e GlueContext
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Ler JSON de Movies do S3
dynamic_frame_movies = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [args['S3_INPUT_PATH_RAW_TMDB_MOVIES']]},
    format="json"
)

# Converter DynamicFrame para DataFrame
df_movies = dynamic_frame_movies.toDF()

# Ler JSON de Series do S3
dynamic_frame_series = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [args['S3_INPUT_PATH_RAW_TMDB_SERIES']]},
    format="json"
)

# Converter DynamicFrame para DataFrame
df_series = dynamic_frame_series.toDF()

# Caminhos de saída
base_output_path = args['S3_OUTPUT_PATH_TRUSTED']
date_path_movies = extract_date_from_path(args['S3_INPUT_PATH_RAW_TMDB_MOVIES'])
date_path_series = extract_date_from_path(args['S3_INPUT_PATH_RAW_TMDB_SERIES'])

output_path_movies = f"{base_output_path}/movies/{date_path_movies}"
output_path_series = f"{base_output_path}/series/{date_path_series}"

# Salvar DataFrame de Movies como Parquet
df_movies.write.mode('overwrite').parquet(output_path_movies)

# Salvar DataFrame de Series como Parquet
df_series.write.mode('overwrite').parquet(output_path_series)

# Commit do job
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
job.commit()
