
CREATE TABLE [arma]
(
	[id] int NOT NULL, 
	[Tipo] nvarchar(50) NULL,
	[Custo] int  NULL,
	[Arma] nvarchar(50) NULL,
	[Alcance] nvarchar(50) NULL,
	[Forca_Min] int  NULL,
	[Bônus] nvarchar(50) NULL,
	[L] int  NULL,
	[M] int  NULL,
	[P] int  NULL,
	[25] int  NULL,
	[50] int  NULL,
	[75] int  NULL,
	[100] int  NULL,
	[Pq] nvarchar(50) NULL,
	[An] nvarchar(50) NULL,
	[El] nvarchar(50) NULL,
	[ME] nvarchar(50) NULL,
	[Hu] nvarchar(50) NULL,
	CONSTRAINT [PK_Arma] PRIMARY KEY([id])
);
 
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(1,'CD',	1,			'Combate Desarmado'			,'-', 		-2,			'AGI',	3,	-1,		-4,			1,		2,		3,		4,		'1m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(2,'CD',	1,			'Manopla'					,'-', 		-1,			'AGI',	2,	0,		-4,			2,		4,		6,		8,		'1m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(3,'CI',	1,			'Boleadeira'				,'20m',		-1,			'AGI',	-1,	1,		3,			0,		0,		0,		0,		'2m',	'2m',	'2m',	'2m',		'2m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(4,'CI',	1,			'Rede'						,'5m',		-1,			'AGI',	0,	2,		3,			0,		0,		0,		0,		'1m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(5,'CL',	1,			'Faca'						,'-',		-2,			'AGI',	3,	-2,		-3,			1,		2,		3,		4,		'1m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(6,'CL',	1,			'Punhal'					,'20m',		-2,			'AGI',	3,	-2,		-3,			2,		4,		6,		8,		'1m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(7,'CLD',	1,			'Bumerangue'				,'40m',		-1,			'PER',	2,	0,		-4,			1,		2,		3,		4,		'1m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(8,'CLD',	1,			'Bumerangue de Corte'		,'-',		-1,			'PER',	2,	0,		-4,			2,		4,		6,		8,		'1m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(9,'CLD',	1,			'Funda Projétil de Pedra'	,'60m',		-1,			'PER',	2,	-1,		-3,			1,		2,		3,		4,		'1m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(10,'CLD',	1,		'Funda Projétil de Metal'	,'-',		-1,			'PER',	2,	-1,		-3,			2,		4,		6,		8,		'1m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(11,'EL',	1,			'Malho'						,'-',		-1,			'AGI',	1,	0,		-3,			1,		2,		3,		4,		'1m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(12,'EL',	1,			'Cajado'					,'-',		-1,			'AGI',	2,	-1,		-3,			2,		4,		6,		8,		'2m',	'2m',	'2m',	'2m',		'2m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(13,'EL',	1,			'Porrete'					,'-',		-1,			'AGI',	1,	0,		-3,			2,		4,		6,		8,		'1m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(14,'CmE',	2,		'Gládio'					,'-',		0,			'AGI',	2,	1,		-3,			3,		6,		9,		12,		'1m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(15,'CmE',	2,		'Rapieira'					,'-',		0,			'AGI',	4,	0,		-4,			3,		6,		9,		12,		'1m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(16,'CmE',	2,		'Cimitarra'					,'-',		1,			'AGI',	2,	1,		-3,			4,		8,		12,		16,		'2m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(17,'CmE',	2,		'Espada'					,'-',		1,			'AGI',	3,	0,		-3,			4,		8,		12,		16,		'2m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(18,'CmE',	2,		'Sabre Élfico'				,'-',		1,			'AGI',	3,	0,		-3,			4,		8,		12,		16,		'2m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(19,'CmM',	2,		'Machado'					,'-',		0,			'AGI',	0,	3,		-3,			3,		6,		9,		12,		'1m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(20,'CmM',	2,		'Machadinha'				,'25m',		0,			'AGI',	1,	2,		-3,			3,		6,		9,		12,		'1m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(21,'CmM',	2,		'Machado Crescente'			,'-',		1,			'AGI',	0,	3,		-3,			4,		8,		12,		16,		'2m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(22,'CmM',	2,		'Machado de Batalha'		,'-',		1,			'AGI',	1,	2,		-3,			4,		8,		12,		16,		'2m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(23,'EM',	2,			'Clava'						,'-',		0,			'AGI',	1,	1,		-2,			3,		6,		9,		12,		'2m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(24,'EM', 	2,		'Maça'						,'-',		0,			'AGI',	-1,	1,		0,			3,		6,		9,		12,		'2m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(25,'EM',	2,			'Martelo de Guerra'			,'25m',		0,			'AGI',	0,	1,		-1,			3,		6,		9,		12,		'1m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(26,'EM',	2,			'Maça de Armas'				,'-',		1,			'AGI',	-2,	1,		1,			4,		8,		12,		16,		'2m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(27,'EM',	2,			'Mangual Leve'				,'-',		1,			'AGI',	-1,	1,		0,			4,		8,		12,		16,		'2m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(28,'PmA',	2,		'Arco Simples'				,'120',		0,			'PER',	3,	1,		-4,			3,		6,		9,		12,		'2m',	'2m',	'2m',	'2m',		'2m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(29,'PmA',	2,		'Arco Composto'				,'200',		0,			'PER',	3,	1,		-4,			4,		8,		12,		16,		'X',	'2m',	'2m',	'2m',		'2m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(30,'PmL',	2,		'Lança Leve'				,'40m',		0,			'AGI',	3,	-1,		-2,			3,		6,		9,		12,		'2m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(31,'PmL',	2,		'Arpão'						,'30m',		0,			'AGI',	2,	1,		-3,			3,		6,		9,		12,		'1m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(32,'PmL',	2,		'Lança de Guarda'			,'-',		1,			'AGI',	2,	0,		-2,			4,		8,		12,		16,		'2m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(33,'PmL',	2,		'Lança Pesada'				,'-',		1,			'AGI',	-1,	2,		-1,			4,		8,		12,		16,		'2m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(34,'PmL',	2,		'Tridente'					,'30m',		1,			'AGI',	2,	-1,		-1,			4,		8,		12,		16,		'2m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(35,'CpE',	3,		'Espada de Mão e Meia'		,'-',		-1,			'FOR',	3,	0,		-2,			5,		10,		15,		20,		'X'	,	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(36,'CpE',	3,		'Espada (Com Duas Mãos)'	,'-',		0,			'FOR',	-2,	1,		3,			0,		0,		0,		0,		'2m',	'2m',	'2m',	'2m', 		''	);
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(37,'CpE',	3,		'Montante'					,'-',		2,			'FOR',	-2,	2,		3,			6,		12,		18,		24,		'X',	'X',	'X'	,	'2m',		'2m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(38,'CpM',	3,		'Machado de Guerra'			,'-',		1,			'FOR',	0,	3,		-2,			5,		10,		15,		20,		'X',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(39,'CpM',	3,		'Machado (Com Duas Mãos)'	,'-',		0,			'FOR',	-2,	3,		1,			0,		0,		0,		0,		'2m',	'2m',	'2m',	'2m',		''	);
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(40,'CpM',	3,		'Axa de Armas'				,'-',		2,			'FOR',	-2,	3,		2,			6,		12,		18,		24,		'X',	'X',	'X'	,	'2m',		'2m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(41,'EP',	3,			'Mangual'					,'-',		1,			'FOR',	-1,	1,		1,			5,		10,		15,		20,		'X',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(42,'EP',	3,			'(Com Duas Mãos)'			,'-',		0,			'FOR',	-2,	1,		3,			0,		0,		0,		0,		'2m',	'2m',	'2m',	'2m',		''	);
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(43,'EP',	3,			'Marreta de Guerra'			,'-',		2,			'FOR',	-3,	2,		4,			6,		12,		18,		24,		'X',	'X',	'X'	,	'2m',		'2m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(44,'PP',	3,			'Lança de Justa'			,'-',		1,			'FOR',	1,	1,		2,			5,		10,		15,		20,		'X',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(45,'PP',	3,			'Lança de Cavalaria'		,'-',		2,			'FOR',	0,	2,		3,			6,		12,		18,		24,		'X',	'X',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(46,'PpA',	3,		'Arco de Guerra'			,'160',		1,			'PER',	0,	1,		2,			5,		10,		15,		20,		'2m',	'2m',	'2m',	'2m',		'2m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(47,'PpA',	3,		'Arco Longo Élfico'			,'300',		2,			'PER',	-2,	2,		3,			6,		12,		18,		24,		'X',	'X',	'2m',	'2m',		'2m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(48,'PpB',	3,		'Besta'						,'80m',		1,			'PER',	0,	1,		2,			5,		10,		15,		20,		'2m',	'1m',	'1m',	'1m',		'1m');
INSERT INTO [ARMA] ([id],[Tipo],[Custo],[Arma],[Alcance],[Forca_Min],[Bônus],[L],[M],[P],[25],[50],[75],[100],[Pq],[An],[El],[ME],[Hu]) VALUES(49,'PpB',	3,		'Besta Pesada'				,'140',		2,			'PER',	-1,	1,		3,			6,		12,		18,		24,		'2m',	'2m',	'2m',	'2m',		'2m');


CREATE TABLE [defesa]
(
	[id] int NOT NULL, 
	[nome] nvarchar(50) NULL,
	[defesa_base] nvarchar(3)  NULL,
	[Absorcao] int NULL,
	[fisico_minimo] int NULL,
	[forca_minima] int  NULL,
	[P] int  NULL,
	[A] int  NULL,
	[E] int  NULL,
	[M] int  NULL,
	[H] int  NULL,
	CONSTRAINT [PK_defesa] PRIMARY KEY([id])
);

INSERT INTO [defesa] ([id],[nome],[defesa_base],[Absorcao],[fisico_minimo],[forca_minima],[P],[A],[E],[M],[H]) VALUES(1,'Nada'					,'L0',0,0,0,0,0,0,0,0);
INSERT INTO [defesa] ([id],[nome],[defesa_base],[Absorcao],[fisico_minimo],[forca_minima],[P],[A],[E],[M],[H]) VALUES(2,'Couro Leve'			,'L1',8,-2,0,0,0,0,0,0);
INSERT INTO [defesa] ([id],[nome],[defesa_base],[Absorcao],[fisico_minimo],[forca_minima],[P],[A],[E],[M],[H]) VALUES(3,'Couro Rígido'			,'L2',12,-1,0,0,0,0,0,0);
INSERT INTO [defesa] ([id],[nome],[defesa_base],[Absorcao],[fisico_minimo],[forca_minima],[P],[A],[E],[M],[H]) VALUES(4,'Cota de Malha Parcial'	,'M1',18,0,0,0,0,0,0,0);
INSERT INTO [defesa] ([id],[nome],[defesa_base],[Absorcao],[fisico_minimo],[forca_minima],[P],[A],[E],[M],[H]) VALUES(5,'Cota de Malha Completa','M2',22,0,0,0,0,0,0,0);
INSERT INTO [defesa] ([id],[nome],[defesa_base],[Absorcao],[fisico_minimo],[forca_minima],[P],[A],[E],[M],[H]) VALUES(6,'Couraça Parcial'		,'P1',28,1,0,0,0,0,0,0);
INSERT INTO [defesa] ([id],[nome],[defesa_base],[Absorcao],[fisico_minimo],[forca_minima],[P],[A],[E],[M],[H]) VALUES(7,'Couraça Completa'		,'P2',32,1,0,0,0,0,0,0);
INSERT INTO [defesa] ([id],[nome],[defesa_base],[Absorcao],[fisico_minimo],[forca_minima],[P],[A],[E],[M],[H]) VALUES(8,'Escudo Pequeno'		,'+1',4,0,-1,1,1,1,1,1);
INSERT INTO [defesa] ([id],[nome],[defesa_base],[Absorcao],[fisico_minimo],[forca_minima],[P],[A],[E],[M],[H]) VALUES(9,'Escudo Grande'			,'+1',8,0,0,2,1,1,1,1);
INSERT INTO [defesa] ([id],[nome],[defesa_base],[Absorcao],[fisico_minimo],[forca_minima],[P],[A],[E],[M],[H]) VALUES(10,'Escudo Torre'			,'+2',12,0,1,0,1,1,1,1);
INSERT INTO [defesa] ([id],[nome],[defesa_base],[Absorcao],[fisico_minimo],[forca_minima],[P],[A],[E],[M],[H]) VALUES(11,'Elmo Aberto'			,'--',2,0,0,0,0,0,0,0);
INSERT INTO [defesa] ([id],[nome],[defesa_base],[Absorcao],[fisico_minimo],[forca_minima],[P],[A],[E],[M],[H]) VALUES(12,'Elmo Fechado'			,'--',4,0,0,0,0,0,0,0);





CREATE TABLE [categoria](
  [id] int NOT NULL, 
  [nome] nvarchar(60) NULL, 
  [icon] nvarchar(50) NULL, 
  CONSTRAINT [PK_categoria] PRIMARY KEY([id]));

CREATE TABLE [combate](
  [id] int NOT NULL, 
  [id_habilidade_grupo] int NULL, 
  [id_categoria] int NULL, 
  [nome] nvarchar(50) NULL, 
  [atributo] nvarchar(3) NULL, 
  [efeito] ntext NULL, 
  [requisitos] ntext NULL, 
  [obs] ntext NULL, 
  [quadro_rolagem] ntext NULL, 
  [aprimoramento] ntext NULL, 
  [bonus] int NULL, 
  [possui_especializacao] int NULL, 
  CONSTRAINT [PK_combate] PRIMARY KEY([id]));

CREATE TABLE [combate_grupo](
  [id] int NOT NULL, 
  [id_pai] int NULL, 
  [nome] nvarchar(100) NULL, 
  CONSTRAINT [PK_combate_grupo] PRIMARY KEY([id]));

CREATE TABLE [combate_grupo_custo](
  [id_combate] int NOT NULL, 
  [id_combate_grupo] int NOT NULL, 
  [custo] int NULL, 
  CONSTRAINT [PK_combate_grupo_custo] PRIMARY KEY([id_combate], [id_combate_grupo]));

CREATE TABLE [divindade](
  [id] int NOT NULL, 
  [nome] nvarchar(60) NULL, 
  [dominio] nvarchar(100) NULL, 
  CONSTRAINT [PK_divindade] PRIMARY KEY([id]));

CREATE TABLE [equipamento](
  [id] int NOT NULL, 
  [id_grupo] int NULL, 
  [nome] nvarchar(60) NULL, 
  [descricao] nvarchar(160) NULL, 
  [image_file] nvarchar(50) NULL, 
  [valor] int NULL, 
  [arma] int NULL, 
  [defesa] int NULL, 
  [armadura] int NULL, 
  [escudo] int NULL, 
  [capacete] int NULL, 
  CONSTRAINT [PK_equipamento] PRIMARY KEY([id]));

CREATE TABLE [equipamento_armas](
  [id] int NOT NULL, 
  [id_habilidade] int NULL, 
  [minima_forca] int NULL, 
  [minima_dano] int NULL, 
  [l0] int NULL, 
  [m0] int NULL, 
  [p0] int NULL, 
  [alcance] int NULL, 
  CONSTRAINT [PK_equipamento_armas] PRIMARY KEY([id]));

CREATE TABLE [equipamento_defesa](
  [id] int NOT NULL, 
  [tipo] nvarchar(10) NULL, 
  [valor_inicio] int NULL, 
  [absorcao] int NULL, 
  CONSTRAINT [PK_equipamento_defesa] PRIMARY KEY([id]));

CREATE TABLE [equipamento_grupos](
  [id] int NOT NULL, 
  [nome] nvarchar(60) NULL, 
  CONSTRAINT [PK_equipamento_grupos] PRIMARY KEY([id]));

CREATE TABLE [especializacao](
  [id] int NOT NULL, 
  [nome] nvarchar(60) NULL, 
  [descricao] ntext NULL, 
  [id_profissao] int NULL, 
  [id_magia_grupo] int NULL, 
  [id_tecnica_grupo] int NULL, 
  CONSTRAINT [PK_especializacao] PRIMARY KEY([id]));

CREATE TABLE "habilidade"(
  [id] int CONSTRAINT [PK_habilidade_new] PRIMARY KEY NOT NULL UNIQUE, 
  [id_habilidade_grupo] int, 
  [nome] nvarchar(50), 
  [atributo] nvarchar(3), 
  [teste_nivel] int, 
  [restrita] int, 
  [penalidades] nvarchar(50), 
  [tarefas_aperfeicoadas] ntext, 
  [descricao] ntext, 
  [niveis] ntext, 
  [bonus] int DEFAULT 0, 
  [possui_especializacao] int DEFAULT 0);

CREATE TABLE [habilidade_especializacao](
  [id] int NOT NULL, 
  [id_habilidade] int NULL, 
  [sugestao] nvarchar(40) NULL, 
  CONSTRAINT [PK_habilidade_especializacao] PRIMARY KEY([id]));

CREATE TABLE [habilidade_grupo](
  [id] int NOT NULL, 
  [id_pai] int NULL, 
  [nome] nvarchar(100) NULL, 
  CONSTRAINT [PK_habilidade_habilidade_grupo] PRIMARY KEY([id]));

CREATE TABLE "habilidade_grupo_custo"(
  [id_habilidade] int NOT NULL, 
  [id_habilidade_grupo] int NOT NULL, 
  [custo] int NULL, 
  CONSTRAINT [PK_skill2group__0000000000000030] PRIMARY KEY([id_habilidade], [id_habilidade_grupo]));

CREATE TABLE "habilidade_old"(
  [id] int NOT NULL, 
  [nome] nvarchar(100) NULL, 
  [descricao] ntext NULL, 
  [bonus] int NULL, 
  [possui_especializacao] int NULL, 
  CONSTRAINT [PK_habilidade] PRIMARY KEY([id]));

CREATE TABLE [linha_tempo](
  [id] int NOT NULL, 
  [id_localidade] int NULL, 
  [ano] int NULL, 
  [evento] nvarchar(300) NULL, 
  CONSTRAINT [PK_linha_tempo] PRIMARY KEY([id]));

CREATE TABLE [localidade](
  [id] int NOT NULL, 
  [id_pai] int NULL DEFAULT (-1), 
  [nome] nvarchar(60) NULL, 
  [brasao] nvarchar(60) NULL, 
  [nota] ntext NULL, 
  [autor] nvarchar(120) NULL, 
  [x] int NULL DEFAULT 0, 
  [y] int NULL DEFAULT 0, 
  CONSTRAINT [PK_localidade] PRIMARY KEY([id]));

CREATE TABLE [magia](
  [id] int NOT NULL, 
  [nome] nvarchar(60) NULL, 
  [descricao] ntext NULL, 
  [evocacao] nvarchar(40) NULL, 
  [alcance] nvarchar(40) NULL, 
  [duracao] nvarchar(60) NULL, 
  [Nivel] ntext NULL, 
  CONSTRAINT [PK_magia] PRIMARY KEY([id]));

CREATE TABLE [magia_grupo](
  [id] int NOT NULL, 
  [id_pai] int NULL, 
  [nome] nvarchar(100) NULL, 
  CONSTRAINT [PK_magia_grupo] PRIMARY KEY([id]));

CREATE TABLE "magia_grupo_custo"(
  [id_magia] int NOT NULL, 
  [id_magia_grupo] int NOT NULL, 
  [custo] int NULL, 
  CONSTRAINT [PK_magia_magia_grupo] PRIMARY KEY([id_magia], [id_magia_grupo]));

CREATE TABLE [personagem](
  [id] int NOT NULL, 
  [nome] nvarchar(100) NULL, 
  [jogador] nvarchar(100) NULL, 
  [image_file] nvarchar(60) NULL, 
  [att_intelecto] int NULL, 
  [att_aura] int NULL, 
  [att_carisma] int NULL, 
  [att_forca] int NULL, 
  [att_fisico] int NULL, 
  [att_agilidade] int NULL, 
  [att_percepcao] int NULL, 
  [defesa_ativa] int NULL, 
  [defesa_passiva] int NULL, 
  [energia_heroica_maxima] int NULL, 
  [energia_heroica] int NULL, 
  [energia_fisica] int NULL, 
  [absorcao] int NULL, 
  [raca] int NULL, 
  [profissao] int NULL, 
  [especializacao] int NULL, 
  [nivel] int NULL, 
  [pontos_habilidade] int NULL, 
  [pontos_combate] int NULL, 
  [pontos_arma] int NULL, 
  [pontos_magia] int NULL, 
  [altura] int NULL, 
  [peso] int NULL, 
  [idade] int NULL, 
  [olhos] nvarchar(60) NULL, 
  [cabelo] nvarchar(60) NULL, 
  [pele] nvarchar(60) NULL, 
  [aparencia] ntext NULL, 
  [divindade] int NULL, 
  [classe_social] nvarchar(30) NULL, 
  [local_nascimento] int NULL, 
  [historia] ntext NULL, 
  [moedas_cobre] int NULL, 
  [moedas_prata] int NULL, 
  [moedas_ouro] int NULL, 
  CONSTRAINT [PK_personagem] PRIMARY KEY([id]));

CREATE TABLE [personagem_combate](
  [id_personagem] int NOT NULL, 
  [id_combate] int NOT NULL, 
  [nivel] int NULL, 
  CONSTRAINT [PK_personagem_combate] PRIMARY KEY([id_personagem], [id_combate]));

CREATE TABLE [personagem_equipamento](
  [id_personagem] int NOT NULL, 
  [id_equipamento] int NOT NULL, 
  [quantidade] int NULL, 
  CONSTRAINT [PK_personagem_equipamento] PRIMARY KEY([id_personagem], [id_equipamento]));

CREATE TABLE [personagem_habilidade](
  [id_personagem] int NOT NULL, 
  [id_habilidade] int NOT NULL, 
  [nivel] int NULL, 
  CONSTRAINT [PK_personagem_habilidade] PRIMARY KEY([id_personagem], [id_habilidade]));

CREATE TABLE [personagem_habilidade_especializacao](
  [id] int CONSTRAINT [PK_personagem_habilidade_especializacao] PRIMARY KEY NOT NULL, 
  [id_personagem] int, 
  [id_habilidade] int, 
  [id_habilidade_especializacao] INT, 
  [especializacao] nvarchar(40), 
  [nivel] int);

CREATE TABLE [personagem_magia](
  [id_personagem] int NOT NULL, 
  [id_magia] int NOT NULL, 
  [nivel] int NULL, 
  CONSTRAINT [PK_personagem_magia] PRIMARY KEY([id_personagem], [id_magia]));

CREATE TABLE [profissao](
  [id] int NOT NULL, 
  [nome] nvarchar(60) NULL, 
  [image_file] nvarchar(60) NULL, 
  [descricao] ntext NULL, 
  [moedas_cobre] int NULL, 
  [energia_heroica] int NULL, 
  [pontos_habilidade] int NULL, 
  [pontos_arma] int NULL, 
  [pontos_combate] int NULL, 
  [penalidade_habilidade_grupo] int NULL, 
  [especialidade_habilidade] int NULL, 
  [atributo_magia] int NULL, 
  [id_magia_grupo] int NULL, 
  CONSTRAINT [PK_profissao] PRIMARY KEY([id]));

CREATE TABLE [raca](
  [id] int NOT NULL, 
  [nome] nvarchar(60) NULL, 
  [image_file] nvarchar(60) NULL, 
  [attr_int] int NULL, 
  [attr_aur] int NULL, 
  [attr_car] int NULL, 
  [attr_for] int NULL, 
  [attr_fis] int NULL, 
  [attr_agi] int NULL, 
  [attr_per] int NULL, 
  [velocidade_inicio] int NULL, 
  [energia_fisica] int NULL, 
  [altura_inicio] int NULL, 
  [peso_inicio] int NULL, 
  [idade_minima] int NULL, 
  [idade_maxima] int NULL, 
  CONSTRAINT [PK_raca] PRIMARY KEY([id]));

CREATE TABLE [raca_profissao](
  [id_raca] int NOT NULL, 
  [id_profissao] int NOT NULL, 
  CONSTRAINT [PK_raca_profissao] PRIMARY KEY([id_raca], [id_profissao]));


