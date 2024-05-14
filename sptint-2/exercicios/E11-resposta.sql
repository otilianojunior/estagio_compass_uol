/*
pergunta:
Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.
*/



-- resposta
SELECT a.cdcli, a.nmcli, SUM(a.vrunt*a.qtd) AS gasto
FROM tbvendas AS a
WHERE a.status = 'Concluído'
GROUP BY a.cdcli
ORDER BY gasto DESC
LIMIT 1;
