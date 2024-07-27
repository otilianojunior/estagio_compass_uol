# Laboratório de AWS Glue

## 1. Upload de Dados

Upload do arquivo `nomes.csv`:

![Upload de Nomes](evidencias/nomes-upload.png)

## 2. Configuração do AWS Glue

### Grupos de Permissão

![Grupos de Permissão](evidencias/groups-permissao.png)

### Permissões do Grupo Developers

![Permissões do Grupo Developers](evidencias/permissoes-developers.png)

### Permissões do AWS Glue

![Permissões do AWS Glue](evidencias/aws-glue-permissoes.png)

## 3. Job no AWS Glue

O arquivo com o código utilizado pode ser encontrado [aqui](job_aws_glue_lab_4.py).

## Exercícios

### Impressão do Schema

![Schema](evidencias/schema.png)

### Impressão da Contagem de Linhas

![Contagem de Linhas](evidencias/quantidade_linhas.png)

### Impressão da Contagem de Nomes

Contagem de nomes agrupados pelos campos ano e sexo:

![Contagem de Nomes Agrupados](evidencias/contagem_nomes_agrupados.png)

### Nome Feminino com Mais Registros e Nome Masculino com Mais Registros

![Nome Feminino e Masculino com Mais Registros](evidencias/masculino_feminino.png)

### Total de Registros (Masculinos e Femininos) - 10 Linhas

![Total de Registros](evidencias/masculinos_femininos_10_linhas.png)

### DataFrame com Valores de Nome em Maiúsculo no S3

![DataFrame no S3](evidencias/s3_json.png)

![DataFrame no S3 - Detalhes](evidencias/s3_json_detalhes.png)

### Crawler

![Crawler](evidencias/crawler.png)

### Athena

Consulta no Athena para mostrar que o banco criado pelo Crawler está funcionando:

![Consulta Athena](evidencias/consulta-athena.png)