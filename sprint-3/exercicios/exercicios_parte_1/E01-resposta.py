# Desenvolva um código em Python que crie variáveis para armazenar o nome e a idade de uma pessoa,
# juntamente com seus valores correspondentes. Como saída, imprima o ano em que a pessoa completará 100 anos de idade.

from datetime import datetime

nome = "Joca"
idade = 25

ano_atual = datetime.today().year
anos_restantes_para_100 = 100 - idade
ano_completara_100 = ano_atual + anos_restantes_para_100


print(ano_completara_100)


