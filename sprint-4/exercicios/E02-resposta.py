# E02
# Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será uma string
# e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.

# É obrigatório aplicar as seguintes funções:
# len
# filter
# lambda

# Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.

# -- Resposta - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def conta_vogais(texto: str) -> int:
    vogais = 'aeiou'
    vogais_filtradas = filter(lambda letra: letra in vogais, texto.lower())
    return len(list(vogais_filtradas))
