# E05
# Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. Cada linha do arquivo
# corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. É o arquivo estudantes.csv
# de seu exercício.
#
# Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as
# seguintes informações:
#
#
# Nome do estudante
# Três maiores notas, em ordem decrescente
# Média das três maiores notas, com duas casas decimais de precisão
#
# O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e
# obedecendo ao formato descrito a seguir:
#
#
# Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>


# -- Resposta - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import csv


def processar_notas(arquivo):
    with open(arquivo, 'r', newline='') as file:
        conteudo_arquivo = csv.reader(file)
        lista_estudantes = [(linha[0], sorted(map(int, linha[1:]), reverse=True)[:3]) for linha in conteudo_arquivo]

    for nome, notas in sorted(lista_estudantes):
        media = round(sum(notas) / 3, 2)
        relatorio = f"Nome: {nome} Notas: {notas} Média: {media}"
        print(relatorio)


processar_notas('estudantes.csv')



