/*
pergunta:
Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.
*/



-- resposta
SELECT a.cdven
FROM tbvendas AS a
WHERE a.deletado = 1;
