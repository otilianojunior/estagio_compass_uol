/* concessionaria_fisico: */

DROP DATABASE IF EXISTS concessionaria;
CREATE DATABASE concessionaria;

CREATE TABLE concessionaria.tb_vendedor (
    id_vendedor INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome_vendedor VARCHAR(100),
    sexo_vendedor CHAR(1),
    uf_vendedor CHAR(2)
);

CREATE TABLE concessionaria.tb_cliente (
    id_cliente INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome_cliente VARCHAR(100),
    cidade_cliente VARCHAR(40),
    uf_cliente CHAR(2),
    pais_cliente VARCHAR(40)
);

CREATE TABLE concessionaria.tb_combustivel (
    id_combustivel INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    tipo_combustivel VARCHAR(20)
);


CREATE TABLE concessionaria.tb_carro (
    id_carro INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    marca_carro VARCHAR(40),
    modelo_carro VARCHAR(40),
    chassi_carro VARCHAR(50),
    ano_carro VARCHAR(9),
    fk_combustivel_id INT,
    CONSTRAINT fk_combustivel FOREIGN KEY (fk_combustivel_id) REFERENCES tb_combustivel (id_combustivel)
);


CREATE TABLE concessionaria.tb_locacao (
    id_locacao INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    data_locacao DATE,
    hora_locacao TIME,
    qtd_diaria INT,
    valor_diaria DECIMAL(10,2),
    data_entrega DATE,
    hora_entrega TIME,
    km_carro_locacao DECIMAL(10,2),
    fk_cliente_id INT,
    fk_carro_id INT,
    fk_vendedor_id INT,
    CONSTRAINT fk_cliente FOREIGN KEY (fk_cliente_id) REFERENCES tb_cliente (id_cliente),
    CONSTRAINT fk_carro FOREIGN KEY (fk_carro_id) REFERENCES tb_carro (id_carro),
    CONSTRAINT fk_vendedor FOREIGN KEY (fk_vendedor_id) REFERENCES tb_vendedor (id_vendedor)
);

