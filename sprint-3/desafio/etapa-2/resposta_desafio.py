import pandas as pd
import logging
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


class ExercicioEtl:

    def abrir_arquivo(self, nome_arquivo):
        try:
            dados = pd.read_csv(nome_arquivo)
            return dados
        except Exception as ex:
            logging.error(f"Erro ao abrir o arquivo: {ex}")
            raise

    def criar_data_frame(self, dados):
        try:
            colunas = ['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type',
                       'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver',
                       'Android Ver']

            data_frame = pd.DataFrame(dados, columns=colunas)

            return data_frame
        except Exception as ex:
            logging.error(f"Erro ao criar dataframe: {ex}")
            raise

    def remover_duplicatas(self, df):
        try:
            data_frame_unico = df.drop_duplicates(subset=['App'])
            return data_frame_unico
        except Exception as ex:
            logging.error(f"Erro ao remover duplicatas do dataframe: {ex}")
            raise

    def data_frame_info(self, data_frame):
        try:
            data_frame.info()
            print(data_frame.isnull().sum())
        except Exception as ex:
            logging.error(f"Erro, data_frame_info: {ex}")

    def corrigir_dados_nan(self, data_frame):
        try:
            data_frame.loc[:, 'Rating'] = data_frame['Rating'].fillna(0.0)

            # Remover linhas com NaN nas colunas relevantes
            data_frame = data_frame.dropna(subset=['Content Rating', 'Type', 'Current Ver', 'Android Ver'])

            return data_frame
        except Exception as ex:
            logging.error(f"Erro em corrigir_dados_nan: {ex}")
            raise

    def alterar_valor(self, data_frame):
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
            logging.error(f"Erro alterar_valor: {ex}")
            raise

    def salvar_resultado(self, nome_arquivo_saida, dados):
        try:
            with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
                arquivo_saida.write(f"{dados}\n")
            logging.info(f"Sucesso: Resultado salvo: '{nome_arquivo_saida}'")
        except Exception as ex:
            logging.error(f"Erro, salvar_resultado: {ex}")
            raise

    def grafico_barras(self, df):
        try:
            # Ordenar o DataFrame pela coluna 'Installs' em ordem decrescente
            df_sorted = df.sort_values(by='Installs', ascending=False)

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
            logging.error(f"Erro ao graficar os dados: {ex}")
            raise

    def formatar_milhoes(self, val, pos):
        if val >= 1e9:
            return f'{val / 1e9:.1f}B'
        else:
            return f'{val / 1e6:.1f}M'

    def grafico_pizza(self, df):
        try:
            # Contar o número de ocorrências de cada categoria
            category_counts = df['Category'].value_counts()

            # Selecionar as 10 principais categorias e agrupar as restantes em uma categoria chamada "Outros"
            top_categories = category_counts.head(9)
            other_categories_count = category_counts.iloc[9:].sum()
            top_categories['Outras'] = other_categories_count

            # Criar uma lista de rótulos da legenda formatados com nome da categoria e porcentagem
            legend_labels = [f"{category}: {count / df.shape[0] * 100:.1f}%" for category, count in
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
            logging.error(f"Erro ao graficar os dados: {ex}")
            raise

    def app_mais_caro(self, df):
        try:
            # Ordenar o DataFrame pela coluna 'Price' em ordem decrescente
            df_sorted = df.sort_values(by='Price', ascending=False)

            # Selecionar o aplicativo mais caro
            app_mais_caro = df_sorted.iloc[0]  # ou df_sorted.iloc[-1] para o último item

            return app_mais_caro  # Imprimir todos os dados do aplicativo mais caro

        except Exception as ex:
            logging.error(f"Erro, app_mais_caro: {ex}")
            raise

    def app_mature_17(self, df):
        try:
            # Filtrar o DataFrame para incluir apenas os aplicativos com a classificação 'Mature 17+'
            mature_17_count = df[df['Content Rating'] == 'Mature 17+'].shape[0]
            valor = "Quantidade de apps com classificação 'Mature 17+':", mature_17_count
            return valor
        except Exception as ex:
            logging.error(f"Erro, app_mature_17: {ex}")
            raise

    def app_num_reviews(self, df):
        try:
            # Ordenar o DataFrame pela coluna 'Reviews' em ordem decrescente
            df_sorted = df.sort_values(by='Reviews', ascending=False)

            # Selecionar os top 10 aplicativos
            top_10_apps = df_sorted.head(10)

            # Criar um novo DataFrame com o nome do aplicativo e a quantidade de reviews
            df_top_apps = pd.DataFrame({
                'App': top_10_apps['App'],
                'Reviews': top_10_apps['Reviews']
            })

            return df_top_apps
        except Exception as ex:
            logging.error(f'Erro, app_num_reviews: {ex}')
            raise

    def top_10_apps_avaliados(self, df):
        try:
            # Ordenar o DataFrame pela coluna 'Reviews' em ordem decrescente
            df_sorted = df.sort_values(by='Rating', ascending=False)

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

    def app_pagos(self, df):
        try:
            # Contagem de apps grátis e pagos
            apps_pagos = (df['Type'] == 'Paid').sum()
            apps_gratis = (df['Type'] == 'Free').sum()

            # Total de apps
            total_apps = len(df)

            # Porcentagem de apps pagos em relação ao total
            porcentagem_apps_pagos = (apps_pagos / total_apps) * 100

            # Mensagem formatada
            mensagem = f"Quantidade de apps pagos: {apps_pagos}, em porcentagem do total: {porcentagem_apps_pagos:.2f}%"

            return mensagem
        except Exception as ex:
            logging.error(f'Erro, app_pago_menor_preco: {ex}')
            raise

    def grafico_dispersao(self, df):
        try:
            # Criar uma cópia do DataFrame para evitar o SettingWithCopyWarning
            df = df.copy()

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
            plt.title('Quantidade de Atualizações por Ano (Dispersão)')
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        except Exception as ex:
            logging.error(f'Erro, grafico_dispersao: {ex}')
            raise

    def grafico_linha_tamanho(self, df):
        try:
            # Filtrar os valores 'Varies with device' na coluna 'Size'
            df = df[df['Size'] != 'Varies with device']

            # Converter os valores para KB
            df.loc[:, 'Size'] = df['Size'].apply(self.convert_to_kb)

            # Ordene o DataFrame pelo tamanho dos aplicativos
            df_sorted = df.sort_values(by='Size', ascending=False)

            # Selecionar os 5 maiores aplicativos
            top_5_apps = df_sorted.head(5)

            # Criar um gráfico de linha para os 5 maiores aplicativos
            plt.figure(figsize=(10, 6))
            for index, row in top_5_apps.iterrows():
                plt.plot(row['Size'], row.name, marker='o')

            plt.xlabel('Tamanho do Aplicativo (KB)')
            plt.ylabel('Índice do Aplicativo')
            plt.title('Tamanho dos 5 Maiores Aplicativos')
            plt.yticks(top_5_apps.index, top_5_apps['App'])  # Usar os nomes dos aplicativos como rótulos no eixo y
            plt.tight_layout()
            plt.show()

        except Exception as ex:
            logging.error(f'Erro, grafico_linha_tamanho: {ex}')
            raise

    def convert_to_kb(self, size_str):
        try:
            if 'M' in size_str:
                return float(size_str.replace('M', '')) * 1024  # Convert MB to KB
            elif 'k' in size_str:
                return float(size_str.replace('k', ''))  # KB already
            else:
                return float(size_str)
        except Exception as ex:
            logging.error(f'Erro, convert_to_kb: {ex}')
            raise Exception


# Exemplo de uso da classe
etl = ExercicioEtl()
dados = etl.abrir_arquivo('googleplaystore.csv')
data_frame = etl.criar_data_frame(dados)
# etl.data_frame_info(data_frame)

data_frame_unicos = etl.remover_duplicatas(data_frame)
# etl.data_frame_info(data_frame_unicos)

data_frame_nan = etl.corrigir_dados_nan(data_frame_unicos)
# etl.data_frame_info(data_frame_nan)

dados_corrigidos = etl.alterar_valor(data_frame_nan)
# etl.data_frame_info(dados_corrigidos)

# grafico_top_5 = etl.grafico_barras(dados_corrigidos)
#
# grafico_categoria = etl.grafico_pizza(dados_corrigidos)

# app_mais_caro = etl.app_mais_caro(dados_corrigidos)
# etl.salvar_resultado('app_mais_caro.txt', app_mais_caro)

# valor = etl.app_mature_17(dados_corrigidos)
# etl.salvar_resultado('app_mature_17.txt', valor)

# top_10_reviews = etl.app_num_reviews(dados_corrigidos)
# etl.salvar_resultado('top_10_reviews.txt', top_10_reviews)

# top_10_apps_avaliados = etl.top_10_apps_avaliados(dados_corrigidos)
# etl.salvar_resultado('top_10_avaliados.txt', top_10_apps_avaliados)

# app_pagos = etl.app_pagos(dados_corrigidos)
# etl.salvar_resultado('app_pagos.txt', app_pagos)

# grafico_dispersao = etl.grafico_dispersao(dados_corrigidos)

grafico_linhas = etl.grafico_linha_tamanho(dados_corrigidos)
