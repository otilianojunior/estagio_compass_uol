Aqui está o markdown corrigido e melhorado:

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

4. Após este passo, navegue no terminal até `sprint-5/desafio/etapa-1`. Nesta pasta, encontrará o arquivo [`requirements.txt`](../desafio/etapa-1/requirements.txt). Com ele, execute o seguinte código para instalar as dependências e concluir a primeira etapa do desafio:

   ```bash
   pip install -r requirements.txt
   ```

### Desafio Etapa 1: Desenvolvimento

Depois de configurar o ambiente, basta abrir e executar o arquivo [`Consulta.py`](../desafio/etapa-1/Consulta.py), presente na pasta da etapa-1. Trata-se de um arquivo Python que utiliza a biblioteca `boto3` para acessar o bucket S3. Ao executá-lo, você concluirá as etapas restantes do desafio. Observe que existe um bloco de execução `if __name__ == '__main__':` no final do código, onde este executa a função `main`, indicando a ordem correta de execução do script.

* A base escolhida foi: `Os acidentes de trânsito da cidade de Belo Horizonte no Ano 2021`

Tópicos do desafio:

1. **Uma Cláusula que filtra dados usando ao menos dois operadores lógicos:**
   * 4.1. Filtra somente os automóveis que sofreram acidentes em movimento.

2. **Duas funções de Agregação:**
   * 4.2.1. Função de Agregação `count` para contar o número de acidentes.
   * 4.2.2. Função de Agregação `sum` para calcular a quantidade total de acidentes e a porcentagem de acidentes.

3. **Uma função Condicional:**
   * 4.3. Função Condicional para atribuir risco de acidentes.

4. **Uma função de Conversão:**
   * 4.4. Função de Conversão da porcentagem.

5. **Uma função de Data:**
   * 4.5. Função de Data que converte e altera o formato da data fornecida no arquivo.

6. **Uma função String:**
   * 4.6. Função String que remove espaços vazios.

Ao executar o arquivo [`Consulta.py`](../desafio/etapa-1/Consulta.py), será gerado o arquivo [`dados_acidentes.db`](../desafio/etapa-1/dados_acidentes.db)no próprio diretório,
contendo um banco de dados do SQLite com o nome `dados_acidentes`, e nele o resultado da nossa consulta. Que também pode ser encontrado aqui [`dados-consulta-sqlite.png`](../evidencias/dados-consulta-sqlite.png)

O arquivo [`.env.example`](../desafio/etapa-1/.env.example)é um demonstrativo de como foi configurado o arquivo `.env` com as chaves de acesso.

Conclusão:
Neste desafio, aprendemos a configurar um ambiente Python e a utilizar a biblioteca boto3 para acessar e manipular dados armazenados na nuvem, 
especificamente em um bucket S3 da AWS. A nuvem oferece uma solução flexível e escalável para armazenar e acessar grandes volumes de dados, 
facilitando a integração e o processamento desses dados em tempo real.




