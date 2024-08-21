import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F

## @params: [JOB_NAME, S3_INPUT_PATH_TRUSTED_INTEGRACAO, S3_OUTPUT_PATH_REFINED]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_TRUSTED_INTEGRACAO', 'S3_OUTPUT_PATH_REFINED'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Ler os dados Parquet do S3
df = spark.read.parquet(args['S3_INPUT_PATH_TRUSTED_INTEGRACAO'])

# Fato Filmes
df_fato_filmes = df.select(
    F.col("id_filme"),
    F.col("id_imdb"),
    F.col("voto_medio"),
    F.col("contagem_votos"),
    F.col("orcamento"),
    F.col("receita"),
    F.col("popularidade_filme"),
    F.col("origem")
)

# Dimensão Elenco
df_dim_elenco = df.select(
    F.col("id_filme"),
    F.col("id_imdb"),
    F.col("id_ator"),
    F.col("cast_id"),
    F.col("adult"),
    F.col("generos"),
    F.col("nome_ator"),
    F.col("nome_original"),
    F.col("departamento"),
    F.col("ator_popularidade"),
    F.col("profile_path"),
    F.col("personagem"),
    F.col("credit_id"),
    F.col("ordem"),
    F.col("origem")
)

# Dimensão Dados Adicionais
df_dim_dados_adicionais = df.select(
    F.col("id_filme"),
    F.col("id_imdb"),
    F.col("titulo"),
    F.col("titulo_original"),
    F.col("sinopse"),
    F.col("url_capa"),
    F.col("origem")
).distinct()

# Dimensão Custos e Receita
df_dim_custos_receita = df.select(
    F.col("id_filme"),
    F.col("id_imdb"),
    F.col("orcamento"),
    F.col("receita"),
    F.col("origem")
).distinct()

# Dimensão Votos
df_dim_votos = df.select(
    F.col("id_filme"),
    F.col("id_imdb"),
    F.col("voto_medio"),
    F.col("contagem_votos"),
    F.col("origem")
).distinct()

# Dimensão Popularidade
df_dim_popularidade = df.select(
    F.col("id_filme"),
    F.col("id_imdb"),
    F.col("popularidade_filme"),
    F.col("origem")
).distinct()

# Dimensão Idioma
df_dim_idioma = df.select(
    F.col("id_filme"),
    F.col("id_imdb"),
    F.col("idioma"),
    F.col("origem")
).distinct()

# Dimensão Tempo
df_dim_tempo = df.select(
    F.col("id_filme"),
    F.col("id_imdb"),
    F.col("ano_lancamento").cast("date").alias("data_lancamento"),
    F.year(F.col("ano_lancamento")).alias("ano"),
    F.month(F.col("ano_lancamento")).alias("mes"),
    F.dayofmonth(F.col("ano_lancamento")).alias("dia"),
    F.col("origem")
).distinct()

# Dimensão Duração e Métricas (Orçamento e Receita)
df_dim_duracao_metrica = df.select(
    F.col("id_filme"),
    F.col("id_imdb"),
    F.col("receita"),
    F.col("orcamento"),
    F.col("tempo_execucao"),
    F.col("origem")
).distinct()

# Dimensão Gêneros
df_dim_generos = df.select(
    F.col("id_filme"),
    F.col("id_imdb"),
    F.col("generos"),
    F.col("origem")
).distinct()

# Salvar os dados no S3 em formato Parquet
df_fato_filmes.write.mode("overwrite").parquet(args['S3_OUTPUT_PATH_REFINED'] + "/fato/fato_filmes/")
df_dim_dados_adicionais.write.mode("overwrite").parquet(args['S3_OUTPUT_PATH_REFINED'] + "/dimensoes/dim_dados_adicionais/")
df_dim_tempo.write.mode("overwrite").parquet(args['S3_OUTPUT_PATH_REFINED'] + "/dimensoes/dim_tempo/")
df_dim_elenco.write.mode("overwrite").parquet(args['S3_OUTPUT_PATH_REFINED'] + "/dimensoes/dim_elenco/")
df_dim_custos_receita.write.mode("overwrite").parquet(args['S3_OUTPUT_PATH_REFINED'] + "/dimensoes/dim_custos_receita/")
df_dim_votos.write.mode("overwrite").parquet(args['S3_OUTPUT_PATH_REFINED'] + "/dimensoes/dim_voto_medio/")
df_dim_popularidade.write.mode("overwrite").parquet(args['S3_OUTPUT_PATH_REFINED'] + "/dimensoes/dim_popularidade/")
df_dim_idioma.write.mode("overwrite").parquet(args['S3_OUTPUT_PATH_REFINED'] + "/dimensoes/dim_idioma/")
df_dim_duracao_metrica.write.mode("overwrite").parquet(args['S3_OUTPUT_PATH_REFINED'] + "/dimensoes/dim_duracao_metrica/")
df_dim_generos.write.mode("overwrite").parquet(args['S3_OUTPUT_PATH_REFINED'] + "/dimensoes/dim_generos/")

job.commit()
