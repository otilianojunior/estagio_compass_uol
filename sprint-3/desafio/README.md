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

4. Após este passo, navegue no terminal até `sprint-3/desafio/etapa-1` [etapa-1](./desafio/etapa-1). Nesta pasta, encontrará o arquivo [`requirements.txt`](./desafio/etapa-1/requirements.txt). Com ele, execute o seguinte código para instalar as dependências e concluir a primeira etapa do desafio:

   ```bash
   pip install -r requirements.txt
   ```

### Desafio Etapa 2: Desenvolvimento

Depois de configurar o ambiente, basta abrir e executar o arquivo `DesafioEtl.ipynb`. Trata-se de um arquivo no formato do Jupyter Notebook. Ao executá-lo, você concluirá as etapas restantes do desafio. Observe que existe um bloco de execução `if __name__ == '__main__':` no final do código, onde está indicada a ordem correta de execução para que o script funcione.

Tópicos do desafio e suas respectivas funções:
1. Remoção das linhas duplicadas: `remover_duplicatas()`
2. Gerar gráfico de colunas: `grafico_coluna_top_5_instalacoes()`. Além disso, o gráfico pode ser encontrado aqui: [grafico_barras.png](evidencias/grafico_barras.png)
3. Gerar gráfico de pizza: `grafico_pizza_frequencia_categorias()`. Além disso, o gráfico pode ser encontrado aqui: [grafico_pizza.png](evidencias/grafico_pizza.png)
4. Qual app é mais caro: `app_mais_caro()`. Além disso, a resposta pode ser encontrada aqui: [app_mais_caro.txt](desafio/etapa-2/app_mais_caro.txt)
5. Quantos apps têm classificação Mature 17+: `numero_apps_mature_17()`. Além disso, a resposta pode ser encontrada aqui: [app_mature_17.txt](desafio/etapa-2/app_mature_17.txt)
6. Top 10 apps por número de reviews: `top_10_aplicativos_reviews()`. Além disso, a resposta pode ser encontrada aqui: [top_10_reviews.txt](desafio/etapa-2/top_10_reviews.txt)
7. Crie mais 2 cálculos sobre o dataset:
    - `top_10_apps_avaliados()`. Além disso, a resposta pode ser encontrada aqui: [top_10_avaliados.txt](desafio/etapa-2/top_10_avaliados.txt)
    - `quantidade_apps_pagos()`. Além disso, a resposta pode ser encontrada aqui: [app_pagos.txt](desafio/etapa-2/app_pagos.txt)
8. Crie mais 2 formas gráficas:
    - `grafico_dispersao_app_updates()`. Além disso, o gráfico pode ser encontrado aqui: [grafico_dispersao.png](evidencias/grafico_dispersao.png)
    - `grafico_linha_genero_instalacoes()`. Além disso, o gráfico pode ser encontrado aqui: [grafico_linha.png](evidencias/grafico_linha.png)



Conclusão:

Python é uma linguagem de programação versátil e poderosa com uma ampla quantidade de bibliotecas e frameworks disponíveis. 
Quando se trata de ETL, o Python oferece várias bibliotecas robustas e eficientes, como Pandas, NumPy e SQLAlchemy, que simplificam o processo de manipulação de dados.

Ao utilizar Python para ETL, é possível extrair dados de diversas fontes, como bancos de dados, arquivos CSV e APIs da web, e depois transformá-los de acordo com os requisitos específicos do projeto. 
Essas transformações podem incluir limpeza de dados, agregação, filtragem e muito mais. Uma vez que os dados estejam preparados, podem ser carregados em diferentes destinos, como bancos de dados relacionais, data lakes ou data warehouses.
