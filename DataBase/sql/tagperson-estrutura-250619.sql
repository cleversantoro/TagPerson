SELECT 1;
PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE [raca_profissao] (
  [id_raca] int NOT NULL
, [id_profissao] int NOT NULL
, CONSTRAINT [sqlite_autoindex_raca_profissao_1] PRIMARY KEY ([id_raca],[id_profissao])
);

CREATE TABLE [raca] (
  [id] int NOT NULL
, [nome] nvarchar(60) NULL COLLATE NOCASE
, [descricao] ntext NULL
, [image_file] nvarchar(60) NULL COLLATE NOCASE
, [attr_int] int NULL
, [attr_aur] int NULL
, [attr_car] int NULL
, [attr_for] int NULL
, [attr_fis] int NULL
, [attr_agi] int NULL
, [attr_per] int NULL
, [velocidade_inicio] int NULL
, [energia_fisica] int NULL
, [altura_inicio] int NULL
, [peso_inicio] int NULL
, [idade_minima] int NULL
, [idade_maxima] int NULL
, CONSTRAINT [sqlite_autoindex_raca_1] PRIMARY KEY ([id])
);

CREATE TABLE [profissao] (
  [id] int NOT NULL
, [nome] nvarchar(60) NULL COLLATE NOCASE
, [image_file] nvarchar(60) NULL COLLATE NOCASE
, [descricao] ntext NULL
, [equipamentos_iniciais] ntext NULL
, [moedas_cobre] int NULL
, [energia_heroica] int NULL
, [pontos_habilidade] int NULL
, [pontos_arma] int NULL
, [pontos_combate] int NULL
, [penalidade_habilidade_grupo] int NULL
, [especialidade_habilidade] int NULL
, [atributo_magia] int NULL
, [id_magia_grupo] int NULL
, CONSTRAINT [sqlite_autoindex_profissao_1] PRIMARY KEY ([id])
);

CREATE TABLE [personagem_magia] (
  [id_personagem] int NOT NULL
, [id_magia] int NOT NULL
, [nivel] int NULL
, CONSTRAINT [sqlite_autoindex_personagem_magia_1] PRIMARY KEY ([id_personagem],[id_magia])
);

CREATE TABLE [personagem_habilidade_especializacao] (
  [id] int NOT NULL
, [id_personagem] int NULL
, [id_habilidade] int NULL
, [id_habilidade_especializacao] int NULL
, [especializacao] nvarchar(40) NULL COLLATE NOCASE
, [nivel] int NULL
, CONSTRAINT [sqlite_autoindex_personagem_habilidade_especializacao_1] PRIMARY KEY ([id])
);

CREATE TABLE [personagem_habilidade] (
  [id_personagem] int NOT NULL
, [id_habilidade] int NOT NULL
, [nivel] int NULL
, CONSTRAINT [sqlite_autoindex_personagem_habilidade_1] PRIMARY KEY ([id_personagem],[id_habilidade])
);

CREATE TABLE [personagem_equipamento] (
  [id_personagem] int NOT NULL
, [id_equipamento] int NOT NULL
, [quantidade] int NULL
, CONSTRAINT [sqlite_autoindex_personagem_equipamento_1] PRIMARY KEY ([id_personagem],[id_equipamento])
);

CREATE TABLE [personagem_combate] (
  [id_personagem] int NOT NULL
, [id_combate] int NOT NULL
, [nivel] int NULL
, CONSTRAINT [sqlite_autoindex_personagem_combate_1] PRIMARY KEY ([id_personagem],[id_combate])
);

CREATE TABLE [personagem] (
  [id] int NOT NULL
, [nome] nvarchar(100) NULL COLLATE NOCASE
, [jogador] nvarchar(100) NULL COLLATE NOCASE
, [image_file] nvarchar(60) NULL COLLATE NOCASE
, [att_intelecto] int NULL
, [att_aura] int NULL
, [att_carisma] int NULL
, [att_forca] int NULL
, [att_fisico] int NULL
, [att_agilidade] int NULL
, [att_percepcao] int NULL
, [defesa_ativa] int NULL
, [defesa_passiva] int NULL
, [energia_heroica_maxima] int NULL
, [energia_heroica] int NULL
, [energia_fisica] int NULL
, [absorcao] int NULL
, [raca] int NULL
, [profissao] int NULL
, [especializacao] int NULL
, [nivel] int NULL
, [pontos_habilidade] int NULL
, [pontos_combate] int NULL
, [pontos_arma] int NULL
, [pontos_magia] int NULL
, [altura] int NULL
, [peso] int NULL
, [idade] int NULL
, [olhos] nvarchar(60) NULL COLLATE NOCASE
, [cabelo] nvarchar(60) NULL COLLATE NOCASE
, [pele] nvarchar(60) NULL COLLATE NOCASE
, [aparencia] ntext NULL
, [divindade] int NULL
, [classe_social] nvarchar(30) NULL COLLATE NOCASE
, [local_nascimento] int NULL
, [historia] ntext NULL
, [moedas_cobre] int NULL
, [moedas_prata] int NULL
, [moedas_ouro] int NULL
, CONSTRAINT [sqlite_autoindex_personagem_1] PRIMARY KEY ([id])
);

CREATE TABLE [magia_grupo_custo] (
  [id_magia] int NOT NULL
, [id_magia_grupo] int NOT NULL
, [custo] int NULL
, CONSTRAINT [sqlite_autoindex_magia_grupo_custo_1] PRIMARY KEY ([id_magia],[id_magia_grupo])
);

CREATE TABLE [magia_grupo] (
  [id] int NOT NULL
, [id_pai] int NULL
, [nome] nvarchar(100) NULL COLLATE NOCASE
, CONSTRAINT [sqlite_autoindex_magia_grupo_1] PRIMARY KEY ([id])
);

CREATE TABLE [magia] (
  [id] int NOT NULL
, [nome] nvarchar(60) NULL COLLATE NOCASE
, [evocacao] nvarchar(40) NULL COLLATE NOCASE
, [alcance] nvarchar(40) NULL COLLATE NOCASE
, [duracao] nvarchar(60) NULL COLLATE NOCASE
, [descricao] ntext NULL
, [niveis] ntext NULL
, CONSTRAINT [sqlite_autoindex_magia_1] PRIMARY KEY ([id])
);

CREATE TABLE [localidade] (
  [id] int NOT NULL
, [id_pai] int DEFAULT (-1) NULL
, [nome] nvarchar(60) NULL COLLATE NOCASE
, [brasao] nvarchar(60) NULL COLLATE NOCASE
, [nota] ntext NULL
, [autor] nvarchar(120) NULL COLLATE NOCASE
, [x] int DEFAULT (0) NULL
, [y] int DEFAULT (0) NULL
, CONSTRAINT [sqlite_autoindex_localidade_1] PRIMARY KEY ([id])
);

CREATE TABLE [linha_tempo] (
  [id] int NOT NULL
, [id_localidade] int NULL
, [ano] int NULL
, [evento] nvarchar(300) NULL COLLATE NOCASE
, CONSTRAINT [sqlite_autoindex_linha_tempo_1] PRIMARY KEY ([id])
);

CREATE TABLE [habilidade_grupo_custo] (
  [id_habilidade] int NOT NULL
, [id_habilidade_grupo] int NOT NULL
, [custo] int NULL
, CONSTRAINT [sqlite_autoindex_habilidade_grupo_custo_1] PRIMARY KEY ([id_habilidade],[id_habilidade_grupo])
);

CREATE TABLE [habilidade_grupo] (
  [id] int NOT NULL
, [id_pai] int NULL
, [nome] nvarchar(100) NULL COLLATE NOCASE
, CONSTRAINT [sqlite_autoindex_habilidade_grupo_1] PRIMARY KEY ([id])
);

CREATE TABLE [habilidade_especializacao] (
  [id] int NOT NULL
, [id_habilidade] int NULL
, [sugestao] nvarchar(40) NULL COLLATE NOCASE
, CONSTRAINT [sqlite_autoindex_habilidade_especializacao_1] PRIMARY KEY ([id])
);

CREATE TABLE [habilidade] (
  [id] int NOT NULL
, [id_habilidade_grupo] int NULL
, [nome] nvarchar(50) NULL COLLATE NOCASE
, [atributo] nvarchar(3) NULL COLLATE NOCASE
, [teste_nivel] int NULL
, [restrita] int NULL
, [penalidades] nvarchar(50) NULL COLLATE NOCASE
, [tarefas_aperfeicoadas] ntext NULL
, [descricao] ntext NULL
, [niveis] ntext NULL
, [bonus] int DEFAULT (0) NULL
, [possui_especializacao] int DEFAULT (0) NULL
, CONSTRAINT [sqlite_autoindex_habilidade_1] PRIMARY KEY ([id])
);

CREATE TABLE [especializacao] (
  [id] int NOT NULL
, [nome] nvarchar(60) NULL COLLATE NOCASE
, [descricao] ntext NULL
, [id_profissao] int NULL
, [id_magia_grupo] int NULL
, [id_tecnica_grupo] int NULL
, CONSTRAINT [sqlite_autoindex_especializacao_1] PRIMARY KEY ([id])
);

CREATE TABLE [equipamento_grupos] (
  [id] int NOT NULL
, [nome] nvarchar(60) NULL COLLATE NOCASE
, CONSTRAINT [sqlite_autoindex_equipamento_grupos_1] PRIMARY KEY ([id])
);

CREATE TABLE [equipamento_defesa] (
  [id] int NOT NULL
, [id_equipamento] int NULL
, [defesa_base] nvarchar(3) NULL COLLATE NOCASE
, [absorcao] int NULL
, [fisico_minimo] int NULL
, [forca_minima] int NULL
, [P] int NULL
, [A] int NULL
, [E] int NULL
, [M] int NULL
, [H] int NULL
, CONSTRAINT [sqlite_autoindex_equipamento_defesa_1] PRIMARY KEY ([id])
);

CREATE TABLE [equipamento_armas] (
  [id] int NOT NULL
, [id_equipamento] int NULL
, [tipo] nvarchar(50) NULL COLLATE NOCASE
, [custo] int NULL
, [alcance] nvarchar(50) NULL COLLATE NOCASE
, [forca_minima] int NULL
, [bonus] nvarchar(50) NULL COLLATE NOCASE
, [l] int NULL
, [m] int NULL
, [p] int NULL
, [25] int NULL
, [50] int NULL
, [75] int NULL
, [100] int NULL
, [Pq] nvarchar(50) NULL COLLATE NOCASE
, [An] nvarchar(50) NULL COLLATE NOCASE
, [El] nvarchar(50) NULL COLLATE NOCASE
, [ME] nvarchar(50) NULL COLLATE NOCASE
, [Hu] nvarchar(50) NULL COLLATE NOCASE
, CONSTRAINT [sqlite_autoindex_equipamento_armas_1] PRIMARY KEY ([id])
);

CREATE TABLE [equipamento] (
  [id] int NOT NULL
, [id_grupo] int NULL
, [nome] nvarchar(60) NULL COLLATE NOCASE
, [descricao] nvarchar(160) NULL COLLATE NOCASE
, [image_file] nvarchar(50) NULL COLLATE NOCASE
, [valor] int NULL
, [arma] int DEFAULT (0) NULL
, [defesa] int DEFAULT (0) NULL
, [armadura] int DEFAULT (0) NULL
, [escudo] int DEFAULT (0) NULL
, [capacete] int DEFAULT (0) NULL
, CONSTRAINT [sqlite_autoindex_equipamento_1] PRIMARY KEY ([id])
);

CREATE TABLE [divindade] (
  [id] int NOT NULL
, [nome] nvarchar(60) NULL COLLATE NOCASE
, [dominio] nvarchar(100) NULL COLLATE NOCASE
, CONSTRAINT [sqlite_autoindex_divindade_1] PRIMARY KEY ([id])
);

CREATE TABLE [combate_grupo_custo] (
  [id_combate] int NOT NULL
, [id_combate_grupo] int NOT NULL
, [custo] int NULL
, [reducao] int NULL
, CONSTRAINT [sqlite_autoindex_combate_grupo_custo_1] PRIMARY KEY ([id_combate],[id_combate_grupo])
);

CREATE TABLE [combate_grupo] (
  [id] int NOT NULL
, [id_pai] int NULL
, [nome] nvarchar(100) NULL COLLATE NOCASE
, CONSTRAINT [sqlite_autoindex_combate_grupo_1] PRIMARY KEY ([id])
);

CREATE TABLE [combate] (
  [id] int NOT NULL
, [id_habilidade_grupo] int NULL
, [id_categoria] int NULL
, [nome] nvarchar(50) NULL COLLATE NOCASE
, [atributo] nvarchar(3) NULL COLLATE NOCASE
, [efeito] ntext NULL
, [requisitos] ntext NULL
, [obs] ntext NULL
, [quadro_rolagem] ntext NULL
, [aprimoramento] ntext NULL
, [bonus] int NULL
, [possui_especializacao] int NULL
, CONSTRAINT [sqlite_autoindex_combate_1] PRIMARY KEY ([id])
);

CREATE TABLE [categoria] (
  [id] int NOT NULL
, [nome] nvarchar(60) NULL COLLATE NOCASE
, [icon] nvarchar(50) NULL COLLATE NOCASE
, CONSTRAINT [sqlite_autoindex_categoria_1] PRIMARY KEY ([id])
);