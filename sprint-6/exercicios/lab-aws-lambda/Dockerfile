# Define a imagem base como Amazon Linux em sua última versão
FROM amazonlinux:latest

# Instalar ferramentas necessárias
RUN yum -y update && \
    yum install -y \
        python3 \
        python3-pip \
        zip \
        && yum clean all

# Verificar a versão do Python instalada
RUN python3 --version

# Atualizar pip usando --ignore-installed para ignorar a desinstalação da versão antiga
RUN python3 -m pip install --upgrade --ignore-installed pip

# Instalar pandas e numpy no diretório python
RUN python3 -m pip install pandas numpy -t /lambda/python

# Compactar as dependências para criar a camada
RUN cd /lambda && zip -r /lambda/layer.zip python
