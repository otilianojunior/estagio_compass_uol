# criamos a pasta vendas dentro do diretório ecommerce
mkdir -p  ecommerce/vendas

# copiamos o arquivo dados para o diretorio vendas
cp ecommerce/dados_de_vendas.csv ecommerce/vendas

# criamos o subdiretorio backup dentro do diretório vendas
mkdir -p  ecommerce/vendas/backup

# Obtemos a data no formato YYYYMMDD
data=$(date +%Y%m%d)

# contruimos o nome do aruqivo
dados_por_dia="dados-${data}.csv"

# copiamos o arquivo dados para o diretorio vendas
cp ecommerce/vendas/dados_de_vendas.csv ecommerce/vendas/backup/$dados_por_dia

# construindo o nome do arquivo na pasta backup
backup_dados="backup-${dados_por_dia}"

# renomeando o arquivo de dados
mv ecommerce/vendas/backup/$dados_por_dia ecommerce/vendas/backup/$backup_dados

# criando nome do relatório
relatorio_diario="relatorio-${data}.txt"

# criando um txt  de relatorio
touch ecommerce/vendas/backup/$relatorio_diario

# customizando o relatório
estilo_inicio_fim="* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
estilo="-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -  "
# style
echo "$estilo_inicio_fim" >> ecommerce/vendas/backup/$relatorio_diario

# formatando a data e hora do sistema
data_2=$(date +"%Y/%m/%d %H:%M")
#inserindo data e hora no relatorio
echo "Data e hora da execução: $data_2" >> ecommerce/vendas/backup/$relatorio_diario
# style
echo "$estilo" >> ecommerce/vendas/backup/$relatorio_diario

# pegamos a data do primeiro registro
data_primeiro_registro=$(head -n 2 ecommerce/vendas/backup/$backup_dados | tail -n 1 | cut -d ',' -f 5 )
# inserindo a data do primeiro produto inserido
echo "Data do primeiro registro de venda: $data_primeiro_registro" >> ecommerce/vendas/backup/$relatorio_diario
# style
echo "$estilo" >> ecommerce/vendas/backup/$relatorio_diario


# pegamos a data do ultimo registro
data_ultimo_registro=$(tail -n 1 ecommerce/vendas/backup/$backup_dados | cut -d ',' -f 5)
# inserindo a data do ultimo produto inserido
echo "Data do ultimo registro de venda: $data_ultimo_registro" >> ecommerce/vendas/backup/$relatorio_diario
# style
echo "$estilo" >> ecommerce/vendas/backup/$relatorio_diario


# inserindo quantidade de itens unicos vendidos
echo "Quantidade de itens únicos vendidos: $(cut -d ',' -f 2 ecommerce/vendas/backup/$backup_dados | uniq -c | wc -l)" >> ecommerce/vendas/backup/$relatorio_diario
# style
echo "$estilo" >> ecommerce/vendas/backup/$relatorio_diario

# pegando os primeiros 10 registros
dez_primeiras=$(tail -n +2 ecommerce/vendas/backup/$backup_dados | head -n 10)
# inserindo texto dos 10 primeiras registros
echo "Esses são os primeiros 10 registros:" >> ecommerce/vendas/backup/$relatorio_diario
# style
echo "$estilo" >> ecommerce/vendas/backup/$relatorio_diario
#inserindo as 10 primeiras linhas no relatorio
echo "$dez_primeiras" >> ecommerce/vendas/backup/$relatorio_diario
# style
echo "$estilo_inicio_fim" >> ecommerce/vendas/backup/$relatorio_diario


# indo ao diretório backup
cd ecommerce/vendas/backup/

# removendo csv do nome do arquivo
dados_zip=$(basename "$backup_dados" .csv)

# compactando o arquivo
zip "${dados_zip}.zip" "$backup_dados"

# removendo arquivo
rm $backup_dados

# indo ao diretório vendas
cd ../
# removendo o arquivo
rm dados_de_vendas.csv
