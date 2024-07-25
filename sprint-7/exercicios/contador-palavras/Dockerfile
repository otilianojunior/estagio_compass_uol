# Use a imagem base com Spark e Jupyter Notebook
FROM jupyter/pyspark-notebook:latest

# Exponha a porta 8888 para acesso ao Jupyter Notebook
EXPOSE 8888

# (Opcional) Defina um diretório de trabalho e volume se necessário
WORKDIR /app
VOLUME ["/app/data"]

# Instalando as dependências
RUN pip install unidecode
