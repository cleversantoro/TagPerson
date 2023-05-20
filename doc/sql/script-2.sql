select 
a.id as idcombate, 
b.id as idhabilidade,
a.nome,
b.nome,
b.bonus,
b.possui_especializacao
from Combate a
inner join habilidade b on a.nome = b.nome;

--update combate set bonus= , possui_especializacao= where id= 
update combate set bonus=-1	, possui_especializacao=0 where id= 2	;		
update combate set bonus=-1	, possui_especializacao=0 where id= 4	;		
update combate set bonus=6	, possui_especializacao=0 where id= 6	;		
update combate set bonus=5	, possui_especializacao=0 where id= 7	;		
update combate set bonus=-1	, possui_especializacao=0 where id= 10	;		
update combate set bonus=-1	, possui_especializacao=0 where id= 11	;		
update combate set bonus=-1	, possui_especializacao=0 where id= 12	;		
update combate set bonus=5	, possui_especializacao=0 where id= 14	;		
update combate set bonus=5	, possui_especializacao=0 where id= 15	;		
update combate set bonus=-1	, possui_especializacao=0 where id= 16	;		
update combate set bonus=6	, possui_especializacao=0 where id= 17	;		
update combate set bonus=-1	, possui_especializacao=0 where id= 23	;		
update combate set bonus=6	, possui_especializacao=0 where id= 25	;		
update combate set bonus=5	, possui_especializacao=0 where id= 29	;		
update combate set bonus=-1	, possui_especializacao=0 where id= 34	;		
update combate set bonus=-1	, possui_especializacao=0 where id= 35	;		
update combate set bonus=5	, possui_especializacao=0 where id= 37	;		
update combate set bonus=-1	, possui_especializacao=0 where id= 38	;		
update combate set bonus=2	, possui_especializacao=0 where id= 42	;		
update combate set bonus=-1	, possui_especializacao=0 where id= 44	;		
update combate set bonus=-1	, possui_especializacao=0 where id= 45	;		
update combate set bonus=4	, possui_especializacao=0 where id= 54	;		
update combate set bonus=4	, possui_especializacao=0 where id= 54	;		
update combate set bonus=6	, possui_especializacao=0 where id= 60	;		

select 
a.id as id_old, 
b.id as id_new, 
b.nome,
a.bonus,
a.possui_especializacao
from habilidade a
inner join habilidade_new b on a.nome = b.nome


select * from habilidade_grupo where id= 3 or id_pai =3;

select a.id_habilidade,a.id_habilidade_grupo,b.nome,c.nome as nome_academia, a.custo, b.bonus,b.possui_especializacao 
from habilidade_grupo_custo a 
inner join habilidade b on a.id_habilidade = b.id
inner join habilidade_grupo c on a.id_habilidade_grupo = c.id_pai
where a.id_habilidade_grupo = 3;

insert into combate_grupo (id,id_pai,nome) values (1,-1,'Técnicas de Combate');
insert into combate_grupo (id,id_pai,nome) values (2,1,'Academia de Infantaria');
insert into combate_grupo (id,id_pai,nome) values (3,1,'Academia dos Arqueiros');
insert into combate_grupo (id,id_pai,nome) values (4,1,'Academia dos Cavaleiros');
insert into combate_grupo (id,id_pai,nome) values (5,1,'Academia dos Gladiadores');
insert combate_grupo_custo () values ()


select 
a.id_habilidade,
d.id as id_habilidade_new,
a.id_habilidade_grupo,
b.nome,
c.nome as nome_academia, 
a.custo, 
b.bonus,
b.possui_especializacao 
from habilidade_grupo_custo a 
inner join habilidade b on a.id_habilidade = b.id
inner join habilidade_grupo c on a.id_habilidade_grupo = c.id_pai
left join combate d on b.nome = d.nome
--where a.id_habilidade_grupo = 3;

