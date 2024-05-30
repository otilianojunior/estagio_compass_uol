/*
pergunta:
Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).

Obs: Somente vendas concluídas.
*/


-- resposta
SELECT a.estado, a.nmpro, ROUND(AVG(a.qtd), 4) AS quantidade_media
FROM tbvendas AS a
WHERE a.status = 'Concluído'
GROUP BY a.estado, a.nmpro
ORDER BY a.estado, a.nmpro;
