/*
pergunta:
Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.
*/


-- resposta
SELECT a.nome 
FROM autor AS a
LEFT JOIN livro AS b ON a.codautor = b.autor
GROUP BY a.codautor
HAVING COUNT(b.autor) = 0
ORDER BY a.nome ASC;
