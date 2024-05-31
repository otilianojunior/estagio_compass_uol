# Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e
# retorne a soma dos dois. Nessa mesma classe, implemente um método de subtração, que aceita dois
# parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).

# Utilize os valores abaixo para testar seu exercício:
#
# x = 4
# y = 5
# imprima:
#
# Somando: 4+5 = 9
# Subtraindo: 4-5 = -1

class Calculo:
    def somando(self, x, y):
        print(f'Somando: {x}+{y} = {x+y}')

    def subtraindo(self, x, y):
        print(f'Subtraindo: {x}-{y} = {x-y}')


if __name__ == '__main__':
    calc = Calculo()
    calc.somando(4,5)
    calc.subtraindo(4, 5)
