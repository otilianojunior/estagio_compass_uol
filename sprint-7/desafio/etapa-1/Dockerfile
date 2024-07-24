# Define a imagem base como Amazon Linux em sua última versão
FROM amazonlinux:latest

# Instalar ferramentas necessárias
RUN yum -y update && \
    yum install -y \
        python3 \
        python3-pip \
        zip \
        && yum clean all

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instalar dependências do requirements.txt no diretório /lambda/python
RUN python3 -m pip install --no-cache-dir -r requirements.txt -t /lambda/python

# Compactar as dependências para criar a camada
RUN cd /lambda && zip -r /lambda/layer-load-tmdb.zip python
