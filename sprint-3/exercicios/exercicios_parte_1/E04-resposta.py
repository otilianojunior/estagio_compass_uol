# Escreva um código Python para imprimir todos os números primos entre 1 até 100.
# Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.

# Importante: Aplique a função range().
import math


def primo(n):
    if n <= 1:
        return False
    elif n <= 3 or n == 5:
        return True
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    else:
        for i in range(5, math.isqrt(n), 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True


for numero in range(1, 101):
    if primo(numero):
        print(numero)

