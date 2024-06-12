import hashlib


def gerar_hash():
    gerador_hash = hashlib.sha1()

    while True:
        print("Digite um texto para ser convertido em SHA-1 ou 'fim' para finalizar.")
        texto_entrada = input()

        if texto_entrada.lower() == 'fim':
            break

        if not texto_entrada.strip() or not all(char.isalnum() or char.isspace() for char in texto_entrada):
            print('Entrada inválida. Somente caracteres alfanuméricos e espaços são permitidos.')
            print('- * -' * 15)
            continue

        try:
            gerador_hash.update(texto_entrada.encode('utf-8'))
            hash_hexa = gerador_hash.hexdigest()
            print("O hash SHA-1 do texto é:", hash_hexa)

        except Exception as ex:
            print(f"Ocorreu um erro inesperado: {ex}")
        print('-' * 75)


if __name__ == "__main__":
    gerar_hash()
