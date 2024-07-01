# Importa as bibliotecas utilizadas no projeto, boto3, dotenv, os
import boto3
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()


# Configura o acesso a aws utilizando as variáveis de ambiente.
def configure_aws_session():
    return boto3.Session(
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
        region_name=os.getenv('AWS_DEFAULT_REGION')
    )


# Cria um cliente do s3 usando boto3
def execute_s3_select(bucket_name, key, query, output_file):
    s3 = boto3.client('s3')

    # Utiliza o nome do bucket, nome do objeto, tipo de consulta, query, formato de entrada e saída.
    resp = s3.select_object_content(
        Bucket=bucket_name,
        Key=key,
        ExpressionType='SQL',
        Expression=query,
        InputSerialization={'CSV': {"FileHeaderInfo": "Use"}, 'CompressionType': 'NONE'},
        OutputSerialization={'CSV': {}},
    )

    # Define os nomes das colunas para o arquivo de saída
    column_names = "total_ocorrencias,quantidade_particular,quantidade_aluguel\n"

    with open(output_file, 'w') as f:
        f.write(column_names)
        for event in resp['Payload']:
            if 'Records' in event:
                records = event['Records']['Payload'].decode('utf-8')
                f.write(records)
            elif 'Stats' in event:
                stats = event['Stats']['Details']
                print(f'Scanned: {stats["BytesScanned"]} bytes, Processed: {stats["BytesProcessed"]} bytes, '
                      f'Returned: {stats["BytesReturned"]} bytes')


if __name__ == "__main__":
    session = configure_aws_session()
    s3_client = boto3.client('s3', region_name=os.getenv('AWS_DEFAULT_REGION'))

    bucket_name = 'otilianojr-dados-acidentes-2021'
    key = 'dados-acidentes-2021.csv'

    query = """
        SELECT COUNT(*) AS total_ocorrencias, 
        SUM(CASE WHEN descricao_categoria = 'PARTICULAR' THEN 1 ELSE 0 END) AS quantidade_particular, 
        SUM(CASE WHEN descricao_categoria = 'ALUGUEL' THEN 1 ELSE 0 END) AS quantidade_aluguel 
        FROM s3object 
        WHERE CAST(SUBSTRING(data_hora_boletim, 9, 2) AS INTEGER) = 21 
        AND descricao_especie = 'AUTOMOVEL' AND desc_situacao = 'EM MOVIMENTO' 
        AND (descricao_categoria = 'PARTICULAR' OR descricao_categoria = 'ALUGUEL');
    """

    output_file = 'query_results.csv'
    execute_s3_select(bucket_name, key, query, output_file)
    print(f"Resultados salvos em: {output_file}")
