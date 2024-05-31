import logging
import matplotlib.pyplot as plt
import pandas as pd

from matplotlib.ticker import FuncFormatter


class DesafioEtl:

    def abrir_arquivo(self, nome_arquivo):
        try:
            dados = pd.read_csv(nome_arquivo)
            return dados
        except Exception as ex:
            logging.error(f"Erro, abrir_arquivo: {ex}")
            raise

    def criar_data_frame(self, dados):
        try:
            colunas = ['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type',
                       'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver',
                       'Android Ver']

            data_frame = pd.DataFrame(dados, columns=colunas)

            return data_frame
        except Exception as ex:
            logging.error(f"Erro, criar_data_frame: {ex}")
            raise

    def remover_duplicatas(self, data_frame):
        try:
            apps_unicos = data_frame.drop_duplicates(subset=['App'])
            return apps_unicos
        except Exception as ex:
            logging.error(f"Erro, remover_duplicatas: {ex}")
            raise

    def data_frame_info(self, data_frame):
        try:
            data_frame.info()
            print(data_frame.isnull().sum())
        except Exception as ex:
            logging.error(f"Erro, data_frame_info: {ex}")
            raise

    def preencher_remover_nan(self, data_frame):
        try:
            data_frame.loc[:, 'Rating'] = data_frame['Rating'].fillna(0.0)

            # Remover linhas com NaN nas colunas relevantes
            data_frame = data_frame.dropna(subset=['Content Rating', 'Type', 'Current Ver', 'Android Ver'])

            return data_frame
        except Exception as ex:
            logging.error(f"Erro, preencher_remover_nan: {ex}")
            raise

    def formatar_converter_atributos(self, data_frame):
        try:
            # Remover o caractere '+' e substituir vírgulas por '' usando .loc
            data_frame.loc[:, 'Installs'] = data_frame['Installs'].str.replace('+', '', regex=False)
            data_frame.loc[:, 'Installs'] = data_frame['Installs'].str.replace(',', '', regex=False)

            # Converter para inteiros usando .loc
            data_frame.loc[:, 'Installs'] = data_frame['Installs'].astype(int)

            data_frame.loc[:, 'Price'] = data_frame['Price'].str.replace('$', '', regex=False)
            data_frame.loc[:, 'Price'] = data_frame['Price'].astype(float)

            data_frame.loc[:, 'Reviews'] = data_frame['Reviews'].astype(int)

            data_frame.loc[:, 'Rating'] = data_frame['Rating'].astype(float)

            data_frame.loc[:, 'Last Updated'] = pd.to_datetime(data_frame['Last Updated'])

            return data_frame
        except Exception as ex:
            logging.error(f"Erro,  formatar_converter_atributos: {ex}")
            raise

    def salvar_resultado_txt(self, nome_arquivo_saida, dados):
        try:
            with open(nome_arquivo_saida+'.txt', 'w', encoding='utf-8') as arquivo_saida:
                arquivo_saida.write(f"{dados}\n")
        except Exception as ex:
            logging.error(f"Erro, salvar_resultado_txt: {ex}")
            raise

    def grafico_coluna_top_5_instalacoes(self, data_frame):
        try:
            # Ordenar o DataFrame pela coluna 'Installs' em ordem decrescente
            df_sorted = data_frame.sort_values(by='Installs', ascending=False)

            # Selecionar os top 5 aplicativos
            top_5_apps = df_sorted.head(5)

            # Extrair os nomes dos aplicativos e os números de instalações
            app_names = top_5_apps['App'].to_list()
            install_counts = top_5_apps['Installs'].to_list()

            # Criar o gráfico de barras
            plt.figure(figsize=(10, 6))
            plt.bar(app_names, install_counts, color='green')
            plt.xlabel("Nome dos Apps")
            plt.ylabel('Número de Instalações')
            plt.title('Top 5 Apps por Número de Instalações')
            plt.xticks(rotation=45, ha='right')
            plt.gca().yaxis.set_major_formatter(FuncFormatter(self.formatar_milhoes))
            plt.tight_layout()

            # Exibir o gráfico
            plt.show()

        except Exception as ex:
            logging.error(f"Erro, grafico_coluna_top_5_instalacoes: {ex}")
            raise

    def formatar_milhoes(self, val, pos):
        try:
            if val >= 1e9:
                return f'{val / 1e9:.1f}B'
            else:
                return f'{val / 1e6:.1f}M'
        except Exception as ex:
            logging.error(f"Erro, formatar_milhoes: {ex}")
            raise

    def grafico_pizza_frequencia_categorias(self, data_frame):
        try:
            # Contar o número de ocorrências de cada categoria
            category_counts = data_frame['Category'].value_counts()

            # Selecionar as 10 principais categorias e agrupar as restantes em uma categoria chamada "Outros"
            top_categories = category_counts.head(9)
            other_categories_count = category_counts.iloc[9:].sum()
            top_categories['Outras'] = other_categories_count

            # Criar uma lista de rótulos da legenda formatados com nome da categoria e porcentagem
            legend_labels = [f"{category}: {count / data_frame.shape[0] * 100:.1f}%" for category, count in
                             top_categories.items()]

            # Criar o gráfico de pizza
            plt.figure(figsize=(10, 6))
            patches, texts, autotexts = plt.pie(top_categories, labels=None, autopct='%1.1f%%', startangle=140)
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.title('Distribuição das Categorias')

            # Adicionar a legenda ao lado do gráfico de pizza
            plt.legend(legend_labels, loc="center left", bbox_to_anchor=(1, 0.5), title="Categorias")

            plt.tight_layout()

            # Exibir o gráfico
            plt.show()
        except Exception as ex:
            logging.error(f"Erro, grafico_pizza_frequencia_categorias: {ex}")
            raise

    def app_mais_caro(self, data_frame):
        try:
            # Ordenar o DataFrame pela coluna 'Price' em ordem decrescente
            df_sorted = data_frame.sort_values(by='Price', ascending=False)

            # Selecionar o aplicativo mais caro
            app_mais_caro = df_sorted.iloc[0]  # ou df_sorted.iloc[-1] para o último item

            return app_mais_caro  # Imprimir todos os dados do aplicativo mais caro

        except Exception as ex:
            logging.error(f"Erro, app_mais_caro: {ex}")
            raise

    def numero_apps_mature_17(self, data_frame):
        try:
            # Filtrar o DataFrame para incluir apenas os aplicativos com a classificação 'Mature 17+'
            mature_17_count = data_frame[data_frame['Content Rating'] == 'Mature 17+'].shape[0]
            resultado = "Quantidade de apps com classificação 'Mature 17+':", mature_17_count
            return resultado
        except Exception as ex:
            logging.error(f"Erro, numero_apps_mature_17: {ex}")
            raise

    def top_10_aplicativos_reviews(self, data_frame):
        try:
            # Ordenar o DataFrame pela coluna 'Reviews' em ordem decrescente
            df_sorted = data_frame.sort_values(by='Reviews', ascending=False)

            # Selecionar os top 10 aplicativos
            top_10_apps = df_sorted.head(10)

            # Criar um novo DataFrame com o nome do aplicativo e a quantidade de reviews
            df_top_apps = pd.DataFrame({
                'App': top_10_apps['App'],
                'Reviews': top_10_apps['Reviews']
            })

            return df_top_apps
        except Exception as ex:
            logging.error(f'Erro, top_10_aplicativos_reviews: {ex}')
            raise

    def top_10_apps_avaliados(self, data_frame):
        try:
            # Ordenar o DataFrame pela coluna 'Reviews' em ordem decrescente
            df_sorted = data_frame.sort_values(by='Rating', ascending=False)

            # Selecionar os top 10 aplicativos
            top_10_apps = df_sorted.head(10)

            # Criar um novo DataFrame com o nome do aplicativo e a quantidade de reviews
            df_top_apps = pd.DataFrame({
                'App': top_10_apps['App'],
                'Rating': top_10_apps['Rating']
            })

            return df_top_apps
        except Exception as ex:
            logging.error(f'Erro, top_10_apps_avaliados: {ex}')
            raise

    def quantidade_apps_pagos(self, data_frame):
        try:
            # Contagem de apps e pagos
            apps_pagos = (data_frame['Type'] == 'Paid').sum()

            # Total de apps
            total_apps = len(data_frame)

            # Porcentagem de apps pagos em relação ao total
            porcentagem_apps_pagos = (apps_pagos / total_apps) * 100

            # Mensagem formatada
            mensagem = f"Quantidade de apps pagos: {apps_pagos}, em porcentagem do total: {porcentagem_apps_pagos:.2f}%"

            return mensagem
        except Exception as ex:
            logging.error(f'Erro, quantidade_apps_pagos: {ex}')
            raise

    def grafico_dispersao_app_updates(self, data_frame):
        try:
            # Criar uma cópia do DataFrame para evitar o SettingWithCopyWarning
            df = data_frame.copy()

            # Converter a coluna 'Last Updated' para o tipo de dados de data
            df['Last Updated'] = pd.to_datetime(df['Last Updated'])

            # Extrair o ano da coluna 'Last Updated'
            df['Year'] = df['Last Updated'].dt.year

            # Contagem de atualizações por ano
            atualizacoes_por_ano = df['Year'].value_counts().sort_index()

            # Criar o gráfico de dispersão
            plt.figure(figsize=(10, 6))
            plt.scatter(atualizacoes_por_ano.index, atualizacoes_por_ano.values, color='blue')
            plt.xlabel('Ano de Atualização')
            plt.ylabel('Quantidade de Atualizações')
            plt.title('Quantidade de Atualizações por Ano')
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        except Exception as ex:
            logging.error(f'Erro, grafico__dispersao_app_updates: {ex}')
            raise

    def grafico_linha_genero_instalacoes(self, data_frame):
        try:
            # Agrupar o DataFrame pela coluna 'Genres' e somar as instalações
            df_grouped = data_frame.groupby('Genres')['Installs'].sum().reset_index()

            # Ordenar o DataFrame agrupado pelo número de instalações em ordem decrescente
            df_sorted = df_grouped.sort_values(by='Installs', ascending=False)

            # Selecionar os top 5 gêneros
            top_5_genres = df_sorted.head(5)

            # Reordenar os dados em ordem crescente para o gráfico da esquerda para a direita
            top_5_genres_sorted = top_5_genres.sort_values(by='Installs')

            # Extrair os nomes dos gêneros e os números de instalações
            genre_names = top_5_genres_sorted['Genres'].to_list()
            install_counts = top_5_genres_sorted['Installs'].to_list()

            # Criar o gráfico de linha
            plt.figure(figsize=(10, 6))
            plt.plot(genre_names, install_counts, marker='o', color='green')
            plt.gca().yaxis.set_major_formatter(FuncFormatter(self.formatar_milhoes))
            plt.xlabel('Gênero')
            plt.ylabel('Número de Instalações')
            plt.title('Número de Instalações dos 5 Principais Gêneros')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

        except Exception as ex:
            logging.error(f'Erro, grafico_linha_genero_instalacoes: {ex}')
            raise


if __name__ == '__main__':
    # Exemplo de uso da classe
    etl = DesafioEtl()
    dados = etl.abrir_arquivo('googleplaystore.csv')
    data_frame = etl.criar_data_frame(dados)
    etl.data_frame_info(data_frame)

    data_frame_unicos = etl.remover_duplicatas(data_frame)

    data_frame_nan = etl.preencher_remover_nan(data_frame_unicos)

    dados_corrigidos = etl.formatar_converter_atributos(data_frame_nan)
    etl.data_frame_info(dados_corrigidos)

    grafico_top_5 = etl.grafico_coluna_top_5_instalacoes(dados_corrigidos)

    grafico_categoria = etl.grafico_pizza_frequencia_categorias(dados_corrigidos)

    app_mais_caro = etl.app_mais_caro(dados_corrigidos)
    etl.salvar_resultado_txt('app_mais_caro', app_mais_caro)

    quant_app_mature_17 = etl.numero_apps_mature_17(dados_corrigidos)
    etl.salvar_resultado_txt('app_mature_17', quant_app_mature_17)

    top_10_reviews = etl.top_10_aplicativos_reviews(dados_corrigidos)
    etl.salvar_resultado_txt('top_10_reviews', top_10_reviews)

    top_10_apps_avaliados = etl.top_10_apps_avaliados(dados_corrigidos)
    etl.salvar_resultado_txt('top_10_avaliados', top_10_apps_avaliados)

    app_pagos = etl.quantidade_apps_pagos(dados_corrigidos)
    etl.salvar_resultado_txt('app_pagos', app_pagos)

    grafico_dispersao = etl.grafico_dispersao_app_updates(dados_corrigidos)

    grafico_linhas = etl.grafico_linha_genero_instalacoes(dados_corrigidos)
