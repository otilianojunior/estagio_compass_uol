# importação das bibliotecas necessárias
import boto3
from dotenv import load_dotenv
import os
from datetime import datetime


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()


# configurar a sessão do usuario na aws
def configure_aws_session():
    try:
        return boto3.Session(
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
            region_name=os.getenv('AWS_DEFAULT_REGION')
        )
    except Exception as ex:
        raise Exception(f'Erro ao configurar sessão: {ex}')


# formatar os dados para formato pedido
def get_s3_key(file, now):
    try:
        file_type = file.split('.')[-1].upper()
        file_name = os.path.splitext(file)[0].capitalize()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        return f"Raw/Local/{file_type}/{file_name}/{year}/{month}/{day}/{file}"
    except Exception as ex:
        raise Exception(f'Erro gerar Key: {ex}')


def upload_files_to_s3(session, bucket_name, local_folder):
    s3 = session.resource('s3')
    bucket = s3.Bucket(bucket_name)
    now = datetime.now()

    if not os.path.exists(local_folder):
        raise Exception(f'O diretório {local_folder} não existe.')

    for root, _, files in os.walk(local_folder):
        for file in files:
            # Obtenha o caminho completo do arquivo
            file_path = os.path.join(root, file)

            # Formate o caminho de destino no S3
            s3_key = get_s3_key(file, now)

            try:
                # Faça o upload do arquivo para o S3
                bucket.upload_file(file_path, s3_key)
                print(f"Uploaded {file_path} no s3://{bucket_name}/{s3_key}")
            except Exception as e:
                print(f"Falha no upload {file_path}: {e}")


# Nome do bucket
bucket_name = 'data-lake-otiliano'

# Pasta local com os arquivos
local_folder = os.path.abspath('dados_brutos')

# Configure a sessão AWS
session = configure_aws_session()

# Faça o upload dos arquivos
upload_files_to_s3(session, bucket_name, local_folder)
