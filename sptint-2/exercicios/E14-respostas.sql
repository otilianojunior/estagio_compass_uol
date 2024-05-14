/*
pergunta:
Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.

Observação: Apenas vendas com status concluído.
*/

-- respostas
SELECT a.estado, ROUND(AVG(a.qtd*a.vrunt), 2) AS gastomedio
FROM tbvendas AS a
WHERE a.status = 'Concluído'
GROUP BY a.estado
ORDER BY gastomedio DESC;

