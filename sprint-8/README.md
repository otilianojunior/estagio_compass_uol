## Sprint 8: Apache Spark

### Objetivo

Praticar a combinação de conhecimentos adquiridos no PB, aprofundando o conhecimento no Apache Spark.

## Desafio da Sprint

O desafio de filmes e séries está dividido em 5 entregas. Nesta sprint, realizaremos a Entrega 3, que envolve a construção da camada TRUSTED e do Data Catalog.

### ➡️ Primeira Etapa

**1. Limpeza de Dados para a Camada Trusted:** Nesta etapa, construímos os jobs para limpar os dados brutos.

* Job CSV: [job-csv.py](desafio/job-csv.py) ✅
* Job JSON: [job-json.py](desafio/job-json.py) ✅

### ➡️ Segunda Etapa

**2. Construção do Banco de Dados Acessível pelo Athena:** Nesta etapa, criamos crawlers para carregar os dados da camada Trusted para um banco de dados `otiliano-desafio-database` no AWS Glue Catalog, com tabelas para CSV e JSON. Também realizamos uma consulta simples no Athena para verificar a execução.

* Crawler CSV e JSON: [Crawler CSV e JSON](evidencias/crawlers.png) ✅
* Tabelas CSV e JSON: [Tabelas CSV e JSON](evidencias/glue-catalog.png) ✅
* Consulta Athena CSV: [Consulta Athena CSV](evidencias/athena-csv.png) ✅
* Consulta Athena JSON: [Consulta Athena JSON](evidencias/athena-json.png) ✅

### Evidências

* **Consultas e Arquivos Gerados:** O script gerado para a resolução do desafio, bem como seus arquivos gerados, estão na pasta [desafio](desafio). Para mais informações, consulte o [README](desafio/README.md) do desafio.

* **Arquivos Adicionais:** As imagens relacionadas ao desafio estão organizadas na pasta [evidencias](evidencias).

### ➡️ Resolução de Exercícios

**3. Exercícios Resolvidos:** Cada pasta de resolução possui seu próprio README com a explicação de como foi feito.

* [Geração de Dados](exercicios/geracao-dados) ✅
* [Apache Spark](exercicios/apache-spark) ✅
* [Exercício TMDB](exercicios/exercicio_tmdb) ✅

### Certificados 🎓

* [Curso AWS - Tutoriais Técnicos - Analytics ](certificados/cursos-sprint-8.png) ✅