/*
pergunta:
Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).
*/




-- resposta
SELECT a.nome, a.codautor, a.nascimento, COUNT(b.autor) AS quantidade
FROM autor AS a
LEFT JOIN livro AS b ON a.codautor = b.autor
GROUP BY a.codautor
ORDER BY a.nome ASC;
