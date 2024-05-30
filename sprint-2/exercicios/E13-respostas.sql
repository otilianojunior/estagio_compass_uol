/*
pergunta:
Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.
*/



-- resposta
SELECT a.cdpro, a.nmcanalvendas, a.nmpro, SUM(a.qtd) AS quantidade_vendas
FROM tbvendas AS a
WHERE a.status = 'Concluído'
AND (a.nmcanalvendas = 'Matriz' OR a.nmcanalvendas = 'Ecommerce')
GROUP BY a.cdpro, a.nmcanalvendas
ORDER BY quantidade_vendas ASC
LIMIT 10;

