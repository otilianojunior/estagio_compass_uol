/*
pergunta:
Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.
*/



-- resposta
SELECT a.cdvdd, a.nmvdd
FROM tbvendedor AS a
JOIN tbvendas AS b ON a.cdvdd = b.cdvdd 
WHERE b.status = 'Concluído'
GROUP BY a.cdvdd, a.nmvdd
HAVING COUNT(b.cdvdd) = (
    SELECT MAX(vendas)
    FROM (
        SELECT COUNT(cdvdd) as vendas
        FROM tbvendas
        WHERE status = 'Concluído'
        GROUP BY cdvdd
    ) AS vendas_por_vendedor
);

