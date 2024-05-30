-- create view fato_locacao

CREATE VIEW fato_locacao AS
SELECT  id_locacao AS id,
	fk_cliente_id AS id_cliente,
	fk_vendedor_id AS id_vendedor,
	fk_carro_id AS id_carro,
	data_locacao AS data_locacao,
	hora_locacao AS hora_locacao,
	data_entrega AS data_entrega,
	hora_entrega AS hora_entrega,
	valor_diaria AS valor_diaria,
	qtd_diaria AS qtd_diaria,
	km_carro_locacao AS km_carro_locacao
FROM tb_locacao;
-- -----------------------

-- create view dim_cliente

CREATE VIEW dim_cliente AS 
SELECT  id_cliente AS id,
	nome_cliente AS nome,
	cidade_cliente AS cidade,
	uf_cliente AS estado,
	pais_cliente AS pais
FROM tb_cliente;
-- -----------------------

-- create view dim_vendedor

CREATE VIEW dim_vendedor AS
SELECT  id_vendedor AS id,
	nome_vendedor AS vendedor,
	sexo_vendedor AS sexo,
	uf_vendedor AS estado
FROM tb_vendedor;
-- -----------------------

-- create view dim_carro

CREATE VIEW dim_carro AS
SELECT  a.id_carro AS id,
	a.marca_carro AS marca,
	a.modelo_carro AS modelo,
	a.chassi_carro AS numero_chassi,
	a.ano_carro AS ano,
	b.tipo_combustivel AS tipo_combustivel
	
FROM tb_carro AS a
JOIN tb_combustivel AS b ON a.fk_combustivel_id = b.id_combustivel;
-- -----------------------

-- create view dim_tempo

CREATE VIEW dim_tempo AS
SELECT DISTINCT 
    data_locacao AS data_locacao,
    YEAR(data_locacao) AS ano_locacao,
    MONTH(data_locacao) AS mes_locacao,
    DAY(data_locacao) AS dia_locacao,
    
    hora_locacao AS horario_locacao,
    HOUR(hora_locacao) AS hora_locacao,
    MINUTE(hora_locacao) AS min_locacao,
    
    data_entrega AS data_entrega,
    YEAR(data_entrega) AS ano_entrega,
    MONTH(data_entrega) AS mes_entrega,
    DAY(data_entrega) AS dia_entrega,
    
    hora_entrega AS horario_entrega,
    HOUR(hora_entrega) AS hora_entrega,
    MINUTE(hora_entrega) AS min_entrega
    
FROM tb_locacao;
-- -----------------------


