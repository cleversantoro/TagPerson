select c.id_pai,a.id_magia_grupo,c.nome as grupo, a.id_magia,b.nome,  a.custo from magia_grupo_custo a 
inner join magia b on a.id_magia = b.id
inner join magia_grupo c on a.id_magia_grupo = c.id


select * from equipamento 
where 
--arma= 1 and
id_grupo = 6

select * from combate

SELECT 
c.id, 
c.nome as descricao, 
ifnull(pc.nivel,0) as nivel, 
cg.custo, 
c.atributo as ajuste,
0 as total,
c.id_categoria,
ct.nome categoria,
ct.icon as icone 
FROM combate c 
inner join combate_grupo_custo cg on c.id = cg.id_combate
left join personagem_combate pc on c.id = pc.id_combate and pc.id_personagem = 9 
inner join categoria ct on c.id_categoria = ct.id
WHERE cg.id_combate_grupo= 1
order by c.nome asc
--and cg.id_combate_grupo <>  1

SELECT 
m.id, 
m.nome as descricao, 
ifnull(pm.nivel,0) as nivel, 
mgc.custo, 
0 as total
FROM magia m 
inner join magia_grupo_custo mgc on m.id = mgc.id_magia
left join personagem_magia pm on m.id = mgc.id_magia and pm.id_personagem = 9 
WHERE mgc.id_magia_grupo= 4
order by m.nome asc

select b.id as id_equipamento, a.id as id_arma, a.arma  from arma a
left join equipamento b on lower(a.Arma) = lower(b.nome)
order by a.id

SELECT * FROM equipamento_armas WHERE id_equipamento=233


SELECT p.id FROM raca_profissao rp, profissao p WHERE p.id=rp.id_profissao AND rp.id_raca=1

select 
a.*
,b.nome
--,c.nome 
from especializacao a
inner join profissao b on a.id_profissao = b.id
--inner join magia_grupo c on a.id_magia_grupo = c.id


select b.nome,c.nome,a.custo from combate_grupo_custo a
inner join combate b on a.id_combate = b.id
inner join combate_grupo c on a.id_combate_grupo = c.id

select 
--lower(a.id_magia),
b.id as id_magia,
--lower(b.nome),
a.id_magia_grupo,
a.custo 
from magia_grupo_custo_new a
inner join magia b on lower(a.id_magia) = lower(b.nome);