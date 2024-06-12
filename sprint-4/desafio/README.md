### Desafio Etapa 1: Carguru

Para esta etapa, é necessário construir a imagem a partir de um arquivo de instruções Dockerfile, que execute o código `carguru.py`. Após isso, execute um container a partir da imagem criada.

1. Primeiro, navegue até o diretório `sprint-4/desafio/etapa-1`:

   ```bash
   cd sprint-4/desafio/etapa-1
   ```

2. Em seguida, crie a imagem do projeto:

   ```bash
   docker build -t desafio-sprint-etapa:1 .
   ```

3. Por fim, crie e execute o container:

   ```bash
   docker run --name desafio-sprint-container desafio-sprint-etapa:1
   ```

### Desafio Etapa 2: Markdown

Nos foi feito um questionamento sobre a possibilidade de reutilizar um container. A resposta pode ser encontrada aqui: [`README.md`](../desafio/etapa-2/README.md).

### Desafio Etapa 3: Converter Strings em Hash SHA-1

Para esta etapa, é necessário construir um script que transforma strings em hash SHA-1. Além disso, é necessário construir a imagem a partir de um arquivo de instruções Dockerfile e, por fim, executar um container a partir da imagem criada.

1. Primeiro, navegue até o diretório `sprint-4/desafio/etapa-3`:

   ```bash
   cd sprint-4/desafio/etapa-3
   ```

2. O script é o arquivo [`ConverteStringHash.py`](../desafio/etapa-3/ConverteStringHash.py).

3. Em seguida, crie a imagem do projeto:

   ```bash
   docker build -t mascarar-dados .
   ```

4. Por fim, crie e execute o container de forma interativa:

   ```bash
   docker run -it --name container-mascarar-dados mascarar-dados
   ```
   
### Desafio Evidencias:

1. Comando utilizado para visualizar as images, [`Imagem da execução`](../evidencias/docker-images.png).

   ```bash
   docker images.
   ```
2. Comando para reutilziar container de forma interativa, [`Imagem da execução`](../evidencias/docker-start-i-container-mascarar-dados.png).

   ```bash
   docker start -i container-mascarar-dados
   ```
3. Logs de execução do container interativo, [`Imagem da execução`](../evidencias/docker-logs-container-mascarar-dados.png).

   ```bash
   docker logs container-mascarar-dados
   ```

### Conclusão sobre Docker

Docker é uma ferramenta poderosa que permite criar, implantar e executar aplicações em containers. Containers são 
leves, portáteis e garantem que a aplicação tenha tudo o que precisa para ser executada, independente do ambiente em 
que se encontra, isso facilita o desenvolvimento.