/* 
pergunta:
Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.
*/


-- resposta
SELECT DISTINCT a.nome
FROM autor AS a
JOIN livro AS b ON a.codautor = b.autor 
JOIN editora AS c ON b.editora = c.codeditora 
JOIN endereco AS d ON c.endereco = d.codendereco 
WHERE d.estado NOT IN ('PARANÁ', 'SANTA CATARINA', 'RIO GRANDE DO SUL')
ORDER BY a.nome ASC;
