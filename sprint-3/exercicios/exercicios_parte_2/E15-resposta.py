# Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, True se a lâmpada estiver ligada,
# False caso esteja desligada. A classe Lampada possuí os seguintes métodos:
# liga(): muda o estado da lâmpada para ligada
# desliga(): muda o estado da lâmpada para desligada
# esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário
# Para testar sua classe:
#
# Ligue a Lampada
# Imprima: A lâmpada está ligada? True
# Desligue a Lampada
# Imprima: A lâmpada ainda está ligada? False


class Lampada:
    def __init__(self, status_inicial):
        if status_inicial:
            self.ligada = True
        else:
            self.ligada = False

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        return self.ligada


if __name__ == '__main__':
    lampada = Lampada(False)
    lampada.liga()
    print(f'A Lâmpada está ligada? {lampada.esta_ligada()}')

    lampada.desliga()
    print(f'A Lâmpada ainda está ligada? {lampada.esta_ligada()}')


