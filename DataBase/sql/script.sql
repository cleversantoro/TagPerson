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

id_equipamento	id_arma	Arma
		1			Combate Desarmado
213		2			Manopla
186		3			Boleadeira
222		4			Rede
194		5			Faca
220		6			Punhal
187		7			Bumerangue
188		8			Bumerangue de Corte
218		9			Funda Projétil de Pedra
219		10			Funda Projétil de Metal
210		11			Malho
189		12			Cajado
217		13			Porrete
197		14			Gládio
221		15			Rapieira
190		16			Cimitarra
192		17			Espada
223		18			Sabre Élfico
206		19			Machado
205		20			Machadinha
207		21			Machado Crescente
208		22			Machado de Batalha
191		23			Clava
203		24			Maça
215		25			Martelo de Guerra
204		26			Maça de Armas
212		27			Mangual Leve
181		28			Arco Simples
178		29			Arco Composto
201		30			Lança Leve
182		31			Arpão
199		32			Lança de Guarda
202		33			Lança Pesada
224		34			Tridente
193		35			Espada de Mão e Meia
		36			Espada (Com Duas Mãos)
216		37			Montante
209		38			Machado de Guerra
		39			Machado (Com Duas Mãos)
183		40			Axa de Armas
211		41			Mangual
		42			Mangual (Com Duas Mãos)
214		43			Marreta de Guerra
200		44			Lança de Justa
198		45			Lança de Cavalaria
179		46			Arco de Guerra
180		47			Arco Longo Élfico
184		48			Besta
185		49			Besta Pesada

id_equipamento	id_arma	nome

	1	Nada
225	2	Couro Leve
226	3	Couro Rígido
227	4	Cota de Malha Parcial
228	5	Cota de Malha Completa
229	6	Couraça Parcial
230	7	Couraça Completa
233	8	Escudo Pequeno
234	9	Escudo Grande
235	10	Escudo de Torre
236	11	Elmo Aberto
237	12	Elmo Fechadoupdate defesa set id_equipamento =0	 	where id= 1;
update defesa set id_equipamento =225	where id= 2;
update defesa set id_equipamento =226	where id= 3;
update defesa set id_equipamento =227	where id= 4;
update defesa set id_equipamento =228	where id= 5;
update defesa set id_equipamento =229	where id= 6;
update defesa set id_equipamento =230	where id= 7;
update defesa set id_equipamento =233	where id= 8;
update defesa set id_equipamento =234	where id= 9;
update defesa set id_equipamento =235	where id= 10;
update defesa set id_equipamento =236	where id= 11;
update defesa set id_equipamento =237	where id= 12;



--update arma set id_iquipamento = 	      where id= 1  ;
update arma set id_equipamento = 213	  where id= 2  ;
update arma set id_equipamento = 186	  where id= 3  ;
update arma set id_equipamento = 222	  where id= 4  ;
update arma set id_equipamento = 194	  where id= 5  ;
update arma set id_equipamento = 220	  where id= 6  ;
update arma set id_equipamento = 187	  where id= 7  ;
update arma set id_equipamento = 188	  where id= 8  ;
update arma set id_equipamento = 218	  where id= 9  ;
update arma set id_equipamento = 219	  where id= 10 ;
update arma set id_equipamento = 210	  where id= 11 ;
update arma set id_equipamento = 189	  where id= 12 ;
update arma set id_equipamento = 217	  where id= 13 ;
update arma set id_equipamento = 197	  where id= 14 ;
update arma set id_equipamento = 221	  where id= 15 ;
update arma set id_equipamento = 190	  where id= 16 ;
update arma set id_equipamento = 192	  where id= 17 ;
update arma set id_equipamento = 223	  where id= 18 ;
update arma set id_equipamento = 206	  where id= 19 ;
update arma set id_equipamento = 205	  where id= 20 ;
update arma set id_equipamento = 207	  where id= 21 ;
update arma set id_equipamento = 208	  where id= 22 ;
update arma set id_equipamento = 191	  where id= 23 ;
update arma set id_equipamento = 203	  where id= 24 ;
update arma set id_equipamento = 215	  where id= 25 ;
update arma set id_equipamento = 204	  where id= 26 ;
update arma set id_equipamento = 212	  where id= 27 ;
update arma set id_equipamento = 181	  where id= 28 ;
update arma set id_equipamento = 178	  where id= 29 ;
update arma set id_equipamento = 201	  where id= 30 ;
update arma set id_equipamento = 182	  where id= 31 ;
update arma set id_equipamento = 199	  where id= 32 ;
update arma set id_equipamento = 202	  where id= 33 ;
update arma set id_equipamento = 224	  where id= 34 ;
update arma set id_equipamento = 193	  where id= 35 ;
update arma set id_equipamento = 193	  where id= 36 ;
update arma set id_equipamento = 216	  where id= 37 ;
update arma set id_equipamento = 209	  where id= 38 ;
update arma set id_equipamento = 209      where id= 39 ;
update arma set id_equipamento = 183	  where id= 40 ;
update arma set id_equipamento = 211	  where id= 41 ;
update arma set id_equipamento = 211      where id= 42 ;
update arma set id_equipamento = 214	  where id= 43 ;
update arma set id_equipamento = 200	  where id= 44 ;
update arma set id_equipamento = 198	  where id= 45 ;
update arma set id_equipamento = 179	  where id= 46 ;
update arma set id_equipamento = 180	  where id= 47 ;
update arma set id_equipamento = 184	  where id= 48 ;
update arma set id_equipamento = 185	  where id= 49 ;