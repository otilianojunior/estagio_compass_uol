/*
pergunta:
 Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.
*/




-- resposta
SELECT COUNT(b.editora) AS quantidade, a.nome, c.estado, c.cidade  
FROM editora AS a
JOIN livro AS b ON a.codeditora = b.editora
JOIN endereco AS c ON a.endereco = c.codendereco 
GROUP BY b.editora
ORDER BY quantidade DESC 
LIMIT 5;
