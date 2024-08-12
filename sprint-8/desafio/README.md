# Desafio

Neste desafio, vamos realizar o processamento da camada "trusted" do data lake, que é o resultado da integração das diversas fontes de origem encontradas na camada "raw".

## 1. Processamento (AWS Glue)

Nesta etapa, utilizamos Apache Spark e AWS Glue para executar dois jobs de tratamento de dados: um para processar dados em [CSV](job-csv.py) e outro para [JSON](job-json.py). Os códigos podem ser acessados nos respectivos links. A imagem abaixo mostra os jobs no Glue. Os arquivos Python deste projeto estão comentados com o objetivo de cada função para facilitar a compreensão do código.

- Imagem: ![jobs](../evidencias/jobs-aws-glue.png)

## Data Lake

Aqui está como o Data Lake ficou após a criação da camada `trusted`:

- Imagem: ![data-lake](../evidencias/data-lake.png)

Modelo da camada `trusted`:

- Imagem: ![data-lake-trusted](../evidencias/camada-trusted.png)

Modelo de arquitetura dos arquivos `CSV` armazenados:

- Imagem: ![arquitetura-csv](../evidencias/arquitetura-csv-movies.png)

Modelo de arquitetura dos arquivos `JSON` armazenados:

- Imagem: ![arquitetura-json](../evidencias/arquitetura-json-movies.png)

## Crawler

Nesta etapa, criamos dois crawlers um para carregar os dados do JSON e outro para o CSV.

- Imagem: ![Crawler](../evidencias/crawlers.png)

## Glue Catalog

As tabelas criadas no banco de dados `otiliano-desafio-database` pelos crawlers foram `csv` e `json`.

- Imagem: ![Tabelas](../evidencias/glue-catalog.png)

## Athena

Consultas no Athena mostram que os bancos criados pelos crawlers estão funcionando corretamente:

- Imagem CSV: ![Consulta Athena CSV](../evidencias/athena-csv.png)
- Imagem JSON: ![Consulta Athena JSON](../evidencias/athena-json.png)
