## Desafio Etapa 2:

**Introdução:**

Este README atualizado fornece instruções mais detalhadas e organizadas para concluir o desafio da Etapa 2. O objetivo é garantir que todos os aqueles que tenham clonado o repositório completo, possam executar o desafio com sucesso.

**Pré-requisitos:**

* Ter o sistema operacional instalado e configurado com as ferramentas básicas de linha de comando.
* Ter o repositório clonado em seu ambiente local.
* Ter permissão de usuário para executar códigos de permissão em sua máquina.
* Ter a biblioteca zip instalada em sua maquina, caso não tenha copie o código a baixo e o execute no seu terminal.

```
sudo apt install zip

```

**Etapas:**

1. **Navegue para o Diretório de Trabalho:**

   Abra um terminal ou prompt de comando e navegue para o diretório `etapa-2` do repositório clonado.


2. **Execute o Script de Processamento:**

   Para iniciar o processo de tratamento dos dados de vendas, execute o seguinte comando:

   ```bash
   ./processamento_de_vendas.sh
   ```
   Note que posssa ser que o arquivo vá pedir permissão de execução, para isso utilize o código a baixo:

    ```
    sudo chmod +x processamento_de_vendas.sh
    ```

   Este script irá ler os arquivos `dados_de_vendas.csv` presentes no diretório `etapa-2/ecommerce` e processá-los de acordo com as regras do desafio.

3. **Execute o Script de Consolidação:**

   Após a conclusão do script de processamento, execute o script de consolidação para gerar os arquivos finais:

   ```bash
   ./consolidador_de_processamento_de_vendas.sh
   ```

      Note que posssa ser que o arquivo vá pedir permissão de execução, para isso utilize o código a baixo:

    ```
    sudo chmod +x consolidador_de_processamento_de_vendas.sh
    ```

   Este script irá consolidar os dados processados e gerar o arquivos `relatorio_final.txt` dentro da pasta ecommerce/vendas/backup.

**Observações:**

* Os arquivos `backup-dados-yyyymmdd.zip` e `relatorio-yyyymmdd.txt` serão gerados com base na data atual do sistema operacional.
* Se você não possui os arquivos `dados_de_vendas_2.csv` e `dados_de_vendas_3.csv` no diretório `etapa-2/ecommerce`, você pode obtê-los nos seguintes links:
    * `dados_de_vendas_2.csv`: [dados_de_vendas_2.csv](/sprint-1/evidencias/dados_de_vendas_2.csv)
    * `dados_de_vendas_3.csv`: [dados_de_vendas_3.csv](/sprint-1/evidencias/dados_de_vendas_3.csv)
* Você pode alterar o arquivo de dados_de_vendas.csv na pasta ecommerce com os valores obtidos no `dados_de_vendas_2.csv` e `dados_de_vendas_3.csv` assim irá obter os valores mostrados no relatorio_final.txt.

**Dicas:**

* Certifique-se de ter permissões de execução para os scripts `processamento_de_vendas.sh` e `consolidador_de_processamento_de_vendas.sh`.
* Se você encontrar algum erro durante a execução dos scripts, revise o código e verifique se os arquivos de entrada estão no diretório correto.

**Conclusão:**

Ao seguir estas instruções cuidadosamente, você deverá conseguir concluir o desafio da mesma forma que eu.


