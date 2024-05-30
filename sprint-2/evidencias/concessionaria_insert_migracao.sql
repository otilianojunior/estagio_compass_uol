
-- inserção na tabela combustivel
INSERT INTO concessionaria.tb_combustivel  (
    id_combustivel,
    tipo_combustivel 
)
SELECT DISTINCT 
	idcombustivel,
	tipoCombustivel
	
FROM
    migracao.tb_locacao;

-- inserção na tabela carro
INSERT INTO concessionaria.tb_carro  (
    id_carro ,
    marca_carro,
    modelo_carro,
    chassi_carro,
    ano_carro,
    fk_combustivel_id 
)
SELECT DISTINCT 
	idCarro,
	marcaCarro,
	modeloCarro,
	classiCarro,
	anoCarro,
	idCombustivel
	
FROM
    migracao.tb_locacao;
    
 -- insert cliente
 INSERT INTO concessionaria.tb_cliente  (
    id_cliente,
    nome_cliente,
    cidade_cliente,
    uf_cliente,
    pais_cliente 
)
SELECT DISTINCT 
    idCliente,
    nomeCliente,
    cidadeCliente,
    CASE estadoCliente
        WHEN 'Acre' THEN 'AC'
        WHEN 'Alagoas' THEN 'AL'
        WHEN 'Amapá' THEN 'AP'
        WHEN 'Amazonas' THEN 'AM'
        WHEN 'Bahia' THEN 'BA'
        WHEN 'Ceará' THEN 'CE'
        WHEN 'Distrito Federal' THEN 'DF'
        WHEN 'Espírito Santo' THEN 'ES'
        WHEN 'Goiás' THEN 'GO'
        WHEN 'Maranhão' THEN 'MA'
        WHEN 'Mato Grosso' THEN 'MT'
        WHEN 'Mato Grosso do Sul' THEN 'MS'
        WHEN 'Minas Gerais' THEN 'MG'
        WHEN 'Pará' THEN 'PA'
        WHEN 'Paraíba' THEN 'PB'
        WHEN 'Paraná' THEN 'PR'
        WHEN 'Pernambuco' THEN 'PE'
        WHEN 'Piauí' THEN 'PI'
        WHEN 'Rio de Janeiro' THEN 'RJ'
        WHEN 'Rio Grande do Norte' THEN 'RN'
        WHEN 'Rio Grande do Sul' THEN 'RS'
        WHEN 'Rondônia' THEN 'RO'
        WHEN 'Roraima' THEN 'RR'
        WHEN 'Santa Catarina' THEN 'SC'
        WHEN 'São Paulo' THEN 'SP'
        WHEN 'Sergipe' THEN 'SE'
        WHEN 'Tocantins' THEN 'TO'
        ELSE 'ER'
    END AS uf_cliente,
    paisCliente 
FROM
    migracao.tb_locacao;
    
-- INSERT VENDEDOR

INSERT INTO concessionaria.tb_vendedor  (
    id_vendedor,
    nome_vendedor,
    sexo_vendedor,
    uf_vendedor
)
SELECT DISTINCT 
    idVendedor,
    nomeVendedor,
    CASE sexoVendedor
    	WHEN '1' THEN 'F'
    	WHEN '0' THEN 'M'
    END AS sexo_vendedor,
    CASE estadoVendedor
        WHEN 'Acre' THEN 'AC'
        WHEN 'Alagoas' THEN 'AL'
        WHEN 'Amapá' THEN 'AP'
        WHEN 'Amazonas' THEN 'AM'
        WHEN 'Bahia' THEN 'BA'
        WHEN 'Ceará' THEN 'CE'
        WHEN 'Distrito Federal' THEN 'DF'
        WHEN 'Espírito Santo' THEN 'ES'
        WHEN 'Goiás' THEN 'GO'
        WHEN 'Maranhão' THEN 'MA'
        WHEN 'Mato Grosso' THEN 'MT'
        WHEN 'Mato Grosso do Sul' THEN 'MS'
        WHEN 'Minas Gerais' THEN 'MG'
        WHEN 'Pará' THEN 'PA'
        WHEN 'Paraíba' THEN 'PB'
        WHEN 'Paraná' THEN 'PR'
        WHEN 'Pernambuco' THEN 'PE'
        WHEN 'Piauí' THEN 'PI'
        WHEN 'Rio de Janeiro' THEN 'RJ'
        WHEN 'Rio Grande do Norte' THEN 'RN'
        WHEN 'Rio Grande do Sul' THEN 'RS'
        WHEN 'Rondônia' THEN 'RO'
        WHEN 'Roraima' THEN 'RR'
        WHEN 'Santa Catarina' THEN 'SC'
        WHEN 'São Paulo' THEN 'SP'
        WHEN 'Sergipe' THEN 'SE'
        WHEN 'Tocantins' THEN 'TO'
        ELSE 'ER'
    END AS uf_vendedor
FROM
    migracao.tb_locacao;
    

-- Insert locacao

INSERT INTO concessionaria.tb_locacao  (
	id_locacao,
	data_locacao,
	hora_locacao,
	qtd_diaria,
	valor_diaria,
	data_entrega,
	hora_entrega,
	km_carro_locacao,
	fk_cliente_id,
	fk_carro_id,
	fk_vendedor_id
)
SELECT
	idLocacao,
	STR_TO_DATE(REPLACE(dataLocacao, '.', ''), '%Y%m%d'),
	horaLocacao,
	qtdDiaria,
	vlrDiaria,
	STR_TO_DATE(REPLACE(dataEntrega, '.', ''), '%Y%m%d'),
	horaEntrega,
	kmCarro,
	idCliente,
	idCarro,
	idVendedor
	
FROM
    migracao.tb_locacao;

