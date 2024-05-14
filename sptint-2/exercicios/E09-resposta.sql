/*
pergunta
Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.
*/




-- resposta
SELECT a.cdpro, a.nmpro 
FROM tbvendas AS a
WHERE a.status = 'Concluído' AND a.dtven BETWEEN '2014-02-03' AND '2018-02-02'
GROUP BY a.cdpro
ORDER BY COUNT(*) DESC
LIMIT 1;
