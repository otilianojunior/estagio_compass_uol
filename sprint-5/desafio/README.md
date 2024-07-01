### Desafio Etapa 1: Ambiente

Para este desafio, é necessário preparar o ambiente para usar o Python. Vamos começar criando o ambiente virtual (venv) para o nosso projeto.

1. Primeiro, instale as dependências do `python3-venv`:

   ```bash
   sudo apt install python3-venv
   ```

2. Em seguida, crie a venv no projeto:

   ```bash
   python3 -m venv venv
   ```

3. O próximo passo é ativar a venv:

   ```bash
   source venv/bin/activate
   ```

4. Após este passo, navegue no terminal até `sprint-5/desafio/etapa-1`. Nesta pasta, encontrará o arquivo [`requirements.txt`](../desafio/etapa-1/requirements.txt). Com ele, execute o seguinte comando para instalar as dependências e concluir a primeira etapa do desafio:

   ```bash
   pip install -r requirements.txt
   ```

### Desafio Etapa 1: Desenvolvimento

Depois de configurar o ambiente, basta abrir e executar o arquivo [`Consulta.py`](../desafio/etapa-1/Consulta.py), presente na pasta da etapa-1. Trata-se de um arquivo Python que utiliza a biblioteca `boto3` para acessar o bucket S3. Ao executá-lo, você concluirá as etapas restantes do desafio. Observe que existe um bloco de execução `if __name__ == '__main__':` no final do código, onde este executa a função `main`, indicando a ordem correta de execução do script.

* A base escolhida foi: `Os acidentes de trânsito da cidade de Belo Horizonte no Ano 2021, com vítima.`

### Tópicos do desafio:
Foi feita uma única consulta que engloba todos os tópicos abaixo. Aqui está cada parte do código descrita:

```sql
query = """
    SELECT COUNT(*) AS total_ocorrencias, 
    SUM(CASE WHEN descricao_categoria = 'PARTICULAR' THEN 1 ELSE 0 END) AS quantidade_particular, 
    SUM(CASE WHEN descricao_categoria = 'ALUGUEL' THEN 1 ELSE 0 END) AS quantidade_aluguel 
    FROM s3object 
    WHERE CAST(SUBSTRING(data_hora_boletim, 9, 2) AS INTEGER) = 21 
    AND descricao_especie = 'AUTOMOVEL' AND desc_situacao = 'EM MOVIMENTO' 
    AND (descricao_categoria = 'PARTICULAR' OR descricao_categoria = 'ALUGUEL');
"""
```

1. **Uma Cláusula que filtra dados usando ao menos dois operadores lógicos:**
    * Foram utilizados os operadores `AND` e `OR` para filtrar automóveis em movimento, do tipo aluguel ou particular.

2. **Duas funções de Agregação:**
    * Foram utilizadas as funções de agregação `COUNT` e `SUM` para contar o total de ocorrências e somar as ocorrências específicas.

3. **Uma função Condicional:**
    * A função condicional `CASE` foi usada para retornar valores diferentes com base em condições especificadas, neste caso 1 ou 0 para fazer a soma.

4. **Uma função de Conversão:**
    * A conversão `CAST` foi usada para converter o valor de string para inteiro.

5. **Uma função de Data:**
    * A consulta do `SELECT S3` é limitada, então vários métodos não funcionam nele. A data foi utilizada para trazer todas as ocorrências do dia 21.

6. **Uma função String:**
    * Foi utilizada a função `SUBSTRING` para formatar a data e fazer a consulta apenas na parte desejada, neste caso no campo do dia.

Ao executar o arquivo [`Consulta.py`](../desafio/etapa-1/Consulta.py), será gerado o arquivo [`query_results.csv`](../desafio/etapa-1/query_results.csv) no próprio diretório, contendo um arquivo CSV com o resultado da nossa consulta. O resultado também pode ser encontrado aqui: [`dados-consulta-csv.png`](../evidencias/dados-consulta-csv.png).

O arquivo [`.env.example`](../desafio/etapa-1/.env.example) é um demonstrativo de como foi configurado o arquivo `.env` com as chaves de acesso.

### Conclusão
Neste desafio, aprendemos a configurar um ambiente Python e a utilizar a biblioteca `boto3` para acessar e manipular dados armazenados na nuvem, especificamente em um bucket S3 da AWS. A nuvem oferece uma solução flexível e escalável para armazenar e acessar grandes volumes de dados, facilitando a integração e o processamento desses dados em tempo real.