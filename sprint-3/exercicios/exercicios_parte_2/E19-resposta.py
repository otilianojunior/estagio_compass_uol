# Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:
# Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!
# import random
# # amostra aleatoriamente 50 números do intervalo 0...500
# random_list = random.sample(range(500),50)

# Use as variáveis abaixo para representar cada operação matemática:
# mediana
# media
# valor_minimo
# valor_maximo

# Importante: Esperamos que você utilize as funções abaixo em seu código:
# random
# max
# min
# sum

import random

random_list = random.sample(range(500), 50)
ordem_list = sorted(random_list)

if len(ordem_list) % 2 == 0:
    meio = len(ordem_list) // 2
    mediana = (ordem_list[meio - 1] + ordem_list[meio]) / 2
else:
    meio = len(ordem_list) // 2
    mediana = ordem_list[meio]

media = sum(ordem_list) / len(ordem_list)

valor_minimo = min(ordem_list)

valor_maximo = max(ordem_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')
