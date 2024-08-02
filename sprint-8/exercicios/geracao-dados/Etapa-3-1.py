# bibliotecas necessárias
import random


# Gera 250 números aleatórios
def gera_numeros_random():
    try:
        list_numbers = random.sample(range(1, 1000), 250)
        return list_numbers
    except Exception as ex:
        raise Exception(f"Erro ao gerar números aleatórios: {ex}")


# Reverte o resultado de uma lista
def reverse_result(list_numbers):
    try:
        list_numbers.reverse()
        return list_numbers
    except Exception as ex:
        raise Exception(f"Erro ao aplicar reverse no resultado: {ex}")


# Bloco de execução
if __name__ == '__main__':
    lista_random = gera_numeros_random()
    lista_reversa = reverse_result(lista_random)
    print("Lista revertida:", lista_reversa)
