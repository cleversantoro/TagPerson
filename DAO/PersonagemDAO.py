from DataBase.ConexaoSQL import ConexaoSQL
from DAO.GenericDAO import GenericDAO as dao
from Model.Personagem import Persona
from DAO.RacaDAO import RacaDAO as racedao
from DAO.ProfissaoDAO import ProfissaoDAO as profidao
from DAO.EspecialidadeDAO import EspecialidadeDAO as especdao
from DAO.LocalidadeDAO import LocalidadeDAO as locdao
from DAO.EquipamentoDAO import EquipamentoDAO as equipdao
from Helpers.constantes import const as data
from Helpers.helpers import utils
import os

conn_usr = ConexaoSQL.db_connect()
cur_usr = conn_usr.cursor()

class PersonagemDAO:

    def get_persona_list():
        query = "SELECT id, nome, raca, profissao, nivel FROM personagem"
        cursor = cur_usr.execute(query)
        return cursor.fetchall()

    def get_players_names():
        query = "SELECT jogador FROM personagem"
        cur_usr.execute(query)
        result = set() # evita entradas repetidas
        for row in cur_usr.fetchall():
            if row[0] is not None:
                result.add(row[0])
        return list(result)

    def get_persona(id):
        query = "SELECT * FROM personagem WHERE id=" + str(id)
        cur_usr.execute(query)

        def build_object(row):
            if row is None:
                return None
            persona = Persona(row[1], row[0])
            persona.player = row[2]
            persona.avatar_file = row[3]
            persona.attributes[data.INT] = row[4]
            persona.attributes[data.AUR] = row[5]
            persona.attributes[data.CAR] = row[6]
            persona.attributes[data.FOR] = row[7]
            persona.attributes[data.FIS] = row[8]
            persona.attributes[data.AGI] = row[9]
            persona.attributes[data.PER] = row[10]

            persona.race = racedao.get_race(row[17])
            raca = persona.race.__str__()
            persona.profession = profidao.get_profession(row[18])
            profissao = persona.profession.__str__()
            persona.specialization = especdao.get_specialization(row[19])
            persona.xp = row[39]
            persona.level = utils.get_level(persona.xp)

            persona.active_defense = row[11]
            persona.passive_defense = row[12]
            persona.max_eh = row[13]
            persona.eh = row[14]
            persona.ef = row[15]
            persona.absorption = row[16]

            persona.skill_points = row[21]
            persona.weapon_points = row[22]
            persona.combat_points = row[23]
            persona.magic_points = row[24]

            persona.height = row[25]
            persona.weight = row[26]
            persona.age = row[27]

            persona.eyes = row[28]
            persona.hair = row[29]
            persona.skin = row[30]
            persona.appearance = row[31]

            persona.god = row[32]
            persona.social_class = row[33]
            persona.homeland = locdao.get_place(row[34])
            persona.history = row[35]
            #persona.goals = row[36]

            persona.copper_coins = row[36]#data.COMBAT_EQUIP]
            persona.silver_coins = row[37]#data.COMBAT_EQUIP+1]
            persona.gold_coins = row[38]#data.COMBAT_EQUIP+2]

            persona.skills, persona.skills_specs = PersonagemDAO.get_persona_skills(id)
            persona.spells = PersonagemDAO.get_persona_spells(id)
            persona.combat_skills = PersonagemDAO.get_persona_combat_skills(id)
            #persona.equipment = PersonagemDAO.get_persona_equipment(id)

            i = 0
            y = 0
            for x in PersonagemDAO.get_persona_equipment(id):
                equip = equipdao.get_equipment_item(x) 

                if( equip.itemtype == 'armour'):
                    persona.combat_equip[0] = equip
                elif(equip.itemtype == 'helmet'):
                    persona.combat_equip[1] = equip
                elif(equip.itemtype == 'shield'):
                    persona.combat_equip[2] = equip
                elif(equip.itemtype == 'weapon'):
                    persona.combat_weapon[y] = equip
                    y += 1
                elif(equip.itemtype == 'item'):
                    persona.equipment[i] = equip
                    i += 1

            return persona

        return build_object(cur_usr.fetchone())

    def __get_persona_something(persona_id, table, columns):
        query = "SELECT %s FROM %s WHERE id_personagem=%s" %\
                (columns, table, persona_id)
        cur_usr.execute(query)
        result = cur_usr.fetchall()
        dic = {}
        for key, value in result:
            dic[key] = value
        return dic

    def get_persona_skills(persona_id):
        # Habilidades comuns
        skills = PersonagemDAO.__get_persona_something(persona_id, 'personagem_habilidade','id_habilidade, nivel')

        # Especializacoes
        query = "SELECT id_habilidade, especializacao, nivel FROM "\
                "personagem_habilidade_especializacao WHERE id_personagem=%s" % persona_id
        cur_usr.execute(query)
        result = cur_usr.fetchall()
        specs = {}
        for skill_id, specialization, level in result:
            if skill_id not in specs:
                specs[skill_id] = []
            specs[skill_id].append((specialization, level))

        return (skills, specs)

    def get_combat_persona(persona_id,combat_group_id):
        query = "SELECT c.id, c.nome as descricao, ifnull(pc.nivel,0) as nivel, cg.custo, c.atributo as ajuste, "\
                " 0 as total, c.id_categoria, ct.nome categoria, ct.icon as icone "\
                " FROM combate c "\
                " inner join combate_grupo_custo cg on c.id = cg.id_combate "\
                " left join personagem_combate pc on c.id = pc.id_combate and pc.id_personagem ={} " \
                " inner join categoria ct on c.id_categoria = ct.id "\
                " WHERE cg.id_combate_grupo={} "\
                " ORDER BY c.nome asc".format(persona_id,combat_group_id) 

        cursor  = cur_usr.execute(query)
        return cursor.fetchall()

    def get_spell_persona(persona_id,spell_group_id):
        query = " SELECT m.id, m.nome as descricao, ifnull(pm.nivel,0) as nivel, mgc.custo, 0 as total "\
                " FROM magia m "\
                " inner join magia_grupo_custo mgc on m.id = mgc.id_magia "\
                " left join personagem_magia pm on m.id = pm.id_magia and pm.id_personagem = {} "\
                " WHERE mgc.id_magia_grupo= {} "\
                " order by m.nome asc ".format(persona_id,spell_group_id) 

        cursor  = cur_usr.execute(query)
        return cursor.fetchall()

    def get_skills_persona(persona_id,skills_group_id):
        query = " SELECT m.id, m.nome as descricao, "\
                " CASE m.restrita "\
                "     WHEN 1 THEN 'SIM' "\
                "     WHEN 0 THEN '' "\
                " END as restrito, ifnull(pm.nivel,0) as nivel, mgc.custo, "\
                " m.atributo as ajuste, 0 as total "\
                " FROM habilidade m "\
                " inner join habilidade_grupo_custo mgc on m.id = mgc.id_habilidade "\
                " left join personagem_habilidade pm on m.id = pm.id_habilidade and pm.id_personagem = {} "\
                " WHERE mgc.id_habilidade_grupo= {} "\
                " order by m.nome asc ".format(persona_id,skills_group_id)

        cursor  = cur_usr.execute(query)
        return cursor.fetchall()

    def get_persona_combat_skills(persona_id):
        return PersonagemDAO.__get_persona_something(persona_id, 'personagem_combate','id_combate, nivel')

    def get_persona_spells(persona_id):
        return PersonagemDAO.__get_persona_something(persona_id, 'personagem_magia','id_magia, nivel')
 
    def get_persona_equipment(persona_id):
        return PersonagemDAO.__get_persona_something(persona_id, 'personagem_equipamento','id_equipamento, quantidade')

    def save_persona(persona):
        fields = {}
        fields['nome'] = persona.name
        fields['jogador'] = persona.player
        fields['image_file'] = persona.avatar_file
        fields['att_intelecto'] = persona.attributes[data.INT]
        fields['att_aura'] = persona.attributes[data.AUR]
        fields['att_carisma'] = persona.attributes[data.CAR]
        fields['att_forca'] = persona.attributes[data.FOR]
        fields['att_fisico'] = persona.attributes[data.FIS]
        fields['att_agilidade'] = persona.attributes[data.AGI]
        fields['att_percepcao'] = persona.attributes[data.PER]
        fields['defesa_ativa'] = persona.active_defense
        fields['defesa_passiva'] = persona.passive_defense
        fields['energia_heroica_maxima'] = persona.max_eh
        fields['energia_heroica'] = persona.eh
        fields['energia_fisica'] = persona.get_max_ef()
        fields['absorcao'] = persona.absorption
        fields['raca'] = persona.race.id
        fields['profissao'] = persona.profession.id
        fields['especializacao'] = persona.specialization
        fields['nivel'] = persona.level
        fields['pontos_habilidade'] = persona.skill_points
        fields['pontos_combate'] = persona.combat_points
        fields['pontos_arma'] = persona.weapon_points
        fields['pontos_magia'] = persona.magic_points
        fields['experiencia'] = persona.xp
        fields['idade'] = persona.age
        fields['altura'] = persona.height
        fields['peso'] = persona.weight
        fields['olhos'] = persona.eyes
        fields['cabelo'] = persona.hair
        fields['pele'] = persona.skin
        fields['aparencia'] = persona.appearance
        fields['divindade'] = persona.god
        fields['classe_social'] = persona.social_class
        fields['historia'] = persona.history
        #fields['goals'] = persona.goals
        #fields['melee_weapon'] = persona.get_melee_weapon()
        #fields['ranged_weapon'] = persona.get_ranged_weapon()
        #fields['armour'] = persona.get_armour()
        #fields['helmet'] = persona.get_helmet()
        #fields['shield'] = persona.get_shield()
        fields['moedas_cobre'] = persona.copper_coins
        fields['moedas_prata'] = persona.silver_coins
        fields['moedas_ouro'] = persona.gold_coins

        if persona.specialization is not None:
            fields['especializacao'] = persona.specialization.id
        else:
            fields['especializacao'] = -1

        try:
            fields['local_nascimento'] = persona.homeland.id
        except:
            fields['local_nascimento'] = -1

        if persona.id == -1:
            persona.id = PersonagemDAO.__insert_persona(fields)
        else:
            PersonagemDAO.__update_persona(persona.id, fields)

        PersonagemDAO.save_persona_spells(persona)
        PersonagemDAO.save_persona_skills(persona)
        PersonagemDAO.save_persona_equipment(persona)
        PersonagemDAO.save_persona_combat_skills(persona)

    def __insert_persona(fields):
        field_list = ', '.join([f for f in fields.keys() if fields[f] is not None])

        data_list = []
        for field in fields.keys():
            data = fields[field]
            if type(data) in (int, float):
                data_list.append(str(data))
            elif type(data) in (str, UnicodeError):
                data_list.append('"%s"' % data)

        data = ', '.join(data_list)

        query = 'INSERT INTO personagem (%s) VALUES (%s)' % (field_list, data)

        cur_usr.execute(query)
        conn_usr.commit()
        cur_usr.execute('SELECT last_insert_rowid()')

        return cur_usr.fetchone()[0]

    def __update_persona(persona_id, fields):
        data_list = []
        for field in fields.keys():
            data = fields[field]
            if type(data) in (int, float):
                data_list.append('%s=%d' % (field, data))
            elif type(data) in (str, UnicodeError):
                data_list.append('%s="%s"' % (field, data))

        data = ', '.join(data_list)
        query = 'UPDATE personagem SET %s WHERE id=%d' % (data, persona_id)

        cur_usr.execute(query)
        conn_usr.commit()

    def save_persona_spells(persona):
        PersonagemDAO.__save_persona_list(persona.id, persona.spells, 'magia')

    def save_persona_combat_skills(persona):
        PersonagemDAO.__save_persona_list(persona.id, persona.combat_skills, 'combate')

    def save_persona_skills(persona):
        PersonagemDAO.__save_persona_list(persona.id, persona.skills, 'habilidade')

    def save_persona_equipment(persona):
        PersonagemDAO.__save_persona_list(persona.id, persona.equipment, 'equipamento', 'quantidade')

    def __save_persona_list(persona_id, itemlist, listname,valuecol='nivel'):

        def _item_exists(item_id):
            query = ' SELECT count(*) FROM personagem_%s '\
                    ' WHERE id_personagem=%d AND id_%s=%d' %\
                    (listname, persona_id, listname, item_id)
            cur_usr.execute(query)
            return cur_usr.fetchone()[0] > 0

        for item_id in itemlist:
            value = itemlist[item_id]

            if _item_exists(item_id):
                query = ' UPDATE personagem_%s SET '\
                        ' %s=%d WHERE id_personagem=%d ' \
                        ' AND id_%s=%d' % \
                        (listname, valuecol, value, persona_id, listname, item_id)
            else:
                query = 'INSERT INTO personagem_%s '\
                        '(id_personagem, id_%s, %s) '\
                        'VALUES (%d, %d, %d)' % \
                        (listname, listname, valuecol,
                        persona_id, item_id, value)

            cur_usr.execute(query)
            query = 'DELETE FROM personagem_%s WHERE %s=0' % \
                    (listname, valuecol)
            cur_usr.execute(query)
            conn_usr.commit()
