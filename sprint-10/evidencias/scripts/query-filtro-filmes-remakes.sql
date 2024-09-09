SELECT "id_filme", "orcamento", "receita", "titulo", "titulo_original", "sinopse", "url_capa", "tempo_execucao",
       "generos", "idioma", "popularidade_filme", "data_lancamento", "ano", "mes", "dia", "voto_medio", "contagem_votos",
       "titulo_com_ano"
FROM (SELECT DISTINCT
    a.id_filme,
    b.orcamento,
    b.receita,
    c.titulo,
    c.titulo_original,
    c.sinopse,
    c.url_capa,
    d.tempo_execucao,
    e.generos,
    f.idioma,
    g.popularidade_filme,
    h.data_lancamento,
    h.ano,
    h.mes,
    h.dia,
    i.voto_medio,
    i.contagem_votos,
    CONCAT(c.titulo, ' - ', CAST(CAST(h.ano AS INT) AS VARCHAR)) AS titulo_com_ano  -- Concatena título com o ano após converter o ano para inteiro e depois para varchar
FROM "otiliano-desafio-database"."fato_filmes" AS a
JOIN "otiliano-desafio-database"."dim_custos_receita" AS b ON a.id_filme = b.id_filme
JOIN "otiliano-desafio-database"."dim_dados_adicionais" AS c ON a.id_filme = c.id_filme
JOIN "otiliano-desafio-database"."dim_duracao_metrica" AS d ON a.id_filme = d.id_filme
JOIN "otiliano-desafio-database"."dim_generos" AS e ON a.id_filme = e.id_filme
JOIN "otiliano-desafio-database"."dim_idioma" AS f ON a.id_filme = f.id_filme
JOIN "otiliano-desafio-database"."dim_popularidade" AS g ON a.id_filme = g.id_filme
JOIN "otiliano-desafio-database"."dim_tempo" AS h ON a.id_filme = h.id_filme
JOIN "otiliano-desafio-database"."dim_voto_medio" AS i ON a.id_filme = i.id_filme
WHERE a.origem = 'tmdb'
  AND a.id_filme IN (3111, 19610, 332562, 70881, 50512, 96724, 665, 271969, 11349, 1598, 4415, 82695, 877, 111, 982, 14462, 25736, 11027, 17529, 44264)) AS "desafio-filmes-remakes"