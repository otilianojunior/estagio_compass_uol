-- Consulta simulando o banco antes de ser relacional

SELECT
    a.id_locacao,
    c.id_cliente,
    c.nome_cliente,
    c.cidade_cliente,
    c.uf_cliente,
    c.pais_cliente,
    b.id_carro,
    a.km_carro_locacao,
    b.chassi_carro,
    b.marca_carro,
    b.modelo_carro,
    b.ano_carro,
    b.fk_combustivel_id,
    e.tipo_combustivel,
    a.data_locacao,
    a.hora_locacao,
    a.qtd_diaria,
    a.valor_diaria,
    a.data_entrega,
    a.hora_entrega,
    d.id_vendedor,
    d.nome_vendedor,
    d.sexo_vendedor,
    d.uf_vendedor
    
FROM concessionaria.tb_locacao AS a
    JOIN tb_carro AS b ON a.fk_carro_id = b.id_carro 
    JOIN tb_cliente AS c ON a.fk_cliente_id = c.id_cliente
    JOIN tb_vendedor AS d ON a.fk_vendedor_id = d.id_vendedor
    JOIN tb_combustivel AS e ON b.fk_combustivel_id = e.id_combustivel
    ORDER BY a.id_locacao ASC;    
