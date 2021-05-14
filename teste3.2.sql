CREATE TABLE IF NOT EXISTS Relação_Operadoras_Ativas_ANS(
    id int AUTO_INCREMENT,
    registro_ans int(10),
    cnpj int(16),
    razao_social varchar(100),
    nome_fantasia varchar(70),
    modalidade varchar(30),
    logradouro varchar(60),
    número int(7),
    complemento varchar(50),
    bairro varchar(50),
    cidade	varchar(30),
    uf char(2),
    cep int(10),
    ddd int(2),
    telefone int(9),
    fax	int(8),
    endereço_eletrônico	varchar(40),
    representante varchar(50),
    cargo_representante varchar(40),
    data_registro_ans date,
    PRIMARY KEY (id)
);

SELECT DATE_FORMAT(data_registro_ans, "%d/%m/%Y") FROM Relação_Operadoras_Ativas_ANS;
