# Etapa 1
# Apresente o ator/atriz com maior número de filmes e a respectiva quantidade.
# A quantidade de filmes se encontra na coluna Numer of movies do aruqivo.

# Etapa 2
# Apresente a média de receita de bilheteria bruta dos principais filmes, considerando todos os
# Estamos falando aqui da média da conluna Gross.

# Etapa 3
# Apresente ator/atriz com a maior média de receita de bilheteria bruta por filme do conjunto de dados.
# Considere a coluna Average per Movie parra fins de cálculo.

# Etapa 4
# A coluna #1 Movie contém o filme de maior bilheteria em que o ator atuou. Realize a contagem de aparições
# destes filmes do dataset, listando-os ordenados pela quantiodade de vezes que estão presentes. Considere
# a ordem crescente e, em segundo nível, o nome do filme.
# Ao escrever no arquivo, considere o padrão de saída(sequencia) - O filme (nome filme) aparece (quantidade) vez(es)
# no dataset, adicioando um resultado a cada linha.

# Etapa 5
# Apresente a lista dos atores ordenada pela receita bruta de bilheteria de seus filmes (conluna Total Gross), em
# ordem decrescente
# Ao escrever no arquivo, considere o padrão de saída (nome do ator) - (receita total bruta), adicionando um
# resultado a cada linha.

import sys


class ExercicioEtl:
    def __init__(self):
        self.arquivo = None

    def abrir_arquivo(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                conteudo_arquivo = arquivo.read()
            return conteudo_arquivo
        except Exception as ex:
            print(f"\033[91m Erro, def abrir arquivo: {ex} \033[0m")
            sys.exit(1)

    def tratar_dados(self, dados_arquivo):
        try:
            linhas = dados_arquivo.strip().split("\n")
            cabecalho = linhas[0].split(",")
            lista_dados_tratados = []

            for linha in linhas[1:]:
                valores = self.dividir_linha(linha)
                valores_sem_aspas = self.remover_aspas(valores)
                dado = self.criar_dados(cabecalho, valores_sem_aspas)
                lista_dados_tratados.append(dado)

            return lista_dados_tratados
        except Exception as ex:
            print(f"\033[91m Erro, def tratar dados: {ex} \033[0m")
            sys.exit(1)

    def dividir_linha(self, linha):
        try:
            valores = []
            dentro_aspas = False
            campo = ''

            for char in linha:
                if char == '"':
                    dentro_aspas = not dentro_aspas
                elif char == ',' and not dentro_aspas:
                    valores.append(campo)
                    campo = ''
                else:
                    campo += char

            valores.append(campo)
            return valores
        except Exception as ex:
            print(f"\033[91m Erro, def dividir linha: {ex} \033[0m")
            sys.exit(1)

    def remover_aspas(self, valores):
        try:
            return [valor.replace('"', '') for valor in valores]
        except Exception as ex:
            print(f"\033[91m Erro: def remover aspas: {ex} \033[0m")
            sys.exit(1)

    def criar_dados(self, cabecalho, valores):
        try:
            ator = valores[0]
            dado = {'Actor': ator}

            for cab, valor in zip(cabecalho[1:], valores[1:]):
                dado[cab.strip()] = valor.strip()

            return dado
        except Exception as ex:
            print(f"\033[91m Erro, def criar dados: {ex} \033[0m")
            sys.exit(1)

    def salvar_resultado(self, nome_arquivo_saida, dados):
        try:
            with open(nome_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
                for item in dados:
                    arquivo_saida.write(f"{item}\n")
            print(f"\033[92m Sucesso: Resultado salvo em {nome_arquivo_saida} \033[0m")
        except Exception as ex:
            print(f"\033[91m Erro, def salvar resultado: {ex}\033[0m")
            sys.exit(1)

    # Etapa-1
    def ator_com_mais_filmes(self, dados):
        try:
            ator_com_mais_filmes = None

            for ator in dados:
                numero_filmes_ator_atual = int(ator['Number of Movies'])
                if not ator_com_mais_filmes or numero_filmes_ator_atual > int(ator_com_mais_filmes['Number of Movies']):
                    ator_com_mais_filmes = ator

            resultado_formatado = [f"O Ator com maior número de filmes no dataset é {ator_com_mais_filmes['Actor']}, "
                                   f"com {ator_com_mais_filmes['Number of Movies']} filmes."]

            return resultado_formatado
        except Exception as ex:
            print(f"\033[91m Erro, def ator com mais filmes: {ex} \033[0m")
            sys.exit(1)

    # Etapa-2
    def media_receita_bilheteria(self, dados):
        try:
            soma = 0
            total_elementos = 0

            for dado in dados:
                soma += float(dado['Gross'])
                total_elementos += 1

            media = round(soma / total_elementos, 2)

            resultado_formatado = ([f'Média de receita de bilheteria bruta: {media}'])

            return resultado_formatado
        except Exception as ex:
            print(f"\033[91m Erro, def media receita bilheteria: {ex} \033[0m")
            sys.exit(1)

    # Etapa-3
    def ator_maior_media_receita_bilheteria(self, dados):
        try:
            ator_com_maior_media = None

            for ator in dados:
                media_ator_atual = float(ator['Average per Movie'])
                if not ator_com_maior_media or media_ator_atual > float(ator_com_maior_media['Average per Movie']):
                    ator_com_maior_media = ator

            resultado_formatado = [f"O ator com maior média de bilheteria no dataset é {ator_com_maior_media['Actor']},"
                                   f" com {ator_com_maior_media['Average per Movie']} por filme."]
            return resultado_formatado
        except Exception as ex:
            print(f"\033[91m Erro, def ator maior media receita bilheteria: {ex} \033[0m")
            sys.exit(1)

    # Etapa-4
    def contar_filmes(self, dados):
        contagem_filmes = {}
        try:
            for dado in dados:
                filme = dado['#1 Movie']
                if filme in contagem_filmes:
                    contagem_filmes[filme] += 1
                else:
                    contagem_filmes[filme] = 1

            filmes_ordenados = sorted(contagem_filmes.items(), key=lambda x: (-x[1], x[0]))

            resultados_formatados = [f"{idx + 1} - O filme {item[0]} aparece {item[1]} vezes no dataset"
                                     for idx, item in enumerate(filmes_ordenados)]

            return resultados_formatados
        except Exception as ex:
            print(f"\033[91m Erro: def contar filmes: {ex}\033[0m")
            sys.exit(1)

    # Etapa-5
    def lista_ordenada_por_total_gross(self, dados):
        try:
            lista_ordenada = []
            for dado in dados:
                lista_ordenada.append((dado["Actor"], dado["Total Gross"]))
            lista_ordenada.sort(key=lambda x: float(x[1]), reverse=True)

            resultados_formatados = [f"{item[0]} - {item[1]}" for item in lista_ordenada]

            return resultados_formatados
        except Exception as ex:
            print(f"\033[91m Erro, def lista ordenada por total gross: {ex}\033[0m")
            sys.exit(1)

    def __del__(self):
        if self.arquivo and not self.arquivo.closed:
            self.arquivo.close()


if __name__ == '__main__':
    exercicio = ExercicioEtl()
    conteudo = exercicio.abrir_arquivo("actors.csv")
    dados_tratados = exercicio.tratar_dados(conteudo)

    # Etapa-1

    ator_maior_numero_filmes = exercicio.ator_com_mais_filmes(dados_tratados)
    exercicio.salvar_resultado('etapa-1.txt', ator_maior_numero_filmes)

    # Etapa-2

    media_receita_bruta = exercicio.media_receita_bilheteria(dados_tratados)
    exercicio.salvar_resultado('etapa-2.txt', media_receita_bruta)

    # Etapa-3

    ator_maior_media = exercicio.ator_maior_media_receita_bilheteria(dados_tratados)
    exercicio.salvar_resultado('etapa-3.txt', ator_maior_media)

    # Etapa-4

    lista_filmes = exercicio.contar_filmes(dados_tratados)
    exercicio.salvar_resultado('etapa-4.txt', lista_filmes)

    # Etapa-5

    lista_total_gross = exercicio.lista_ordenada_por_total_gross(dados_tratados)
    exercicio.salvar_resultado('etapa-5.txt', lista_total_gross)
