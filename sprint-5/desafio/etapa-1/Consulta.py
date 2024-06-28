import boto3
from dotenv import load_dotenv
import os
import pandas as pd
from sqlalchemy import create_engine
import logging

load_dotenv()

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def configure_aws_session():
    return boto3.Session(
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
        region_name=os.getenv('AWS_DEFAULT_REGION')
    )


def get_s3_client(session):
    return session.client('s3')


def get_csv_from_s3(s3_client, bucket_name, key):
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=key)
        return pd.read_csv(response['Body'], encoding='utf8')
    except Exception as ex:
        logger.error(f"Erro ao ler o arquivo CSV do S3: {ex}")
        raise


def save_to_sql(df, table_name, engine):
    try:
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        logger.info(f"Resultado salvo em '{table_name}'.")
    except Exception as ex:
        logger.error(f"Erro ao salvar a tabela '{table_name}' no SQLite: {ex}")
        raise


def main():
    session = configure_aws_session()
    s3_client = get_s3_client(session)

    bucket_name = 'otilianojr-dados-acidentes-2021'
    key = 'dados-acidentes-2021.csv'
    sqlite_db = 'dados_acidentes.db'
    sqlite_engine = create_engine(f'sqlite:///{sqlite_db}', echo=True)

    df = get_csv_from_s3(s3_client, bucket_name, key)

    # 4.1. Filtros usando operadores lógicos
    df_filtrado = df[(df['cod_categ'] == 3) & (df['cod_situacao'] != 2)].copy()

    # 4.6 Função String (remoção de espaços)
    df_filtrado['descricao_especie'] = df_filtrado['descricao_especie'].str.strip()

    # 4.2.1 Função de Agregação
    quantidade_veiculos_acidentes = df_filtrado.groupby('descricao_especie').agg({
        'cod_especie': 'count'
    }).rename(columns={'cod_especie': 'count'})

    # 4.2.2 Função de Agregação com Porcentagem
    quantidade_veiculos_acidentes['porcentagem'] = (
            quantidade_veiculos_acidentes['count'] /
            quantidade_veiculos_acidentes['count'].sum() * 100
    )

    # 4.3 Função Condicional para atribuir risco de acidentes
    quantidade_veiculos_acidentes['risco'] = quantidade_veiculos_acidentes['porcentagem'].apply(
        lambda x: 'Alto' if x > 1 else 'Baixo'
    )

    # 4.4 Função Conversão da porcentagem
    quantidade_veiculos_acidentes['porcentagem'] = quantidade_veiculos_acidentes['porcentagem'].apply(
        lambda x: f"{x:.0f}%"
    )

    # 4.5 Função Data
    df_filtrado['data_formato_bd'] = pd.to_datetime(df_filtrado['data_hora_boletim'],
                                                    format='%d/%m/%y %H:%M').dt.strftime('%Y')

    # Selecionar a primeira ocorrência e renomear as colunas
    primeira_ocorrencia = df_filtrado.iloc[0:1].copy()
    primeira_ocorrencia = primeira_ocorrencia.rename(columns={
        'descricao_especie': 'tipo',
        'data_formato_bd': 'data_dados'
    })

    # Adicionar as colunas de quantidade, porcentagem e risco de acidentes
    primeira_ocorrencia['quantidade_veiculos_acidentes'] = quantidade_veiculos_acidentes.loc['AUTOMOVEL', 'count']
    primeira_ocorrencia['porcentagem_acidentes'] = quantidade_veiculos_acidentes.loc['AUTOMOVEL', 'porcentagem']
    primeira_ocorrencia['risco_acidente'] = quantidade_veiculos_acidentes.loc['AUTOMOVEL', 'risco']

    # Selecionar apenas as colunas desejadas
    colunas_desejadas = ['tipo', 'quantidade_veiculos_acidentes', 'porcentagem_acidentes', 'risco_acidente',
                         'data_dados']
    df_resultado = primeira_ocorrencia[colunas_desejadas]

    # Salvar o resultado no banco de dados
    save_to_sql(df_resultado, 'dados_acidentes', sqlite_engine)
    logger.info("Todos os resultados foram salvos em tabelas no banco SQLite dados_acidentes.")


if __name__ == "__main__":
    main()
