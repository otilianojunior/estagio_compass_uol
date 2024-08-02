# bibliotecas necessárias
import csv
import os


# Ordena uma lista utilizando a função sort
def ordena_lista(lista):
    try:
        lista.sort()
        return lista
    except Exception as ex:
        raise Exception(f"Erro ao ordenar lista: {ex}")


# Salva o resultado em um arquivo csv no diretório data
def salvar_lista(lista, nome_arquivo):
    try:
        diretorio = 'data'
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        os.makedirs(diretorio, exist_ok=True)

        with open(caminho_arquivo, mode='w', newline='') as file:
            writer = csv.writer(file)
            for item in lista:
                writer.writerow([item])
    except Exception as ex:
        raise Exception(f"Erro ao salvar lista em arquivo CSV: {ex}")


if __name__ == '__main__':
    # Lista de animais utilizada
    lista_animais = ["Orca", "Elefante", "Tigre", "Tubarão Branco", "Pinguim", "Camaleão", "Girafa", "Gorila", "Polvo",
                     "Morcego", "Baleia Azul", "Panda", "Hipopótamo", "Cachorro", "Gato", "Cavalo", "Canguru",
                     "Tartaruga", "Golfinho", "Arara"]

    lista_animais_ordenada = ordena_lista(lista_animais)
    print("Lista ordenada:", lista_animais_ordenada)
    salvar_lista(lista_animais_ordenada, 'lista_animais_ordenada.csv')
