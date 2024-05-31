# Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles.
# Depois imprima a soma dos valores.
#
# A string deve ter valor  "1,3,4,6,10,76"


def soma_str(string):
    lista_split = string.split(',')
    lista_numeros = [int(i) for i in lista_split]
    print(sum(lista_numeros))


soma_str("1,3,4,6,10,76")
