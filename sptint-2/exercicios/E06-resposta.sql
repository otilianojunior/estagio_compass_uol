/*
pergunta:
Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.
*/



-- resposta
SELECT a.codautor, a.nome, COUNT(b.autor) AS quantidade_publicacoes 
FROM autor AS a
JOIN livro AS b ON a.codautor = b.autor
GROUP BY a.codautor
ORDER BY quantidade_publicacoes DESC
LIMIT 1;
