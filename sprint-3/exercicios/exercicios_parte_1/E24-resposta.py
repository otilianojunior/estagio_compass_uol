class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        listaOrdenada = sorted(self.listaBaguncada)
        return listaOrdenada

    def ordenacaoDecrescente(self):
        listaOrdenada = sorted(self.listaBaguncada, reverse=True)
        return listaOrdenada


if __name__ == '__main__':
    crescente = Ordenadora([3, 4, 2, 1, 5])
    decrescente = Ordenadora([9, 7, 6, 8])

    resultado_crescente = crescente.ordenacaoCrescente()
    resultado_decrescente = decrescente.ordenacaoDecrescente()

    print(resultado_crescente)
    print(resultado_decrescente)
