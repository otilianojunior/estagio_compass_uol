## Sprint 9: Modelagem da Camada Refined

### Objetivo

Praticar a combinação de conhecimentos adquiridos ao longo do programa, integrando e aplicando diferentes técnicas e conceitos estudados.

## Desafio da Sprint

O desafio "Filmes e Séries" está dividido em cinco entregas. Nesta etapa, será realizada a quarta entrega, que consiste na modelagem de dados da camada Refined. Esta camada corresponde à fase do data lake onde os dados estão prontos para análise e extração de insights.
### ➡️ Primeira Etapa

Após a análise dos dados nas camadas raw e trusted, percebi que não seria possível concluir o desafio com as questões
inicialmente propostas. Foi necessário atualizar as perguntas do desafio para garantir a análise correta dos dados.

**Tema Central:**  
**"Análise de Remakes de Filmes Clássicos de Drama e Recomendações para Novas Produções: Considerações sobre Orçamento, Receita, Elenco e Avaliações"**

Remakes de filmes clássicos são uma tendência constante na indústria cinematográfica. 
O objetivo desta análise é identificar filmes clássicos de drama que possam ser bons candidatos para remakes, 
avaliando como fatores como orçamento, bilheteria, elenco e recepção crítica influenciam o sucesso tanto dos filmes originais quanto de suas reinterpretações modernas.

**Diferenças e Similaridades:**  
A análise permitirá explorar como a modernização e reinterpretação de histórias clássicas afetam o desempenho comercial
e crítico dos filmes. Investigar se os remakes mantêm, superam ou falham em replicar o sucesso dos originais pode fornecer insights 
valiosos sobre quais elementos são cruciais para o sucesso. Além disso, será analisado se certos filmes clássicos indicam potenciais para futuros remakes.

**Impacto do Elenco e Produção:**  
Remakes frequentemente apresentam elencos e equipes de produção diferentes. Analisar como essas mudanças influenciam o sucesso dos 
filmes ajudará a compreender o papel crucial do elenco e da produção na aceitação pelo público e no desempenho financeiro.

**Expectativas do Público e Crítica:**  
O interesse dos espectadores e da crítica em remakes pode diferir significativamente dos originais. 
Avaliar a recepção crítica e a popularidade dos remakes em comparação com os filmes originais pode oferecer insights sobre as expectativas e preferências do público.

**Estudo de Tendências e Impactos Culturais:**  
Remakes muitas vezes refletem mudanças culturais e tendências atuais. Analisar essas obras pode proporcionar uma compreensão mais profunda das dinâmicas culturais e 
de como elas influenciam o sucesso dos filmes.

**Lista de Filmes Clássicos Escolhida:**

Aqui está a separação dos filmes em "Com Remake" e "Proposta de Remake":

### Com Remake:
- **Ben-Hur**
- **Scarface** 
- **A Star is Born** 
- **True Grit** 
- **The Great Gatsby** 
- **The Postman Always Rings Twice** 
- **Cape Fear**
- **The Manchurian Candidate** 
- **12 Angry Men** 
- **Les Misérables** 
- **Doctor Zhivago** 

### Proposta de Remake:
- **O Poderoso Chefão** 
- **Um Sonho de Liberdade**
- **A Lista de Schindler**
- **Forrest Gump - O Contador de Histórias**
- **À Espera de um Milagre**
- **A Vida é Bela**
- **O Resgate do Soldado Ryan**
- **O Silêncio dos Inocentes**
- **Intocáveis** 
- **Sempre ao Seu Lado**
- **Interestelar**
- **Histórias Cruzadas**
- **À Procura da Felicidade**
- **Homens de Honra**
- **Coringa**
- **O Sexto Sentido**
- **Até o Último Homem**
- **A Noviça Rebelde**
- **Angry Men**
- **Inferno na Torre**


### ➡️ Segunda Etapa

Utilizei o script [ConsultaID.py](../sprint-9/evidencias/scripts/ConsultaID.py) para obter os IDs dos filmes na API TMDB, facilitando as etapas subsequentes.

Após obter os IDs, usei o código [UpdateRawTMDB.py](../sprint-9/evidencias/scripts/UpdateRawTMDB.py) para atualizar a camada raw de sprints anteriores,
sem precisar refazer todos os passos, mantendo todos os parâmetros exigidos.

Por fim, atualizei os códigos dos jobs da Sprint 8 para que a construção da camada trusted gerasse tabelas concisas com todos os dados, 
sem perder nenhuma informação gerada. Veja os códigos [job-csv.py](../sprint-8/desafio/job-csv.py) e [job-json.py](../sprint-8/desafio/job-json.py).

### ➡️ Terceira Etapa

**1. Refinamento dos Dados para a Camada Refined:**  
Nesta etapa, construímos um job para limpar os dados brutos e transformá-los em dados prontos para utilização no banco de dados.

- Job Layer Refined: [job_layer_refined.py](desafio/job_layer_refined.py) ✅

**2. Construção do Banco de Dados:**  
Criamos crawlers para carregar os dados da camada refined para um banco de dados `otiliano-desafio-database` no AWS Glue Catalog,
com tabelas dimensionadas para fatos e dimensões. Também realizamos uma consulta simples no Athena para verificar a execução.

- Crawlers: [Crawler](evidencias/fotos/crawlers.png) ✅
- Banco de Dados Dimensionado: [Tabelas CSV e JSON](evidencias/fotos/otiliano-desafio-database.png) ✅

### Evidências

- **Consultas e Arquivos Gerados:**  
O script gerado para a resolução do desafio, bem como seus arquivos gerados, estão na pasta [desafio](desafio). 
- Para mais informações, consulte o [README](desafio/README.md) do desafio.

- **Arquivos Adicionais:**  
As imagens relacionadas ao desafio estão organizadas na pasta [evidencias/fotos](evidencias/fotos) e os arquivos de script em [evidencias/scripts](evidencias/scripts).

### ➡️ Resolução de Exercícios

**Exercícios Resolvidos:**  
Nesta sprint, não houve exercícios.

### Certificados

**Certificados:**  
Nesta sprint, não houve cursos que geraram certificados.