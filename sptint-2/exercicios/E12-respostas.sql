/*
pergunta:
Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.

Observação: Apenas vendas com status concluído.

*/

-- resposta
SELECT c.cddep, c.nmdep, c.dtnasc, SUM(a.qtd * a.vrunt) AS valor_total_vendas
FROM tbvendas AS a
RIGHT JOIN tbvendedor AS b ON a.cdvdd = b.cdvdd
RIGHT JOIN tbdependente AS c ON b.cdvdd = c.cdvdd
WHERE a.status = 'Concluído'
GROUP BY c.cddep
HAVING SUM(a.qtd * a.vrunt) > 0
ORDER BY valor_total_vendas ASC
LIMIT 1;
