select 
b.bonus,
b.possui_especializacao,
a.id
from habilidade_new a 
left join habilidade b on a.nome = b.nome
order by a.id

select * from habilidade_new where possui_especializacao =1

INSERT INTO [habilidade_grupo] ([id],[id_pai],[nome]) VALUES (1,-1,'Habilidades Comuns');
INSERT INTO [habilidade_grupo] ([id],[id_pai],[nome]) VALUES (2,-1,'Habilidades com Armas');
INSERT INTO [habilidade_grupo] ([id],[id_pai],[nome]) VALUES (3,-1,'Técnicas de Combate');

INSERT INTO [habilidade_grupo] ([id],[id_pai],[nome]) VALUES (1,1,'Profissional');
INSERT INTO [habilidade_grupo] ([id],[id_pai],[nome]) VALUES (2,1,'Subterfúgio');
INSERT INTO [habilidade_grupo] ([id],[id_pai],[nome]) VALUES (3,1,'Manobra');
INSERT INTO [habilidade_grupo] ([id],[id_pai],[nome]) VALUES (4,1,'Influência');
INSERT INTO [habilidade_grupo] ([id],[id_pai],[nome]) VALUES (5,1,'Conhecimento');
INSERT INTO [habilidade_grupo] ([id],[id_pai],[nome]) VALUES (6,1,'Geral');

INSERT INTO [habilidade_grupo] ([id],[id_pai],[nome]) VALUES (10,3,'Academia de Infantaria');
INSERT INTO [habilidade_grupo] ([id],[id_pai],[nome]) VALUES (11,3,'Academia dos Arqueiros');
INSERT INTO [habilidade_grupo] ([id],[id_pai],[nome]) VALUES (12,3,'Academia dos Cavaleiros');
INSERT INTO [habilidade_grupo] ([id],[id_pai],[nome]) VALUES (13,3,'Academia dos Gladiadores');


select * from habilidade_grupo_custo order by id_habilidade_grupo

update habilidade_new set bonus=5	, possui_especializacao=0	where id= 1		;
update habilidade_new set bonus=5	, possui_especializacao=0	where id= 2		;
update habilidade_new set bonus=2	, possui_especializacao=1	where id= 5		;
update habilidade_new set bonus=5	, possui_especializacao=0	where id= 6		;
update habilidade_new set bonus=5	, possui_especializacao=0	where id= 8		;
update habilidade_new set bonus=0	, possui_especializacao=0	where id= 12	;
update habilidade_new set bonus=5	, possui_especializacao=0	where id= 13	;
update habilidade_new set bonus=5	, possui_especializacao=0	where id= 14	;
update habilidade_new set bonus=0	, possui_especializacao=1	where id= 15	;
update habilidade_new set bonus=2	, possui_especializacao=0	where id= 16	;
update habilidade_new set bonus=5	, possui_especializacao=0	where id= 18	;
update habilidade_new set bonus=6	, possui_especializacao=0	where id= 19	;
update habilidade_new set bonus=6	, possui_especializacao=0	where id= 20	;
update habilidade_new set bonus=2	, possui_especializacao=0	where id= 21	;
update habilidade_new set bonus=5	, possui_especializacao=0	where id= 23	;
update habilidade_new set bonus=6	, possui_especializacao=0	where id= 24	;
update habilidade_new set bonus=0	, possui_especializacao=0	where id= 25	;
update habilidade_new set bonus=0	, possui_especializacao=0	where id= 26	;
update habilidade_new set bonus=5	, possui_especializacao=0	where id= 27	;
update habilidade_new set bonus=4	, possui_especializacao=0	where id= 28	;
update habilidade_new set bonus=6	, possui_especializacao=0	where id= 29	;
update habilidade_new set bonus=6	, possui_especializacao=0	where id= 30	;
update habilidade_new set bonus=2	, possui_especializacao=0	where id= 33	;
update habilidade_new set bonus=0	, possui_especializacao=0	where id= 34	;
update habilidade_new set bonus=6	, possui_especializacao=0	where id= 36	;
update habilidade_new set bonus=6	, possui_especializacao=0	where id= 38	;
update habilidade_new set bonus=6	, possui_especializacao=0	where id= 39	;
update habilidade_new set bonus=5	, possui_especializacao=0	where id= 40	;
update habilidade_new set bonus=0	, possui_especializacao=0	where id= 42	;


INSERT INTO [habilidade_especializacao] ([id],[id_habilidade],[sugestao]) VALUES (13,15,'Lantranês');
INSERT INTO [habilidade_especializacao] ([id],[id_habilidade],[sugestao]) VALUES (14,15,'Órquico');
INSERT INTO [habilidade_especializacao] ([id],[id_habilidade],[sugestao]) VALUES (15,15,'Malês meridional');
INSERT INTO [habilidade_especializacao] ([id],[id_habilidade],[sugestao]) VALUES (16,15,'Malês central');
INSERT INTO [habilidade_especializacao] ([id],[id_habilidade],[sugestao]) VALUES (17,15,'Malês setentrional');
INSERT INTO [habilidade_especializacao] ([id],[id_habilidade],[sugestao]) VALUES (18,15,'Élfico');
