# Implemente duas classes, Pato e Pardal , que herdam de uma superclasse chamada Passaro as habilidades de voar e emitir som.
# Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, conforme o modelo a seguir.
# Imprima no console exatamente assim:
#
# Pato
# Voando...
# Pato emitindo som...
# Quack Quack
# Pardal
# Voando...
# Pardal emitindo som...
# Piu Piu


class Passaro:
    def voar(self):
        print("Voando...")

    def emitir_som(self):
        print("Passaro emitindo som...")


class Pato(Passaro):
    def emitir_som(self):
        super().emitir_som()
        print("Quack Quack")


class Pardal(Passaro):
    def emitir_som(self):
        super().emitir_som()
        print("Piu Piu")


if __name__ == "__main__":
    print("Pato")
    pato = Pato()
    pato.voar()
    pato.emitir_som()

    print("Pardal")
    pardal = Pardal()
    pardal.voar()
    pardal.emitir_som()
