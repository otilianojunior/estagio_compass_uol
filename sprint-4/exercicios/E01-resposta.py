# E01
# Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order
# functions, apresente os 5 maiores valores pares e a soma destes.

# Você deverá aplicar as seguintes funções no exercício:
# map
# filter
# sorted
# sum

# Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
# a lista dos 5 maiores números pares em ordem decrescente;
# a soma destes valores.

# -- Resposta - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def processar_numeros(file_path):
    with open(file_path, 'r') as file:
        numeros = list(map(int, file.readlines()))

    numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
    numeros_pares_ordenados = sorted(numeros_pares, reverse=True)
    cinco_maiores_pares = numeros_pares_ordenados[:5]
    soma_cinco_maiores_pares = sum(cinco_maiores_pares)

    return cinco_maiores_pares, soma_cinco_maiores_pares


cinco_maiores_pares, soma_cinco_maiores_pares = processar_numeros('number.txt')

print(cinco_maiores_pares)
print(soma_cinco_maiores_pares)
