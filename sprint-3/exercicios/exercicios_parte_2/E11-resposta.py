# Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
#
# Dica: leia a documentação do pacote json


import json

with open('person.json') as json_file:
    person = json.load(json_file)
    print(person)
