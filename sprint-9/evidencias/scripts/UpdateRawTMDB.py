# Importação das bibliotecas necessárias
import boto3
from datetime import datetime
import json
import os
import requests
from dotenv import load_dotenv  # Biblioteca para carregar variáveis do .env

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Armazena o tamanho total dos arquivos
total_size = 0

# Configura o cliente S3 com base nas variáveis de ambiente
def configure_s3_client():
    try:
        aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
        aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
        aws_session_token = os.getenv('AWS_SESSION_TOKEN')
        region_name = os.getenv('AWS_DEFAULT_REGION')

        if not all([aws_access_key_id, aws_secret_access_key, aws_session_token, region_name]):
            raise ValueError('Credenciais AWS não configuradas corretamente.')

        return boto3.resource(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token,
            region_name=region_name
        )
    except Exception as ex:
        raise Exception(f'Erro ao configurar cliente S3: {ex}')

# Conecta API do TMDB
def conecta_api_tmdb(endpoint, params=None):
    base_url = 'https://api.themoviedb.org/3'
    url = f'{base_url}/{endpoint}'
    params['api_key'] = configure_api_key_tmdb()
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Erro na requisição: {response.status_code} - {response.text}')
            return None
    except Exception as ex:
        raise Exception(f'Erro ao obter dados da API do TMDB: {ex}')

# Obtém a chave API do TMDB
def configure_api_key_tmdb():
    try:
        api_key = os.getenv('TMDB_API_KEY')
        if not api_key:
            raise ValueError('API key não configurada.')
        return api_key
    except Exception as ex:
        raise Exception(f'Erro ao obter API key: {ex}')

# Carrega o elenco dos filmes
def get_elenco_movie(movie_id):
    try:
        endpoint = f'movie/{movie_id}/credits'
        data = conecta_api_tmdb(endpoint, {})
        if data:
            return data.get('cast', [])
        else:
            return []
    except Exception as ex:
        print(f'Erro ao obter dados do cast: {ex}')
        return []

# Obtém detalhes do filme, incluindo custo, bilheteira, runtime, overview, e imdb_id
def get_movie_details(movie_id):
    try:
        endpoint = f'movie/{movie_id}'
        data = conecta_api_tmdb(endpoint, {})
        if data:
            return {
                'id': data.get('id', 'N/A'),
                'title': data.get('title', 'N/A'),
                'original_title': data.get('original_title', 'N/A'),
                'release_date': data.get('release_date', 'N/A'),
                'language': data.get('original_language', 'N/A'),
                'genres': [genre['name'] for genre in data.get('genres', [])],
                'vote_count': data.get('vote_count', 'N/A'),
                'vote_average': data.get('vote_average', 'N/A'),
                'popularity': data.get('popularity', 'N/A'),
                'runtime': data.get('runtime', 'N/A'),
                'overview': data.get('overview', 'N/A'),
                'imdb_id': data.get('imdb_id', 'N/A'),
                'budget': data.get('budget', 'N/A'),
                'revenue': data.get('revenue', 'N/A'),
                'poster_path': data.get('poster_path', None)
            }
        else:
            return {}
    except Exception as ex:
        print(f'Erro ao obter detalhes do filme: {ex}')
        return {}

# Obtém a URL da capa do filme
def get_poster_url(poster_path):
    if poster_path:
        return f'https://image.tmdb.org/t/p/original{poster_path}'
    return None

# Salva os resultados em arquivos JSON no S3
def save_s3(data, filename):
    global total_size
    try:
        s3 = configure_s3_client()
        bucket_name = 'data-lake-otiliano'

        # Gerar a chave no S3
        now = datetime.now()
        file_type = filename.split('.')[-1].upper()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")

        s3_key = f"Raw/TMDB/{file_type}/{year}/{month}/{day}/{filename}"

        # Converte dados em JSON e calcular o tamanho do arquivo
        json_data = json.dumps(data, ensure_ascii=False, indent=4)
        file_size = len(json_data.encode('utf-8'))
        total_size += file_size

        # Salvar os dados no S3
        s3.Object(bucket_name, s3_key).put(Body=json_data)

        print(f'Dados salvos em: s3://{bucket_name}/{s3_key} - Tamanho: {file_size} bytes')

    except Exception as ex:
        raise Exception(f'Erro ao salvar dados no S3: {ex}')

# Edita os resultados em arquivos JSON de 100 em 100
def save_json(movie_ids, filename_prefix):
    try:
        results = []
        file_counter = 1
        json_limit_size = 10 * 1024 * 1024  # 10MB

        for movie_id in movie_ids:
            print(f'Processando filme ID: {movie_id}')
            movie_details = get_movie_details(movie_id)
            if movie_details:
                print(f'Sucesso ao obter detalhes do filme ID: {movie_id}')
                movie = {
                    'id_filme': movie_details.get('id', 'N/A'),
                    'title': movie_details.get('title', 'N/A'),
                    'original_title': movie_details.get('original_title', 'N/A'),
                    'release_date': movie_details.get('release_date', 'N/A'),
                    'language': movie_details.get('language', 'N/A'),
                    'genres': movie_details.get('genres', []),
                    'vote_count': movie_details.get('vote_count', 'N/A'),
                    'vote_average': movie_details.get('vote_average', 'N/A'),
                    'popularidade_filme': movie_details.get('popularity', 'N/A'),
                    'runtime': movie_details.get('runtime', 'N/A'),
                    'overview': movie_details.get('overview', 'N/A'),
                    'imdb_id': movie_details.get('imdb_id', 'N/A'),
                    'budget': movie_details.get('budget', 'N/A'),
                    'revenue': movie_details.get('revenue', 'N/A'),
                    'poster_url': get_poster_url(movie_details.get('poster_path')),
                    'cast': get_elenco_movie(movie_id)
                }
                results.append(movie)

                # Verifica se o tamanho dos dados acumulados ultrapassa 10MB
                json_data = json.dumps(results, ensure_ascii=False, indent=4)
                if len(json_data.encode('utf-8')) >= json_limit_size:
                    filename = f'{filename_prefix}_{file_counter}.json'
                    save_s3(results, filename)
                    results = []  # Reseta a lista para o próximo arquivo
                    file_counter += 1

        # Salva qualquer dado restante em um arquivo final
        if results:
            filename = f'{filename_prefix}_{file_counter}.json'
            save_s3(results, filename)

    except Exception as ex:
        raise Exception(f'Erro ao salvar resultados como JSON no S3: {ex}')

# Função principal para executar o código
def main():
    try:
        lista_id = [238, 242, 240, 278, 424, 13, 497, 637, 857, 274, 77338, 28178, 157336, 50014, 1402, 11978, 475557,
                    745, 665, 271969, 324786, 15121, 332562, 3111, 19610, 96724, 70881, 50512, 111, 877, 982, 14462,
                    1598, 11349, 11027, 25736, 44264, 17529, 4415, 82695, 5919, 154030]

        # Busca detalhes dos filmes com base na lista de IDs
        save_json(lista_id, 'movies')

        # Converte o tamanho total para MB
        total_size_mb = total_size / (1024 * 1024)
        print(f'Dados processados com sucesso. Tamanho total: {total_size_mb:.2f} MB')

    except Exception as ex:
        print(f'Erro ao processar dados: {ex}')

if __name__ == "__main__":
    main()
