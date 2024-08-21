import sys
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql import functions as F

# Parâmetros do job
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_TRUSTED_TMDB', 'S3_INPUT_PATH_TRUSTED_CSV', 'S3_OUTPUT_PATH_TRUSTED'])

# Inicializa o contexto
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Caminhos dos arquivos de entrada
input_path_tmdb = args['S3_INPUT_PATH_TRUSTED_TMDB']
input_path_csv = args['S3_INPUT_PATH_TRUSTED_CSV']

# Caminho do arquivo de saída
output_path = args['S3_OUTPUT_PATH_TRUSTED'] + "/INTEGRACAO"

# Leitura dos arquivos Parquet
df_tmdb = spark.read.parquet(input_path_tmdb)
df_csv = spark.read.parquet(input_path_csv)

# Expande o campo 'cast' para linhas individuais no df_tmdb
df_tmdb_expanded = df_tmdb.withColumn("elenco", F.explode(F.col("cast")))

# Cria o DataFrame com os dados do elenco separados
df_filmes_tmdb = df_tmdb_expanded.select(
    F.col("id_filme").cast("int").alias("id_filme"),
    F.col("imdb_id").cast("string").alias("id_imdb"),
    F.col("budget").cast("int").alias("orcamento"),
    F.col("genres").cast("string").alias("generos"),
    F.col("language").cast("string").alias("idioma"),
    F.col("original_title").cast("string").alias("titulo_original"),
    F.col("overview").cast("string").alias("sinopse"),
    F.col("popularidade_filme"),
    F.col("poster_url").cast("string").alias("url_capa"),
    F.col("release_date").cast("date").alias("ano_lancamento"),
    F.col("revenue").cast("int").alias("receita"),
    F.col("runtime").cast("int").alias("tempo_execucao"),
    F.col("title").cast("string").alias("titulo"),
    F.col("vote_average").cast("double").alias("voto_medio"),
    F.col("vote_count").cast("int").alias("contagem_votos"),
    F.col("origem").cast("string"),
    F.col("elenco.id").cast("int").alias("id_ator"),
    F.col("elenco.cast_id").cast("int").alias("cast_id"),
    F.col("elenco.adult").cast("boolean").alias("adult"),
    F.col("elenco.gender").cast("string").alias("genero_ator"),
    F.col("elenco.name").cast("string").alias("nome_ator"),
    F.col("elenco.original_name").cast("string").alias("nome_original"),
    F.col("elenco.known_for_department").cast("string").alias("departamento"),
    F.col("elenco.popularity").cast("double").alias("ator_popularidade"),
    F.col("elenco.profile_path").cast("string").alias("profile_path"),
    F.col("elenco.character").cast("string").alias("personagem"),
    F.col("elenco.credit_id").cast("string").alias("credit_id"),
    F.col("elenco.order").cast("int").alias("ordem")
)

# Seleciona as colunas do DataFrame CSV, convertendo os anos em datas fictícias
df_csv = df_csv.select(
    F.col("id").cast("string").alias("id_imdb"),
    F.col("titulo").cast("string").alias("titulo"),
    F.col("titulo_original").cast("string").alias("titulo_original"),
    F.col("ano_lancamento").cast("date").alias("ano_lancamento"),
    F.col("tempo_duracao").cast("int").alias("tempo_execucao"),
    F.col("genero").cast("string").alias("generos"),
    F.col("media_votos").cast("double").alias("voto_medio"),
    F.col("numero_votos").cast("int").alias("contagem_votos"),
    F.col("genero_artista").cast("string").alias("genero_ator"),
    F.col("personagem").cast("string").alias("personagem"),
    F.col("nomeArtista").cast("string").alias("nome_ator"),
    F.when(F.col("ano_nascimento").isNotNull(), F.to_date(F.concat(F.col("ano_nascimento"), F.lit("-01-01")), "yyyy-MM-dd")).alias("ano_nascimento"),
    F.when(F.col("anoFalecimento").isNotNull(), F.to_date(F.concat(F.col("anoFalecimento"), F.lit("-01-01")), "yyyy-MM-dd")).alias("ano_falecimento"),
    F.col("profissao").cast("string").alias("departamento"),
    F.col("titulos_conhecidos").cast("string").alias("titulo_conhecidos"),
    F.col("origem").cast("string").alias("origem")
)

# Realiza a união dos DataFrames, alinhando as colunas e preenchendo os valores ausentes com None
df_final = df_filmes_tmdb.unionByName(df_csv, allowMissingColumns=True)

# Salva o DataFrame combinado como um único arquivo Parquet
df_final.write.mode('overwrite').parquet(output_path)

# Finaliza o job
job.commit()
