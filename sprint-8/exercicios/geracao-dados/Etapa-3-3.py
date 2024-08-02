# bibliotecas necessárias
import names
import random
import time
import os

# configurações iniciais
random.seed(40)
qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

# Mede o tempo de execução
start_time = time.time()

# Gera uma lista de nomes únicos
AUX = []
for i in range(0, qtd_nomes_unicos):
    AUX.append(names.get_full_name())

print("Gerando {} nomes aleatórios".format(qtd_nomes_aleatorios))

# Gera uma lista de nomes aleatórios a partir dos nomes únicos
dados = []
for i in range(0, qtd_nomes_aleatorios):
    dados.append(random.choice(AUX))

# Define o diretório e o nome do arquivo com caminho relativo
diretorio = 'data'
nome_arquivo = 'nomes_aleatorios.txt'
caminho_arquivo = os.path.join(diretorio, nome_arquivo)

print(caminho_arquivo)

# Certifica-se de que o diretório existe
os.makedirs(diretorio, exist_ok=True)

# Salva os nomes aleatórios em um arquivo de texto
with open(caminho_arquivo, 'w') as file:
    for item in dados:
        file.write(f"{item}\n")

print(f"Dados salvos em {caminho_arquivo}")

# Exibir o tempo total de execução
end_time = time.time()
print(f"Tempo total de execução: {end_time - start_time:.2f} segundos")
