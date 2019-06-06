select * from equipamento where id_grupo = 6

select a.id,c.id,b.custo,* from habilidade a
left join habilidade_grupo c on a.id_habilidade_grupo = c.id
left join habilidade_grupo_custo b on a.id = b.id_habilidade


id	nome
1	Animais
2	Transportes
3	Residências
4	Material Profissional
5	Miscelâneos
6	Armas
7	Defesas
--pertences e afins
--armaduras,elmos,escudos
Couro leve											2 m.p.
Couro rígido										10 m.p.
Cota de malha parcial								20 m.p.
Cota de malha completa								60 m.p.
Couraça parcial										15 m.o.
Couraça completa									20 m.o.
Cota de malha para montaria							80 m.p.
Cota de malha completa para montaria (elmo incluso) 15 m.o.
Escudo pequeno										2 m.p.
Escudo grande										15 m.p.
Escudo de torre										30 m.p.
Elmo aberto											2 m.p.
Elmo fechado										5 m.p.

--armas 6
Arco composto				20 m.p.
Arco de guerra				25 m.p.
Arco Longo Élfico			12 m.o. (*)
Arco simples				10 m.p.
Arpão						60 m.p.
Axa de armas				50 m.p.
Besta						16 m.o. (*)
Besta Pesada				32 m.o. (*)
Boleadeira					4 m.p.
Bumerangue					20 m.c.
Bumerangue de Corte			12 m.p.
Cajado						5 m.c.
Cimitarra					50 m.p.
Clava						15 m.c.
Espada						40 m.p.
Espada de mão e meia		60 m.p.
Faca						2 m.p.
Flecha (10 unidades)		10 m.c.
Funda						12 m.c.
Gládio						12 m.p.
Lança de cavalaria			60 m.p.
Lança de guarda				17 m.p.
Lança de justa				35 m.p.
Lança leve					8 m.p.
Lança pesada				15 m.p.
Maça						15 m.p.
Maça de armas				30 m.p.
Machadinha					6 m.p.
Machado						10 m.p.
Machado crescente			22 m.p.
Machado de batalha			12 m.p.
Machado de guerra			35 m.p.
Malho						12 m.p.
Mangual						30 m.p.
Mangual leve				25 m.p.
Manopla						2 m.p.
Marreta de guerra			30 m.p.
Martelo de guerra			11 m.p.
Montante					80 m.p.
Porrete						3 m.c.
Projetil de metal/funda		2 m.c.
Projetil de pedra/funda		0
Punhal						5 m.p.
Rapieira					60 m.p.
Rede						80 m.p.
Sabre Élfico				28 m.o (*)
Tridente					8 m.p.

--animais 1
Águia domesticada		50 m.p.
Boi						10 m.p.
Búfalo					20 m.p.
Burro					2 m.p.
Canários				1 m.p.
Cabra/Bode				5 m.p.
Cão comum				0
Cão de raça (Alão)		10 m.p.
Cavalo Comum			50 m.p.
Cavalo de Carga			75 m.p.
Cavalo de Guerra Leve	20 m.o.
Cavalo de Guerra Pesado 40 m.o.
Cavalo treinado			10 m.o.
Coelho					10 m.c.
Corvo ou Pombo Treinado	2 m.p.
Galinha					3 m.c
Ganso/Pato				1 m.p.
Gato de Raça			1 m.p.
Gavião domesticado		30 m.p.
Lebre					15 m.c.
Mula					10 m.p.
Ovelha/Carneiro			20 m.p.
Pônei					40 m.p.
Pônei de guerra leve	75 m.p.
Porco					10 m.p.
Vaca					30 m.p.

--transporte
Barcaça escravista| 45 pessoas + carga					400 m.o.
Barco a remo| 2 pessoas									10 m.o.
Barco grande a remo| 4 pessoas + carga					20 m.o.
Canoa| 1 pessoa + carga									10 m.p.
Canoa de troncos| 1 pessoa								5 m.p.
Canoa longa| 2 pessoas + carga							50 m.p.
Caravela| 60 pessoas + carga							500 m.o.
Carro de boi| 2 pessoas + carga 2 TON					20 m.p.
Carroça| 4 pessoas + carga 1,5 TON						40 m.p.
Carruagem (p/2 cavalos)| 6 pessoas						20 m.o.
Carruagem pesada (p/4 cavalos)| 6 pessoas + carga 3 TON	40 m.o.
Charrete rápida (p/2 cavalos)| 2 pessoas				10 m.o.
Galera pequena| 15 pessoas + carga						100 m.o.
Trenó p/ 10 cachorros| 1 pessoa + carga					10 m.p.
Veleiro pequeno| 8 pessoas + carga						50 m.o.

--residencia
Barraca de Lona (1 pessoa)						5 m.p.
Casa confortável (5 cômodos)					50 m.o.
Casa de ofício (Galpão, com 1 cômodo extra)		25 m.o.
Casa grande (10+ cômodos)						100 m.o.
Casa simples (3 cômodos)						12 m.o.
Castelo Grande 1000m² x 10km²					100.000 m.o.
Castelo pequeno 500m² x 4km²					25.000 m.o.
Choupana (2 cômodos)							40 m.p.
Farol											1000 m.o.
Fortaleza										10.000 m.o.
Forte											2.000 m.o
Muralha (50 metros)								50 m.o.
Tenda (4 pessoas)								10 m.p.
Torreão											5.000 m.o.

--estalagem
Aluguel de uma Casa Confortável						10 m.p.
Aluguel de uma Casa Simples4						5 m.p.
Hospedagem barata (individual)						3 m.c.
Hospedagem boa (banho e cama de casal)				1 m.p.
Hospedagem coletiva (10 pessoas)					1 m.c.
Hospedagem média (individual com banho)				5 m.c.
Hospedagem nobre (cama de casal, banho e serviçal)	5 m.p.

--refeicao
Água fresca														1 m.c.
Banquete nobre para 5 pessoas c/ bebidas e comidas variadas		60 m.p.
Banquete para 5 pessoas c/ bebidas e comidas variadas			20 m.p.
Barril d’água (5 litros)										5 m.c.
Cesta de frutas													3 m.c.
Condimentos (sal, alho, coentro, temperos diversos e etc)		5 m.p.
Copo de vinho bom												1 m.p.
Copo de vinho comum													2 m.c.
Especiarias (azeite, vinagre, pimenta, alecrim, ervas finas e etc)	20 m.p.
Grãos (500 gramas)													6 m.c.
Hortaliças e legumes												2 m.c.
Insetos comestíveis preparados - fritos ou assados (150 gramas) – aranhas, escorpião, grilos, gafanhotos, larvas e etc. 1 m.c.
Odre de vinho bom (1 litro)											1 m.p.
Odre de vinho comum (1 litro)										1 m.p.
Ração para animais (saco médio de 20 kg) – 3 dias					2 m.c.
Ração Semanal (carne seca e queijo)									3 m.p.
Refeição barata (moídos de frango e porco sem tempero ou peixe, pão e fruta)	3 m.c.
Refeição boa (carne bovina temperada e grãos)									3 m.p.
Refeição cara (carne nobre bovina temperada, carnes exóticas, grãos e etc)		5 m.p.
Refeição Normal (carne de frango ou suína e etc. pouco temperada e grãos)		5 m.c.
Tonel de vinho comum (5 litros)													4 m.p.
Ração para animais (saco grande 40 kg de Feno) – uma semana para um cavalo		4 m.c.

--vestimenta
Cachecol de lã						4 m.c.
Capa								3 m.c.
Capa Longa							6 m.c.
Casaco de lã						6 m.c.
Chapéu de Palha						2 m.c
Cinto								2 m.c.
Cinto multiuso						1 m.p.
Cobertor							8 m.c.
Manta de carneiro					1 m.p.
Manto com capuz						8 m.c.
Par de botas						5 m.c.
Par de botas de couro				1 m.p.
Par de botas para Cavalaria			5 m.p.
Par de botas para Infantaria		5 m.p.
Par de luvas						3 m.c.
Par de luvas de couro				5 m.c.
Par de luvas metálicas (manoplas)	2 m.p.
Par de sandálias					2 m.c.
Pele de animal selvagem				5 m.p.
Roupa comum							3 m.c.
Roupa de linho						12 m.c.
Roupa intima						1 m.c.
Roupa para inverno					2 m.p.
Roupa tingida						6 m.c.
Sobretudo							3 m.p.
Tecido bom (1 metro)				5 m.c.
Tecido nobre (1 metro)				5 m.p.
Traje nobre (pronto)				30 m.p.

-- material profissional
Estojo de Cirurgia Anestésico (Feito de Beladona) doses maiores poderiam ser letais, ópio, láudano.
Seringa, agulhas, serrote, cateteres, colher de flecha, linha, faca, panos limpos, etc.
50 m.p.
Estojo de primeiros socorros
(Recupera 200 de EF)
Bandagens, tala, pomadas cicatrizantes, agulha, fio, sal e etc. 10 m.p.
Estojo para arrombamento Pé de cabra, martelo, haste de metal. 10 m.p.
Estojo para disfarces Tinta facial, peruca, pó de arroz, acessórios e etc. 25 m.p.
Estojo para higiene pessoal Sabonete, pano de rosto, pente, palito de dente, repelente, pinico e etc. 5 m.p.
Estojo para jogos Dados, cartas, copos, peças e etc. 1 m.p.
Estojo para pesca Anzol, linha, puçá, faca, tarrafa, rede, vara de pesca e etc. 12 m.p.
Estojo para trabalho em metal Carvão mineral, fole, fôrmas diversas, jogo de torquês, malho, martelos e pedra de
amolar.
50 m.p.
Estojo para trabalhos em madeira Machadinha, serrote pequeno, cola, pregos, martelo, drena, plaina e etc. 30 m.p.
Estojo para trabalhos manuais Agulha, barbante, cola, dedal, fios, linhas, martelinho, navalha, tachas e tesoura. 3 m.p.
Material completo para
construção, agricultura ou
mineração
Pá, balde, picareta, inchada, arado, peneira, vassoura, roldanas, cordas, gancho e etc. 80 m.p.
Material completo para escalada 100 metros de corda, ganchos, 10 pítons, e etc. 20 m.p.
Material completo para
laboratório de venefício,
herbalismo ou de alquimia.
Almofariz ou pilão; balança; colheres de tamanhos variados; facas de tamanhos
diferentes; frascos de vidro, de tamanhos e formas diferentes; fogareiro a óleo; funis;
lamparina; panelas de cobre e de barro; tigelas de madeira ou cerâmica; etc.
20 m.p.
Material completo para montaria Cela, cabresto, ferradura, rédeas e etc. 12 m.p.
Material completo para trabalhos
em metais
Bigorna, fornalha e estojo para trabalho em metais. Este conjunto não pode ser
transportado.
10 m.o.
Material para Destravar
Fechaduras
Gazuas, alicates, serra pequena, lima, pó de chumbo negro, grafite, etc 3 m.p

--instrumentos musicais
Alaúde			30 m.p.
Apito			1 m.c.
Atabaque		6 m.c.
Balalaica		12 m.p.
Bandolim		20 m.p.
Banjo			10 m.p.
Berrante		1 m.p.
Chocalho		3 m.c.
Clarineta		3 m.p.
Flauta de madeira		12 m.c.
Flauta longa de metal	3 m.p.
Gaita				6 m.p.
Harpa				50 m.p.
Pandeirola			5 m.c.
Rabeca				8 m.p.
Sino				2 m.c.
Tambor				1 m.p.
Triângulo de metal	3 m.c.

--gemas
Âmbar, Quartzo, Obsidiana Rotineiro					1 m.p.
Ametista, Topázio, Granada, Citrino Fácil			5 m.p.
Perola, Opala, Agua Marinha Médio					20 m.p.
Opala Preta, Perola Negra, Turmalina Dificil		50 m.p.
Turmalina Bicolor, Safira, Esmeralda Muito Dificil	20 m.o.
Rubi e Diamante Absurdo								50 m.o.
Diamante Vermelho Impossível						500 m.o.

-- miscelanes
Água abençoada (250 ml) Causa 1 de dano na EF ou 4 na EH, reduz em 1 a RM "não acumula". Funciona contra demônios
e mortos vivos. Somente Sacerdotes com a magia Sagração de Itens 1, podem abençoar até 1 Litro/Karma
5 m.c.
Alforje 3 m.p.
Alforje grande p/ montaria 12 m.p.
Algemas 1 m.p.
Algibeira (500 g) 1 m.p.
Aljava 5 m.p.
Ampulheta 8 m.p.
Artesanato 3 m.c.
Bacia para banho 5 m.c.
Bainha para punhais e espadas 12 m.c.
Balança 12 m.p.
Baú c/ hastes de metal 2 m.p.
Baú de madeira (até 10 kg) 5 m.p.
Baú de madeira grande (até 20 kg) 10 m.p.
Barras de Ferro Bruto 10 m.p.
Bengalas e raquete para neve (par) 5 m.p.
Bijuterias e penduricalhos (unidade) 2 m.c.
Cachimbo 3 m.c.
Cadeado grande 3 m.p.
Cadeado médio 1 m.p.
Cadeado pequeno 8 m.c.
Cama de palha 1 m.p.
Caneca de madeira 2 m.c.
Cantil (1 litro) 6 m.c.
Canudo de respiração para mergulho 12 m.c.
Cola natural 1 m.p.
Coleira de couro 8 m.c.
Coleira de metal 2 m.p.
Componentes místicos 10 m.p.
Corda (20 metros) 1 m.p.
Corda trançada (50 metros) 8 m.p.
Corrente de metal (5 metros) 3 m.p.
Corrente de metal grossa (5 metros) 5 m.p.
Escada de madeira de 10 metros 2 m.p.
Escada de madeira de 5 metros 1 m.p.
Espelho de cobre 1 m.p.
Espelho de prata 10 m.p.
Estopa 1 m.c.
Fechadura complexa 5 m.p.
Fechadura normal 1 m.p.
Fechadura simples 5 m.c.
Feno (10 kg) 1 m.c.
Ferradura para neve 8 m.p.
Flores 2 m.c.
Frasco de cerâmica 5 m.c.
Frasco de coco 3 m.c.
Frasco de metal 8 m.p.
Frasco de vidro 5 m.p.
Fumo (300 g) 3 m.c.
Funil 6 m.c.
Gaiola para pássaros 3 m.c.
Gancho 4 m.p.
Gancho de três pontas 10 m.p.
Giz de cera (10 unidades) 5 m.c.
Incensos (10 unidades) 3 m.c.
Lamparina a óleo (100 ml, 4 horas, ilumina 3 m² lugar fechado ) 12 m.c.
Lamparina a vela (1 h, 3 m² lugar fechado) 5 m.c.
Lanterna a óleo (1 L = 48 horas) 5 m.p.
Lanterna direcional 8 m.p.
Leque 5 m.c.
Leque ornamentado 8 m.p.
Maca 6 m.p.
Mochila de Aventureiro (50 kg) 12 m.p.
Mochila de Couro (10 kg) 12 m.c.
Mochila de pano fivelada (5kg) 10 m.c.
Mochila grande (20 kg) 5 m.p.
Mochila para provisões (5 kg) 6 m.c.
Navalha 1 m.p.
Odre 1 L 6 m.c.
Óleo de lanterna (500 ml, dura 24 h) 1 m.p.
Papiro (unidade) 3 m.c.
Pederneiras 5 m.c.
Pena e tinta 5 m.p.
Pergaminho (unidade) 8 m.p.
Pítons para alpinismo (10 unidades) 5 m.p.
Porta mapas 3 m.c.
Rédeas para cães puxadores de Trenó 3 m.p.
Remos 2 m.p.
Repelente vegetal 2 m.p.
Saco de dormir 12 m.c.
Saco grande (5 kg) 5 m.c.
Saco pequeno (1,5 kg) 2 m.c.
Sementes para plantio (diversos) 1 m.p.
Símbolo sagrado de ferro 1 m.p.
Símbolo sagrado de madeira 2 m.c.
Símbolo sagrado de ouro 80 m.p.
Símbolo sagrado de prata 8 m.p.
Tábuas de Madeira comum 6 m.c.
Tábuas de Madeira maciça 12 m.c.
Tábuas de pedra 8 m.p
Tábuas de pedra nobre 30 m.p.
Tochas (10 uni. Dura 1 hora) 2 m.p.
Travesseiro de penas de ganso 8 m.p.
Utensílios de cozinha 12 m.p.
Utensílios de limpeza 8 m.p.
Vela (10 uni.) 1 m.p.
Velas coloridas para ritual (10 uni.) 3 m.p.









select * from equipamento where id_grupo =6
--basicas
select id,nome from Combate a
--inner join
  
--Basicas
INSERT INTO [combate_grupo_custo](id_combate,id_combate_grupo,custo) values (4,1,2);
INSERT INTO [combate_grupo_custo](id_combate,id_combate_grupo,custo)values (6,1,1);
INSERT INTO [combate_grupo_custo](id_combate,id_combate_grupo,custo)values (10,1,1);
INSERT INTO [combate_grupo_custo](id_combate,id_combate_grupo,custo)values (16,1,2);
INSERT INTO [combate_grupo_custo](id_combate,id_combate_grupo,custo)values (17,1,1);
INSERT INTO [combate_grupo_custo](id_combate,id_combate_grupo,custo)values (18,1,1);
INSERT INTO [combate_grupo_custo](id_combate,id_combate_grupo,custo)values (24,1,2);
INSERT INTO [combate_grupo_custo](id_combate,id_combate_grupo,custo)values (29,1,1);
INSERT INTO [combate_grupo_custo](id_combate,id_combate_grupo,custo)values (40,1,2);
INSERT INTO [combate_grupo_custo](id_combate,id_combate_grupo,custo)values (44,1,1);
INSERT INTO [combate_grupo_custo](id_combate,id_combate_grupo,custo)values (50,1,2);
INSERT INTO [combate_grupo_custo](id_combate,id_combate_grupo,custo)values (54,1,2);

--grupos
INSERT INTO [combate_grupo] ([id],[id_pai],[nome]) VALUES (1,-1,'Técnicas de Combate (Básicas)');
INSERT INTO [combate_grupo] ([id],[id_pai],[nome]) VALUES (2,-1,'Técnicas de Combate (Restritas)');
INSERT INTO [combate_grupo] ([id],[id_pai],[nome]) VALUES (3,-1,'Técnicas de Combate (Avançadas)');
INSERT INTO [combate_grupo] ([id],[id_pai],[nome]) VALUES (4,2,'Guerreiros');
INSERT INTO [combate_grupo] ([id],[id_pai],[nome]) VALUES (5,2,'Ladinos');
INSERT INTO [combate_grupo] ([id],[id_pai],[nome]) VALUES (6,3,'Academia de Infantaria');
INSERT INTO [combate_grupo] ([id],[id_pai],[nome]) VALUES (7,3,'Academia dos Arqueiros');
INSERT INTO [combate_grupo] ([id],[id_pai],[nome]) VALUES (8,3,'Academia dos Cavaleiros');
INSERT INTO [combate_grupo] ([id],[id_pai],[nome]) VALUES (9,3,'Academia dos Gladiadores');
INSERT INTO [combate_grupo] ([id],[id_pai],[nome]) VALUES (10,3,'Guilda dos Assassinos');
INSERT INTO [combate_grupo] ([id],[id_pai],[nome]) VALUES (11,3,'Guilda dos Ladrões');
INSERT INTO [combate_grupo] ([id],[id_pai],[nome]) VALUES (12,3,'Guilda dos Piratas');

--insert into habilidade_grupo_custo(id_habilidade,id_habilidade_grupo,custo)values(40,1,2);
--insert into habilidade_grupo_custo(id_habilidade,id_habilidade_grupo,custo)values(41,6,2);
--insert into habilidade_grupo_custo(id_habilidade,id_habilidade_grupo,custo)values(42,5,1);

CREATE TABLE [combate_grupo] (
  [id] int  NOT NULL
, [id_pai] int  NULL
, [nome] nvarchar(100)  NULL
, CONSTRAINT [PK_combate_grupo] PRIMARY KEY ([id])
);

CREATE TABLE [combate_grupo_custo] (
  [id_combate] int  NOT NULL
, [id_combate_grupo] int  NOT NULL
, [custo] int  NULL
, CONSTRAINT [PK_combate_grupo_custo] PRIMARY KEY ([id_combate],[id_combate_grupo])
);