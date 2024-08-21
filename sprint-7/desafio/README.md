# Desafio Etapa 1

Nesta etapa do desafio, iremos capturar dados do TMDB via AWS Lambda realizando chamadas de API. Os dados coletados devem ser persistidos no Amazon S3, mantendo o formato original (JSON) e, se possível, agrupando em arquivos com no máximo 100 registros cada.

O objetivo é complementar os dados dos Filmes e Séries, carregados na ETAPA 1, com dados oriundos do TMDB (API).

## 1. Criar a Função Lambda (loadDataTMDB)
- Imagem: ![Função Lambda](../evidencias/lambda-load-tmdb.png)

## 2. Construção do Código
- O código da função pode ser acessado neste arquivo: [load_data_tmdb](../desafio/etapa-1/load_data_TMDB.py)

## 3. Criar um Layer (layer-load-tmdb)
- Criamos um layer com as bibliotecas necessárias para a execução da função.
- As bibliotecas podem ser vistas aqui: [requirements.txt](../desafio/etapa-1/requirements.txt)
- A partir da execução de um Dockerfile Python, compactaremos as dependências para criar a camada.
- O arquivo Dockerfile pode ser encontrado aqui: [Dockerfile](../desafio/etapa-1/Dockerfile)
- O comando do Dockerfile já gera o zip, então só precisamos copiá-lo para um local fora da imagem para ter acesso.
- Para isso, utilizamos o seguinte código:

```sh
docker build -t load_data_image .
docker run --rm -v $(pwd):/host load_data_image cp /lambda/layer-load-tmdb.zip /host/
```

- Imagem: ![build-zip](../evidencias/build-zip.png)

- Vale lembrar que estou em um ambiente de execução Linux, logo os comandos podem ser diferentes para outro SO.

## 4. Acesso do Lambda ao Bucket (ROLE)
- Imagem: ![role-lambda-bucket](../evidencias/role-acesso-lambda-bucket.png)

## 5. Upload do Zip em Bucket (layer-load-tmdb.zip)
- Como o zip possui mais de 10MB, é recomendado subir em um bucket S3.
- Imagem: ![Layer zip](../evidencias/layer-load-tmdb-zip.png)
- Criamos uma pasta `layer` para colocar os arquivos zip-layer do projeto.
- Imagem: ![data lake](../evidencias/data-lake.png)

## 6. Layer Configurado
- Imagem: ![Layer](../evidencias/layer-load-tmdb.png)

## 7. Lambda com Layer Configurado (loadDataTMDB)
- Imagem: ![Lambda Layer](../evidencias/lambda-load-tmdb.png)

## 8. Amazon EventBridge Schedules (trigger-lambda-tmdb)
- Imagem: ![EventBridge](../evidencias/eventbridge.png)
- O agendamento foi feito para executar uma vez às 13:41 do dia 24 de julho de 2024

## 9. Execução da Função (loadDataTMDB)
- Imagem: ![Função em Execução](../evidencias/execução-lambda.png)

## 10. Arquivos Upados (data-lake-otiliano)
- Imagem: ![load-movies](../evidencias/load_movie.png)
- Imagem: ![load-series](../evidencias/load-serie.png)

## Atualizações

Após uma análise aprofundada do material obtido na API TMDb, decidi focar em filmes do gênero **Drama**. 
As motivações e justificativas para essa escolha podem ser consultadas neste [README](../../README.md). 

Na consulta realizada para adquirir os dados da camada raw, utilizei os IDs dos filmes que serão analisados.

A lista de filmes selecionados é a seguinte:

- A Noviça Rebelde
- Até o Último Homem
- Ben-Hur
- O Sexto Sentido
- Coringa
- Homens de Honra
- À Procura da Felicidade
- Histórias Cruzadas
- Interestelar
- Sempre ao Seu Lado
- Intocáveis
- O Silêncio dos Inocentes
- O Poderoso Chefão
- A Vida é Bela
- À Espera de um Milagre
- Forrest Gump - O Contador de Histórias
- A Lista de Schindler
- Um Sonho de Liberdade
- Anna Karenina
- A Star Is Born

Para obter esses filmes, utilizei o código [consulta_id](../../sprint-9/evidencias/scripts/ConsultaID.py) 
para extrair os IDs. Abaixo está o código em execução:

![consulta-id](../../sprint-9/evidencias/fotos/consulta_id_execucao.png)

```python
lista_id = [238, 242, 240, 278, 424, 13, 497, 637, 857, 274, 77338, 28178, 157336, 50014, 1402, 11978, 475557,
            745, 665, 271969, 324786, 15121, 332562, 3111, 19610, 96724, 70881, 50512]
```

Após obter os IDs corretos para o gênero selecionado, atualizei o código para salvar o resultado da consulta na camada 
raw, em um arquivo JSON, seguindo todos os padrões estabelecidos.

