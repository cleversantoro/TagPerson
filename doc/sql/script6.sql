select * from equipamento where id_grupo = 6

select a.id,c.id,b.custo,* from habilidade a
left join habilidade_grupo c on a.id_habilidade_grupo = c.id
left join habilidade_grupo_custo b on a.id = b.id_habilidade

--equipamento_grupo
INSERT INTO [equipamento_grupos](id,nome) VALUES (1,'Animais');
INSERT INTO [equipamento_grupos](id,nome) VALUES (2,'Transportes');
INSERT INTO [equipamento_grupos](id,nome) VALUES (3,'Residências');
INSERT INTO [equipamento_grupos](id,nome) VALUES (4,'Material Profissional');
INSERT INTO [equipamento_grupos](id,nome) VALUES (5,'Miscelâneos');
INSERT INTO [equipamento_grupos](id,nome) VALUES (6,'Armas');
INSERT INTO [equipamento_grupos](id,nome) VALUES (7,'Defesas');INSERT INTO [equipamento_grupos](id,nome) VALUES (8,'Estalagem');
INSERT INTO [equipamento_grupos](id,nome) VALUES (9,'Refeição');
INSERT INTO [equipamento_grupos](id,nome) VALUES (10,'Vestimenta');
INSERT INTO [equipamento_grupos](id,nome) VALUES (11,'Instrumentos Musicais');
INSERT INTO [equipamento_grupos](id,nome) VALUES (12,'Gemas');

--pertences e afins
--animais 1
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (1,1,'Águia domesticada',500);		;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (2,1,'Boi',100)	;					;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (3,1,'Búfalo',200)					;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (4,1,'Burro',20)					;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (5,1,'Canários',10)					;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (6,1,'Cabra/Bode',50)				;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (7,1,'Cão comum',0)					;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (8,1,'Cão de raça (Alão)',100)		;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (9,1,'Cavalo Comum',500)			;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (10,1,'Cavalo de Carga',750)			;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (11,1,'Cavalo de Guerra Leve',2000)	;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (12,1,'Cavalo de Guerra Pesado',4000);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (13,1,'Cavalo treinado',1000)	   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (14,1,'Coelho',10)				   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (15,1,'Corvo ou Pombo Treinado',20) ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (16,1,'Galinha',3)				   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (17,1,'Ganso/Pato',10)			   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (18,1,'Gato de Raça',10)			   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (19,1,'Gavião domesticado',300)	   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (20,1,'Lebre',15)				   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (21,1,'Mula',100)				   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (22,1,'Ovelha/Carneiro',200)		   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (23,1,'Pônei',400)				   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (24,1,'Pônei de guerra leve',750)   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (25,1,'Porco',100)				   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (26,1,'Vaca',300)				   ;
--transporte 2
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (27,2,'Barcaça escravista','45 pessoas + carga',40000);
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (28,2,'Barco a remo', '2 pessoas',1000)			   ;
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (29,2,'Barco grande a remo', '4 pessoas + carga',2000);
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (30,2,'Canoa', '1 pessoa + carga',100)				   ;
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (31,2,'Canoa de troncos', '1 pessoa',50)			   ;
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (32,2,'Canoa longa', '2 pessoas + carga',500)		   ;
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (33,2,'Caravela', '60 pessoas + carga',50000)		   ;
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (34,2,'Carro de boi', '2 pessoas + carga 2 TON',200)  ;
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (35,2,'Carroça', '4 pessoas + carga 1,5 TON',400)	   ;
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (36,2,'Carruagem (p/2 cavalos)', '6 pessoas',2000)	   ;
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (37,2,'Carruagem pesada (p/4 cavalos)', '6 pessoas + carga 3 TON',4000);
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (38,2,'Charrete rápida (p/2 cavalos)', '2 pessoas',1000);
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (39,2,'Galera pequena', '15 pessoas + carga',10000)	 ;
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (40,2,'Trenó p/ 10 cachorros', '1 pessoa + carga',100)	 ;
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (41,2,'Veleiro pequeno', '8 pessoas + carga',5000)		 ;
--residencia 3			  
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (42,3,'Barraca de Lona (1 pessoa)',50); 
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (43,3,'Casa confortável (5 cômodos)',5000);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (44,3,'Casa de ofício (Galpão, com 1 cômodo extra)',2500);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (45,3,'Casa grande (10+ cômodos)',10000);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (46,3,'Casa simples (3 cômodos)',1200);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (47,3,'Castelo Grande 1000m² x 10km²',10000000);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (48,3,'Castelo pequeno 500m² x 4km²',2500000);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (49,3,'Choupana (2 cômodos)',400);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (50,3,'Farol',100000);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (51,3,'Fortaleza',1000000);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (52,3,'Forte',200000);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (53,3,'Muralha (50 metros)',5000);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (54,3,'Tenda (4 pessoas)',100);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (55,3,'Torreão',500000);
-- material profissional 4
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (56,4,'Estojo de Cirurgia Anestésico (Feito de Beladona) doses maiores poderiam ser letais, ópio, láudano','Seringa, agulhas, serrote, cateteres, colher de flecha, linha, faca, panos limpos, etc.',500);
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (57,4,'Estojo de primeiros socorros (Recupera 200 de EF)','Bandagens, tala, pomadas cicatrizantes, agulha, fio, sal e etc.', 100);
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (58,4,'Estojo para arrombamento','Pé de cabra, martelo, haste de metal.', 100);
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (59,4,'Estojo para disfarces', 'Tinta facial, peruca, pó de arroz, acessórios e etc.' ,250);
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (60,4,'Estojo para higiene pessoal', 'Sabonete, pano de rosto, pente, palito de dente, repelente, pinico e etc.' ,50);
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (61,4,'Estojo para jogos', 'Dados, cartas, copos, peças e etc.' ,10);
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (62,4,'Estojo para pesca', 'Anzol, linha, puçá, faca, tarrafa, rede, vara de pesca e etc.',120);
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (63,4,'Estojo para trabalho em metal', 'Carvão mineral, fole, fôrmas diversas, jogo de torquês, malho, martelos e pedra de amolar.' ,500);
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (64,4,'Estojo para trabalhos em madeira', 'Machadinha, serrote pequeno, cola, pregos, martelo, drena, plaina e etc.' ,300);
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (65,4,'Estojo para trabalhos manuais', 'Agulha, barbante, cola, dedal, fios, linhas, martelinho, navalha, tachas e tesoura.' ,30);
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (66,4,'Material completo para construção, agricultura ou mineração' ,'Pá, balde, picareta, inchada, arado, peneira, vassoura, roldanas, cordas, gancho e etc.' ,800);
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (67,4,'Material completo para escalada', '100 metros de corda, ganchos, 10 pítons, e etc.' ,200);
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (68,4,'Material completo para laboratório de venefício,herbalismo ou de alquimia.' ,'Almofariz ou pilão; balança; colheres de tamanhos variados; facas de tamanhos diferentes; frascos de vidro, de tamanhos e formas diferentes; fogareiro a óleo; funis; lamparina; panelas de cobre e de barro; tigelas de madeira ou cerâmica; etc.' ,200);
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (69,4,'Material completo para montaria', 'Cela, cabresto, ferradura, rédeas e etc.' ,120);
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (70,4,'Material completo para trabalhos em metais', 'Bigorna, fornalha e estojo para trabalho em metais. Este conjunto não pode ser transportado.' ,1000);
INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (71,4,'Material para Destravar Fechaduras', 'Gazuas, alicates, serra pequena, lima, pó de chumbo negro, grafite, etc' ,30);
-- miscelanes 5			  
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (72,5,'Alforje', 30);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (73,5,'Alforje grande p/ montaria',120);				   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (74,5,'Algemas',10)									   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (75,5,'Algibeira (500 g)',10)						   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (76,5,'Aljava',50)									   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (77,5,'Ampulheta',80)								   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (78,5,'Artesanato',3)								   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (79,5,'Bacia para banho',5)							   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (80,5,'Bainha para punhais e espadas', 12)			   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (81,5,'Balança',120)									   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (82,5,'Baú c/ hastes de metal',20)					   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (83,5,'Baú de madeira (até 10 kg)',50)				   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (84,5,'Baú de madeira grande (até 20 kg)',100)		   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (85,5,'Barras de Ferro Bruto',100)					   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (86,5,'Bengalas e raquete para neve (par)',50)		   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (87,5,'Bijuterias e penduricalhos (unidade)',	2)	   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (88,5,'Cachimbo', 3),									   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (89,5,'Cadeado grande', 30)							   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (90,5,'Cadeado médio', 10)							   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (91,5,'Cadeado pequeno', 8)							   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (92,5,'Cama de palha', 10)							   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (93,5,'Caneca de madeira', 2)						   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (94,5,'Cantil (1 litro)', 6)							   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (95,5,'Canudo de respiração para mergulho', 12)		   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (96,5,'Cola natural', 10)							   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (97,5,'Coleira de couro', 8)							   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (98,5,'Coleira de metal', 20)						   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (99,5,'Componentes místicos', 100)					   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (100,5,'Corda (20 metros)', 10)						   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (101,5,'Corda trançada (50 metros)', 80)				   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (102,5,'Corrente de metal (5 metros)', 30)			   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (103,5,'Corrente de metal grossa (5 metros)', 50)		   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (104,5,'Escada de madeira de 10 metros', 20)			   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (105,5,'Escada de madeira de 5 metros', 10)			   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (106,5,'Espelho de cobre', 10)						   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (107,5,'Espelho de prata', 100)						   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (108,5,'Estopa', 1)									   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (109,5,'Fechadura complexa', 50)						   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (110,5,'Fechadura normal', 10)						   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (111,5,'Fechadura simples', 5)						   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (112,5,'Feno (10 kg)', 1)								   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (113,5,'Ferradura para neve', 80)						   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (114,5,'Flores', 2)									   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (115,5,'Frasco de cerâmica', 5)						   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (116,5,'Frasco de coco', 3)							   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (117,5,'Frasco de metal', 80)							   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (118,5,'Frasco de vidro', 50)							   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (119,5,'Fumo (300 g)', 3)								   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (120,5,'Funil', 6)									   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (121,5,'Gaiola para pássaros', 3)						   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (122,5,'Gancho', 40)									   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (123,5,'Gancho de três pontas', 100)					   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (124,5,'Giz de cera (10 unidades)', 5)				   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (125,5,'Incensos (10 unidades)', 3)					   ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (126,5,'Lamparina a óleo (100 ml, 4 horas, ilumina 3 m² lugar fechado )', 12);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (127,5,'Lamparina a vela (1 h, 3 m² lugar fechado)', 5)	;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (128,5,'Lanterna a óleo (1 L = 48 horas)', 50)			;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (129,5,'Lanterna direcional', 80)							;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (130,5,'Leque', 5)										;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (131,5,'Leque ornamentado', 80)							;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (132,5,'Maca', 60)										;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (133,5,'Mochila de Aventureiro (50 kg)', 120)				;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (134,5,'Mochila de Couro (10 kg)', 12)					;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (135,5,'Mochila de pano fivelada (5kg)', 10)				;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (136,5,'Mochila grande (20 kg)', 50)						;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (137,5,'Mochila para provisões (5 kg)', 6)				;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (138,5,'Navalha', 10)										;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (139,5,'Odre 1 L', 6)										;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (140,5,'Óleo de lanterna (500 ml, dura 24 h)', 10)		;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (141,5,'Papiro (unidade)', 3)								;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (142,5,'Pederneiras', 5)									;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (143,5,'Pena e tinta', 50)								;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (144,5,'Pergaminho (unidade)', 80)						;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (145,5,'Pítons para alpinismo (10 unidades)', 50)			;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (146,5,'Porta mapas', 3)									;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (147,5,'Rédeas para cães puxadores de Trenó', 30)			;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (148,5,'Remos', 20)										;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (149,5,'Repelente vegetal', 20)							;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (150,5,'Saco de dormir', 12)								;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (151,5,'Saco grande (5 kg)', 5)							;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (152,5,'Saco pequeno (1,5 kg)', 2)						;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (153,5,'Sementes para plantio (diversos)', 10)			;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (154,5,'Símbolo sagrado de ferro', 10)					;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (155,5,'Símbolo sagrado de madeira', 2)					;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (156,5,'Símbolo sagrado de ouro', 800)					;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (157,5,'Símbolo sagrado de prata', 80)					;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (158,5,'Tábuas de Madeira comum', 6)						;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (159,5,'Tábuas de Madeira maciça', 12)					;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (160,5,'Tábuas de pedra', 80)								;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (171,5,'Tábuas de pedra nobre', 300)						;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (172,5,'Tochas (10 uni. Dura 1 hora)', 20)				;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (173,5,'Travesseiro de penas de ganso', 80)				;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (174,5,'Utensílios de cozinha', 120)						;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (175,5,'Utensílios de limpeza', 80)						;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (176,5,'Vela (10 uni.)', 10)								;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (177,5,'Velas coloridas para ritual (10 uni.)', 30)		;
--armas 6				  
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (178,6,1,'Arco composto',200)		  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (179,6,1,'Arco de guerra',250)		  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (180,6,1,'Arco Longo Élfico',120)	  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (181,6,1,'Arco simples',100)			  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (182,6,1,'Arpão',600)				  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (183,6,1,'Axa de armas',500)			  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (184,6,1,'Besta',160)				  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (185,6,1,'Besta Pesada',320)			  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (186,6,1,'Boleadeira',40	)			  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (187,6,1,'Bumerangue',20	)			  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (188,6,1,'Bumerangue de Corte',120)		;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (189,6,1,'Cajado',5)					  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (190,6,1,'Cimitarra',500)			  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (191,6,1,'Clava',15)					  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (192,6,1,'Espada',400)				  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (193,6,1,'Espada de mão e meia',600)		;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (194,6,1,'Faca',20)					  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (195,6,1,'Flecha (10 unidades)',10	);
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (196,6,1,'Funda',12	)				  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (197,6,1,'Gládio',120)				  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (198,6,1,'Lança de cavalaria',600)		;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (199,6,1,'Lança de guarda',170)		  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (200,6,1,'Lança de justa',350)		  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (201,6,1,'Lança leve',80	)			  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (202,6,1,'Lança pesada',150)			  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (203,6,1,'Maça',150)					  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (204,6,1,'Maça de armas',300)		  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (205,6,1,'Machadinha',60	)			  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (206,6,1,'Machado',100)				  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (207,6,1,'Machado crescente',220)		;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (208,6,1,'Machado de batalha',120)		;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (209,6,1,'Machado de guerra',350)		;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (210,6,1,'Malho',120)				  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (211,6,1,'Mangual',300)				  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (212,6,1,'Mangual leve',250)			  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (213,6,1,'Manopla',20)				  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (214,6,1,'Marreta de guerra',300)		;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (215,6,1,'Martelo de guerra',110)		;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (216,6,1,'Montante',800)				  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (217,6,1,'Porrete',3)				  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (218,6,1,'Projetil de metal/funda',2)	;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (219,6,1,'Projetil de pedra/funda',0)  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (220,6,1,'Punhal',50	)				  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (221,6,1,'Rapieira',600)				  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (222,6,1,'Rede',800)					  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (223,6,1,'Sabre Élfico',2800)		  ;
INSERT INTO [equipamento](id,id_grupo,arma,nome,valor) VALUES (224,6,1,'Tridente',80)				  ;
--armaduras,elmos,escudos 7
INSERT INTO [equipamento](id,id_grupo,armadura,escudo,capacete,defesa,arma,nome,valor) VALUES (225,7,1,0,0,1,0,'Couro leve',20)				  ;
INSERT INTO [equipamento](id,id_grupo,armadura,escudo,capacete,defesa,arma,nome,valor) VALUES (226,7,1,0,0,1,0,'Couro rígido',100)				  ;
INSERT INTO [equipamento](id,id_grupo,armadura,escudo,capacete,defesa,arma,nome,valor) VALUES (227,7,1,0,0,1,0,'Cota de malha parcial',200)	  ;
INSERT INTO [equipamento](id,id_grupo,armadura,escudo,capacete,defesa,arma,nome,valor) VALUES (228,7,1,0,0,1,0,'Cota de malha completa',600)	  ;
INSERT INTO [equipamento](id,id_grupo,armadura,escudo,capacete,defesa,arma,nome,valor) VALUES (229,7,1,0,0,1,0,'Couraça parcial',1500)			  ;
INSERT INTO [equipamento](id,id_grupo,armadura,escudo,capacete,defesa,arma,nome,valor) VALUES (230,7,1,0,0,1,0,'Couraça completa',2000)		  ;
INSERT INTO [equipamento](id,id_grupo,armadura,escudo,capacete,defesa,arma,nome,valor) VALUES (231,7,1,0,0,1,0,'Cota de malha para montaria',800);
INSERT INTO [equipamento](id,id_grupo,armadura,escudo,capacete,defesa,arma,nome,valor) VALUES (232,7,1,0,0,1,0,'Cota de malha completa para montaria (elmo incluso)',1500);
INSERT INTO [equipamento](id,id_grupo,armadura,escudo,capacete,defesa,arma,nome,valor) VALUES (233,7,0,1,0,1,1,'Escudo pequeno',20)  ;
INSERT INTO [equipamento](id,id_grupo,armadura,escudo,capacete,defesa,arma,nome,valor) VALUES (234,7,0,1,0,1,1,'Escudo grande',150)  ;
INSERT INTO [equipamento](id,id_grupo,armadura,escudo,capacete,defesa,arma,nome,valor) VALUES (235,7,0,1,0,1,1,'Escudo de torre',300);
INSERT INTO [equipamento](id,id_grupo,armadura,escudo,capacete,defesa,arma,nome,valor) VALUES (236,7,0,0,1,1,0,'Elmo aberto',20);
INSERT INTO [equipamento](id,id_grupo,armadura,escudo,capacete,defesa,arma,nome,valor) VALUES (237,7,0,0,1,1,0,'Elmo fechado',50);
--estalagem 8			  
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (238,8,'Aluguel de uma Casa Confortável',100)		 ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (239,8,'Aluguel de uma Casa Simples',450)			 ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (240,8,'Hospedagem barata (individual)',3)		 ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (241,8,'Hospedagem boa (banho e cama de casal)',10);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (242,8,'Hospedagem coletiva (10 pessoas)',1)		 ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (243,8,'Hospedagem média (individual com banho)',5);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (244,8,'Hospedagem nobre (cama de casal, banho e serviçal)',50);
--refeicao 9			  
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (245,9,'Água fresca',1);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (246,9,'Banquete nobre para 5 pessoas c/ bebidas e comidas variadas',600);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (247,9,'Banquete para 5 pessoas c/ bebidas e comidas variadas',200);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (248,9,'Barril d’água (5 litros)',5);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (249,9,'Cesta de frutas',30);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (250,9,'Condimentos (sal, alho, coentro, temperos diversos e etc)',500);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (251,9,'Copo de vinho bom',100);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (252,9,'Copo de vinho comum',2);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (253,9,'Especiarias (azeite, vinagre, pimenta, alecrim, ervas finas e etc)',200);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (254,9,'Grãos (500 gramas)',6);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (255,9,'Hortaliças e legumes',2);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (256,9,'Insetos comestíveis preparados - fritos ou assados (150 gramas) – aranhas, escorpião, grilos, gafanhotos, larvas e etc.',1);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (257,9,'Odre de vinho bom (1 litro)',10);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (258,9,'Odre de vinho comum (1 litro)',10);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (259,9,'Ração para animais (saco médio de 20 kg) – 3 dias',2);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (260,9,'Ração Semanal (carne seca e queijo)',30);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (261,9,'Refeição barata (moídos de frango e porco sem tempero ou peixe, pão e fruta)',3);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (262,9,'Refeição boa (carne bovina temperada e grãos)',30);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (263,9,'Refeição cara (carne nobre bovina temperada, carnes exóticas, grãos e etc)',50);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (264,9,'Refeição Normal (carne de frango ou suína e etc. pouco temperada e grãos)',5);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (265,9,'Tonel de vinho comum (5 litros)',40);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (266,9,'Ração para animais (saco grande 40 kg de Feno) – uma semana para um cavalo',4);
--vestimenta 10			  
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (267,10,'Cachecol de lã',4)		 ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (268,10,'Capa',3)					 ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (269,10,'Capa Longa',6)			 ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (270,10,'Casaco de lã',6)			 ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (271,10,'Chapéu de Palha',2)		 ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (272,10,'Cinto',2)				 ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (273,10,'Cinto multiuso',10)		 ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (274,10,'Cobertor',8)				 ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (275,10,'Manta de carneiro',10)	 ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (276,10,'Manto com capuz',8)		 ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (277,10,'Par de botas',5)			 ;
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (278,10,'Par de botas de couro',10);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (279,10,'Par de botas para Cavalaria',50);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (280,10,'Par de botas para Infantaria',50);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (281,10,'Par de luvas',3);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (282,10,'Par de luvas de couro',5);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (283,10,'Par de luvas metálicas (manoplas)',20);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (284,10,'Par de sandálias',2);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (285,10,'Pele de animal selvagem',50);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (286,10,'Roupa comum',3);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (287,10,'Roupa de linho',12);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (288,10,'Roupa intima',1);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (289,10,'Roupa para inverno',20);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (290,10,'Roupa tingida',6);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (291,10,'Sobretudo',30);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (292,10,'Tecido bom (1 metro)',5);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (293,10,'Tecido nobre (1 metro)',50);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (294,10,'Traje nobre (pronto)',300);
--instrumentos musicais 11
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (295,11,'Alaúde',300);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (296,11,'Apito',1);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (297,11,'Atabaque',6);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (298,11,'Balalaica',120);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (299,11,'Bandolim',200);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (300,11,'Banjo',100);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (301,11,'Berrante',10);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (302,11,'Chocalho',3);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (303,11,'Clarineta',30);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (304,11,'Flauta de madeira',12);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (305,11,'Flauta longa de metal',30);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (306,11,'Gaita',60);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (307,11,'Harpa',500);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (308,11,'Pandeirola',5);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (309,11,'Rabeca',80);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (310,11,'Sino',2);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (311,11,'Tambor',10);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (312,11,'Triângulo de metal',3);
--gemas 12				  
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (313,12,'Âmbar, Quartzo, Obsidiana Rotineiro',10);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (314,12,'Ametista, Topázio, Granada, Citrino Fácil',50);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (315,12,'Perola, Opala, Agua Marinha Médio',200);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (316,12,'Opala Preta, Perola Negra, Turmalina Dificil',500);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (317,12,'Turmalina Bicolor, Safira, Esmeralda Muito Dificil',2000);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (318,12,'Rubi e Diamante Absurdo',5000);
INSERT INTO [equipamento](id,id_grupo,nome,valor) VALUES (319,12,'Diamante Vermelho Impossível',50000);

INSERT INTO [equipamento](id,id_grupo,nome,descricao,valor) VALUES (320,5,'Água abençoada (250 ml)', 'Causa 1 de dano na EF ou 4 na EH, reduz em 1 a RM "não acumula". Funciona contra demônios e mortos vivos. Somente Sacerdotes com a magia Sagração de Itens 1, podem abençoar até 1 Litro/Karma', 5);



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



--select * from equipamento where id_grupo =6
--basicas
--select id,nome from Combate a
--inner join
  

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