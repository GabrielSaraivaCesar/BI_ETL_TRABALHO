use TRABALHO_BI;

CREATE TABLE dim_localizacao (
	id int unique not null,
	sigla char(2) not null,
	nome varchar(20) not null,
	regiao varchar(20) not null,
	PRIMARY KEY (id)
);

CREATE TABLE dim_tempo (
	id int unique not null,
	mes int not null,
	ano int not null,
	trimestre int not null,
	PRIMARY KEY (id)
);

CREATE TABLE dim_setor (
	id int unique not null,
	nome varchar(45) not null,
	PRIMARY KEY (id)
);

create table fato_consumo (
	id int unique not null,
	consumo float not null,
	num_consumidores float,
	fk_tempo int not null,
	fk_local int not null,
	fk_setor int not null,
    FOREIGN KEY (fk_tempo) REFERENCES dim_tempo(id),
    FOREIGN KEY (fk_local) REFERENCES dim_localizacao(id),
    FOREIGN KEY (fk_setor) REFERENCES dim_setor(id),
	PRIMARY KEY (id)
);


SELECT * FROM dim_localizacao;
SELECT * FROM dim_setor;
SELECT * FROM dim_tempo;
SELECT * FROM fato_consumo;