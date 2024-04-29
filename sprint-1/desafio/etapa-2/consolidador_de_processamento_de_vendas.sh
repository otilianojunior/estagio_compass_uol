#!/bin/bash

# caminho para a pasta onde os relatórios estão
caminho_relatorios=~/Documentos/CompassUol/estagio_compass_uol/sprint-1/desafio/etapa-2/ecommerce/vendas/backup

# caminho para o arquivo relatorio_final.txt
relatorio_final=$caminho_relatorios/relatorio_final.txt

# verifica se há arquivos de relatório na pasta
if ls "$caminho_relatorios"/relatorio-*.txt 1> /dev/null 2>&1; then
    # Remove o arquivo relatorio_final.txt se ele existir para evitar a concatenação de relatórios antigos
    rm -f "$relatorio_final"
    
    # Loop pelos arquivos de relatório na pasta
    for relatorio in "$caminho_relatorios"/relatorio-*.txt; do
        # Adiciona o conteúdo de cada relatório ao arquivo relatorio_final.txt
        cat "$relatorio" >> "$relatorio_final"
    done
    
    echo "Relatórios concatenados com sucesso em $relatorio_final"
else
    echo "Nenhum arquivo de relatório encontrado na pasta $caminho_relatorios"
fi
