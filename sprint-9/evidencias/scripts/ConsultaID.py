import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv(dotenv_path='.env')


# Função para obter a chave API do TMDB
def obter_chave_api_tmdb():
    try:
        api_key = os.getenv('TMDB_API_KEY')
        if not api_key:
            raise ValueError('API key não configurada.')
        return api_key
    except Exception as ex:
        raise Exception(f'Erro ao obter API key: {ex}')


# Função para conectar à API do TMDB
def conectar_api_tmdb(endpoint, params=None):
    base_url = 'https://api.themoviedb.org/3'
    url = f'{base_url}/{endpoint}'
    if params is None:
        params = {}
    params['api_key'] = obter_chave_api_tmdb()
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Erro na requisição: {response.status_code}')
            return None
    except Exception as ex:
        raise Exception(f'Erro ao obter dados da API do TMDB: {ex}')


def buscar_filmes_por_titulo_e_genero(titulo, generos, max_pages=None):
    pagina = 1
    resultados = []
    while True:
        params = {
            'query': titulo,
            'page': pagina,
            'with_genres': ','.join(map(str, generos))  # Gêneros separados por vírgula
        }
        resposta = conectar_api_tmdb('search/movie', params)

        if not resposta or 'results' not in resposta or not resposta['results']:
            break

        resultados.extend(resposta['results'])
        pagina += 1

        if max_pages and pagina > max_pages:
            break

    # Montar o dicionário final com todos os filmes encontrados
    dicionario_filmes = {filme['id']: {'title': filme['title'], 'release_date': filme['release_date']} for filme in
                         resultados}

    return dicionario_filmes


def buscar_detalhes_filmes(ids_filmes):
    detalhes = {}
    for id_filme in ids_filmes:
        params = {}
        resposta = conectar_api_tmdb(f'movie/{id_filme}', params)

        if resposta:
            detalhes[id_filme] = {
                'budget': resposta.get('budget', 'Não disponível'),
                'revenue': resposta.get('revenue', 'Não disponível')
            }
    return detalhes


def main():
    try:
        # IDs dos gêneros para Drama e Romance
        generos = [18, 10749]  # Drama = 18, Romance = 10749
        filmes = buscar_filmes_por_titulo_e_genero('The Great Gatsby', generos)
        ids_filmes = filmes.keys()  # Coleta os IDs dos filmes encontrados

        detalhes_filmes = buscar_detalhes_filmes(ids_filmes)

        for id_filme, info in filmes.items():
            detalhes = detalhes_filmes.get(id_filme, {})
            print(f"ID: {id_filme}, Título: {info['title']}, Data de Lançamento: {info['release_date']}, "
                  f"Custo: {detalhes.get('budget', 'Não disponível')}, Bilheteira: {detalhes.get('revenue', 'Não disponível')}")
    except Exception as ex:
        print(f'Erro: {str(ex)}')


if __name__ == '__main__':
    main()
