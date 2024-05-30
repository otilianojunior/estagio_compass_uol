/*
pergunta:
Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.  Atenção às colunas esperadas no resultado final:  titulo, valor.
*/



-- resposta
SELECT a.titulo, a.valor 
FROM livro AS a
ORDER BY a.valor DESC
LIMIT 10;
