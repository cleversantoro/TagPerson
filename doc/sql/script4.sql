select * from habilidade;
select * from habilidade_new;

select * from personagem;

select id,nome,* from combate;
select * from magia;
select * from magia_grupo;
select * from magia_magia_grupo order by id_magia_grupo;

select * from habilidade_new order by id_habilidade_grupo;

select * from habilidade_grupo;
select * from habilidade_habilidade_grupo;


select c.id,c.nome,a.id as id_old from habilidade a 
join combate c on a.nome = c.nome
order by c.nome;



select c.id,c.nome,a.bonus,a.possui_especializacao from habilidade a 
join habilidade_habilidade_grupo b on a.id = b.id_habilidade
join habilidade_new c on a.nome = c.nome
--join combate c on a.nome = c.nome
where b.id_habilidade_grupo  in(4,5,6,7,8,9)
order by c.nome;



