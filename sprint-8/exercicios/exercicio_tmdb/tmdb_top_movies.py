# Importação das bibliotecas necessárias
from dotenv import load_dotenv
import requests
import pandas as pd
from IPython.display import display
import os

# Carrega o arquivo .env e define variáveis de ambiente
load_dotenv()

# Obtém a chave da API TMDB do ambiente
api_key = os.getenv('TMDB_API_KEY')

# Define a URL da API para obter os filmes mais bem avaliados, utilizando a chave da API
url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR'

# Faz a requisição HTTP para a API
response = requests.get(url)

# Converte a resposta da requisição para o formato JSON
data = response.json()

# Lista para armazenar as informações dos filmes
filmes = []

# Itera sobre cada filme nos resultados retornados pela API
for movie in data['results']:
    # Cria um dicionário com as informações relevantes do filme
    df = {'Titulo': movie['title'], 'Data Lançamento': movie['release_date'], 'Visão Geral': movie['overview'],
          'Votos': movie['vote_count'], 'Média de votos': movie['vote_average']}
    # Adiciona o dicionário à lista de filmes
    filmes.append(df)

# Converte a lista de dicionários em um DataFrame do pandas
df = pd.DataFrame(filmes)

# Exibe o DataFrame
display(df)
