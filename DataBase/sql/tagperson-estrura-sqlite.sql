CREATE TABLE [localidade] (
  [id] int  NOT NULL
, [id_pai] int DEFAULT -1  NULL
, [nome] nvarchar(60)  NULL
, [brasao] nvarchar(60)  NULL
, [nota] ntext NULL
, [autor] nvarchar(120)  NULL
, [x] int DEFAULT 0  NULL
, [y] int DEFAULT 0  NULL
, CONSTRAINT [PK_localidade] PRIMARY KEY ([id])
);

CREATE TABLE [linha_tempo] (
  [id] int  NOT NULL
, [id_localidade] int  NULL
, [ano] int  NULL
, [evento] nvarchar(300)  NULL
, CONSTRAINT [PK_linha_tempo] PRIMARY KEY ([id])
);

CREATE TABLE [divindade] (
  [id] int  NOT NULL
, [nome] nvarchar(60)  NULL
, [dominio] nvarchar(100)  NULL
, CONSTRAINT [PK_divindade] PRIMARY KEY ([id])
);

CREATE TABLE [categoria] (
  [id] int  NOT NULL
, [nome] nvarchar(60)  NULL
, [icon] nvarchar(50)  NULL
, CONSTRAINT [PK_categoria] PRIMARY KEY ([id])
);

CREATE TABLE [especializacao] (
  [id] int  NOT NULL
, [nome] nvarchar(60)  NULL
, [descricao] ntext NULL
, [id_profissao] int  NULL
, [id_magia_grupo] int  NULL
, [id_tecnica_grupo] int  NULL
, CONSTRAINT [PK_especializacao] PRIMARY KEY ([id])
);

CREATE TABLE [raca] (
  [id] int  NOT NULL
, [nome] nvarchar(60)  NULL
, [image_file] nvarchar(60)  NULL
, [attr_int] int  NULL
, [attr_aur] int  NULL
, [attr_car] int  NULL
, [attr_for] int  NULL
, [attr_fis] int  NULL
, [attr_agi] int  NULL
, [attr_per] int  NULL
, [velocidade_inicio] int  NULL
, [energia_fisica] int  NULL
, [altura_inicio] int  NULL
, [peso_inicio] int  NULL
, [idade_minima] int  NULL
, [idade_maxima] int  NULL
, CONSTRAINT [PK_raca] PRIMARY KEY ([id])
);

CREATE TABLE [profissao] (
  [id] int  NOT NULL
, [nome] nvarchar(60)  NULL
, [image_file] nvarchar(60)  NULL
, [descricao] ntext NULL
, [moedas_cobre] int  NULL
, [energia_heroica] int  NULL
, [pontos_habilidade] int  NULL
, [pontos_arma] int  NULL
, [pontos_combate] int  NULL
, [penalidade_habilidade_grupo] int  NULL
, [especialidade_habilidade] int  NULL
, [atributo_magia] int  NULL
, [id_magia_grupo] int  NULL
, CONSTRAINT [PK_profissao] PRIMARY KEY ([id])
);

CREATE TABLE [raca_profissao] (
  [id_raca] int  NOT NULL
, [id_profissao] int  NOT NULL
, CONSTRAINT [PK_raca_profissao] PRIMARY KEY ([id_raca],[id_profissao])
);

CREATE TABLE [personagem_magia] (
  [id_personagem] int  NOT NULL
, [id_magia] int  NOT NULL
, [nivel] int  NULL
, CONSTRAINT [PK_personagem_magia] PRIMARY KEY ([id_personagem],[id_magia])
);

CREATE TABLE [personagem_combate] ( 
  [id_personagem] int  NOT NULL 
, [id_combate] int  NOT NULL 
, [nivel] int  NULL 
, CONSTRAINT [PK_personagem_combate] PRIMARY KEY ([id_personagem],[id_combate]) 
);

CREATE TABLE [personagem_habilidade_especializacao] (
  [id] int  NOT NULL
, [id_personagem] int  NULL
, [id_habilidade] int  NULL
, [especializacao] nvarchar(40)  NULL
, [nivel] int  NULL
, CONSTRAINT [PK_personagem_habilidade_especializacao] PRIMARY KEY ([id])
);

CREATE TABLE [personagem_habilidade] (
  [id_personagem] int  NOT NULL
, [id_habilidade] int  NOT NULL
, [nivel] int  NULL
, CONSTRAINT [PK_personagem_habilidade] PRIMARY KEY ([id_personagem],[id_habilidade])
);

CREATE TABLE [personagem_equipamento] (
  [id_personagem] int  NOT NULL
, [id_equipamento] int  NOT NULL
, [quantidade] int  NULL
, CONSTRAINT [PK_personagem_equipamento] PRIMARY KEY ([id_personagem],[id_equipamento])
);

CREATE TABLE [personagem] (
  [id] int  NOT NULL
, [nome] nvarchar(100)  NULL
, [jogador] nvarchar(100)  NULL
, [image_file] nvarchar(60)  NULL
, [att_intelecto] int  NULL
, [att_aura] int  NULL
, [att_carisma] int  NULL
, [att_forca] int  NULL
, [att_fisico] int  NULL
, [att_agilidade] int  NULL
, [att_percepcao] int  NULL
, [defesa_ativa] int  NULL
, [defesa_passiva] int  NULL
, [energia_heroica_maxima] int  NULL
, [energia_heroica] int  NULL
, [energia_fisica] int  NULL
, [absorcao] int  NULL
, [raca] int  NULL
, [profissao] int  NULL
, [especializacao] int  NULL
, [nivel] int  NULL
, [pontos_habilidade] int  NULL
, [pontos_combate] int  NULL
, [pontos_arma] int  NULL
, [pontos_magia] int  NULL
, [altura] int  NULL
, [peso] int  NULL
, [idade] int  NULL
, [olhos] nvarchar(60)  NULL
, [cabelo] nvarchar(60)  NULL
, [pele] nvarchar(60)  NULL
, [aparencia] ntext NULL
, [divindade] int  NULL
, [classe_social] nvarchar(30)  NULL
, [local_nascimento] int  NULL
, [historia] ntext NULL
, [moedas_cobre] int  NULL
, [moedas_prata] int  NULL
, [moedas_ouro] int  NULL
, CONSTRAINT [PK_personagem] PRIMARY KEY ([id])
);

CREATE TABLE [magia] (
  [id] int  NOT NULL
, [nome] nvarchar(60)  NULL
, [descricao] ntext NULL
, [evocacao] nvarchar(40)  NULL
, [alcance] nvarchar(40)  NULL
, [duracao] nvarchar(60)  NULL
, [Nivel] ntext NULL
, CONSTRAINT [PK_magia] PRIMARY KEY ([id])
);

CREATE TABLE [magia_grupo] (
  [id] int  NOT NULL
, [id_pai] int  NULL
, [nome] nvarchar(100)  NULL
, CONSTRAINT [PK_magia_grupo] PRIMARY KEY ([id])
);

CREATE TABLE [magia_grupo_custo] (
  [id_magia] int  NOT NULL
, [id_magia_grupo] int  NOT NULL
, [custo] int  NULL
, CONSTRAINT [PK_magia_grupo_custo] PRIMARY KEY ([id_magia],[id_magia_grupo])
);

CREATE TABLE [habilidade] (
  [id] int  NOT NULL
, [nome] nvarchar(100)  NULL
, [descricao] ntext NULL
, [bonus] int  NULL
, [possui_especializacao] int  NULL
, CONSTRAINT [PK_habilidade] PRIMARY KEY ([id])
);

CREATE TABLE [habilidade_new](
  [id] int NOT NULL UNIQUE 
, [id_habilidade_grupo] int 
, [nome] nvarchar(50) 
, [atributo] nvarchar(3) 
, [teste_nivel] int 
, [restrita] int 
, [penalidades] nvarchar(50) 
, [tarefas_aperfeicoadas] ntext  NULL 
, [descricao] ntext  NULL 
, [niveis] ntext  NULL 
, [bonus] int 
, [possui_especializacao] int
, CONSTRAINT [PK_habilidade_new] PRIMARY KEY ([id]) 
);

CREATE TABLE [habilidade_grupo] (
  [id] int  NOT NULL
, [id_pai] int  NULL
, [nome] nvarchar(100)  NULL
, CONSTRAINT [PK_habilidade_habilidade_grupo] PRIMARY KEY ([id])
);

CREATE TABLE [habilidade_grupo_custo] (
  [id_habilidade] int  NOT NULL
, [id_habilidade_grupo] int  NOT NULL
, [custo] int  NULL
, CONSTRAINT [PK_habilidade_grupo_custo] PRIMARY KEY ([id_habilidade],[id_habilidade_grupo])
);

CREATE TABLE [habilidade_especializacao] (
  [id] int  NOT NULL
, [id_habilidade] int  NULL
, [sugestao] nvarchar(40)  NULL
, CONSTRAINT [PK_habilidade_especializacao] PRIMARY KEY ([id])
);

CREATE TABLE [combate] (
  [id] int  NOT NULL 
, [id_habilidade_grupo] int  NULL
, [id_categoria] int  NULL
, [nome] nvarchar(50)  NULL
, [atributo] nvarchar(3)  NULL
, [efeito] ntext  NULL
, [requisitos] ntext  NULL
, [obs] ntext  NULL
, [quadro_rolagem] ntext  NULL
, [aprimoramento] ntext  NULL
, [bonus] int  NULL
, [possui_especializacao] int  NULL
, CONSTRAINT [PK_combate] PRIMARY KEY ([id]) 
);

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

CREATE TABLE [equipamento] (
  [id] int  NOT NULL
, [id_grupo] int  NULL
, [nome] nvarchar(60)  NULL
, [descricao] nvarchar(160)  NULL
, [image_file] nvarchar(50)  NULL
, [valor] int  NULL
, [arma] int  NULL
, [defesa] int  NULL
, [armadura] int  NULL
, [escudo] int  NULL
, [capacete] int  NULL
, CONSTRAINT [PK_equipamento] PRIMARY KEY ([id])
);

CREATE TABLE [equipamento_grupos] (
  [id] int  NOT NULL
, [nome] nvarchar(60)  NULL
, CONSTRAINT [PK_equipamento_grupos] PRIMARY KEY ([id])
);

CREATE TABLE [equipamento_defesa] (
  [id] int  NOT NULL
, [tipo] nvarchar(10)  NULL
, [valor_inicio] int  NULL
, [absorcao] int  NULL
, CONSTRAINT [PK_equipamento_defesa] PRIMARY KEY ([id])
);

CREATE TABLE [equipamento_armas] (
  [id] int  NOT NULL
, [id_habilidade] int  NULL
, [minima_forca] int  NULL
, [minima_dano] int  NULL
, [l0] int  NULL
, [m0] int  NULL
, [p0] int  NULL
, [alcance] int  NULL
, CONSTRAINT [PK_equipamento_armas] PRIMARY KEY ([id])
);

