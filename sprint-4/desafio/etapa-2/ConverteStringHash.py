import hashlib


def gerar_hash():
    while True:
        print("Digite algo para ser convertido em SHA-1 ou 'sair' para finalizar.")
        entrada = input()

        if entrada.lower() == "sair":
            break

        if not entrada.strip():
            print("Entrada inválida. Por favor, insira algo válido.")
            print('-' * 65)
            continue

        try:
            hash_obj = hashlib.sha1()
            hash_obj.update(entrada.encode('utf-8'))
            hash_str = hash_obj.hexdigest()

            print("O hash SHA-1 da string é:", hash_str)
        except Exception as ex:
            print("Ocorreu um erro ao calcular o hash:", ex)
        print('-' * 65)


if __name__ == "__main__":
    gerar_hash()
