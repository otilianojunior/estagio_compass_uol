# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o script Python e o arquivo .env para o diretório de trabalho
COPY . .

# Defina o ponto de entrada do contêiner para executar o script Python
ENTRYPOINT ["python", "data_loader.py"]
