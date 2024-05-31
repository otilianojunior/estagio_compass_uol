# Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3
# partes iguais. Teste sua implementação com a lista abaixo
#
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def separa_lista(lista, partes):
    n = len(lista) // partes
    listas_divididas = [lista[i * n:(i + 1) * n] for i in range(partes)]
    return listas_divididas


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
listas_divididas = separa_lista(lista, 3)

output = ' '.join(str(sublista) for sublista in listas_divididas)
print(output)
