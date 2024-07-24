# importação das bibliotecas necessárias
import boto3
from datetime import datetime
import json
import os
import requests

# Armazena o tamanho total dos arquivos
total_size = 0


# Função principal da function
def lambda_handler(event, context):
    # Obtem a chave API do TMDB
    def configure_api_key_tmdb():
        try:
            api_key = os.getenv('TMDB_API_KEY')
            if not api_key:
                raise ValueError('API key não configurada.')
            return api_key
        except Exception as ex:
            raise Exception(f'Erro ao obter API key: {ex}')

    # Conecta API do TMDB
    def fetch_data_from_tmdb(endpoint, params=None):
        base_url = 'https://api.themoviedb.org/3'
        url = f'{base_url}/{endpoint}'
        params['api_key'] = configure_api_key_tmdb()
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                print(f'Erro na requisição: {response.status_code}')
                return None
        except Exception as ex:
            raise Exception(f'Erro ao obter dados da API do TMDB: {ex}')

    # Busca filmes ou séries por gêneros e intervalo de datas
    def get_media_by_genres(media_type, start_year, end_year, genres='18,10749', page=1):
        try:
            endpoint = f'discover/{media_type}'
            date_key = 'primary_release_date' if media_type == 'movie' else 'first_air_date'
            params = {
                'with_genres': genres,
                f'{date_key}.gte': f'{start_year}-01-01',
                f'{date_key}.lte': f'{end_year}-12-31',
                'page': page
            }
            return fetch_data_from_tmdb(endpoint, params)
        except Exception as ex:
            raise Exception(f'Erro ao obter dados de {media_type}: {ex}')

# Carrega o elenco das séries
    def get_series_cast(series_id):
        try:
            endpoint = f'tv/{series_id}/credits'
            data = fetch_data_from_tmdb(endpoint, {})
            if data:
                return data.get('cast', [])
            else:
                return []
        except Exception as ex:
            print(f'Erro ao obter dados do cast: {ex}')
            return []

    # Filtra os resultados com avaliação menor que 5 e maior que zero, ou igual a 0 se a popularidade for diferente de 0
    def filter_by_rating(results):
        try:
            return [result for result in results if
                    ('vote_average' in result and result['vote_average'] < 5 and result['vote_average'] != 0) or
                    ('vote_average' in result and result['vote_average'] == 0 and 'popularity' in result and result[
                        'popularity'] != 0)]
        except Exception as ex:
            raise Exception(f'Erro ao filtrar resultados por avaliação e popularidade: {ex}')

    # Salva os resultados em arquivos JSON no S3
    def save_to_s3(data, filename, media_type):
        global total_size
        try:
            s3 = boto3.resource('s3')
            bucket_name = 'data-lake-otiliano'

            # Gerar a chave no S3
            now = datetime.now()
            file_type = filename.split('.')[-1].upper()
            year = now.strftime("%Y")
            month = now.strftime("%m")
            day = now.strftime("%d")

            media_category = 'Movies' if media_type == 'movie' else 'Series'
            s3_key = f"Raw/TMDB/{file_type}/{media_category}/{year}/{month}/{day}/{filename}"

            # Converter dados em JSON e calcular o tamanho do arquivo
            json_data = json.dumps(data, ensure_ascii=False, indent=4)
            file_size = len(json_data.encode('utf-8'))
            total_size += file_size

            # Salvar os dados no S3
            s3.Object(bucket_name, s3_key).put(Body=json_data)

            print(f'Dados salvos em: s3://{bucket_name}/{s3_key} - Tamanho: {file_size} bytes')

        except Exception as ex:
            raise Exception(f'Erro ao salvar dados no S3: {ex}')

    # Edita os resultados em arquivos JSON de 100 em 100
    def save_results_to_json(media_type, start_year, end_year, genres, filename_prefix):
        try:
            page = 1
            results = []

            while True:
                response = get_media_by_genres(media_type, start_year, end_year, genres, page)
                if not response or 'results' not in response:
                    break

                filtered_results = filter_by_rating(response['results'])

                if media_type == 'tv':
                    # Adiciona o cast para cada série antes de salvar
                    for series in filtered_results:
                        series_id = series['id']
                        series['cast'] = get_series_cast(series_id)

                results.extend(filtered_results)

                # Salva resultados em arquivos de 100 em 100
                if len(results) >= 100:
                    filename = f'{filename_prefix}_{page}.json'
                    save_to_s3(results[:100], filename, media_type)
                    results = results[100:]

                # Verifica se chegou ao fim das páginas disponíveis
                if page >= response['total_pages']:
                    break

                page += 1

            # Salva resultados finais que não preenchem 100 em um arquivo separado
            if results:
                filename = f'{filename_prefix}_{page}.json'
                save_to_s3(results, filename, media_type)

        except Exception as ex:
            raise Exception(f'Erro ao salvar resultados como JSON no S3: {ex}')

    try:
        genres_dict = {
            'drama_romance': '18,10749'
        }
        # Busca filmes de drama e romance de 2019 a 2023
        save_results_to_json('movie', 2019, 2023, genres_dict['drama_romance'], 'movie')

        # Busca séries de drama e romance de 1980 a 2024
        save_results_to_json('tv', 1980, 2024, genres_dict['drama_romance'], 'serie')

        # Converte o tamanho total para MB
        total_size_mb = total_size / (1024 * 1024)

        return {'statusCode': 200, 'body': f'Dados processados com sucesso. Tamanho total: {total_size_mb:.2f} MB'}

    except Exception as ex:
        return {'statusCode': 500, 'body': f'Erro ao processar dados: {ex}'}

