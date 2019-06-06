from DataBase.ConexaoSQL import ConexaoSQL
from DAO.GenericDAO import GenericDAO as dao
from Model.Magia import Spell

cur_con = ConexaoSQL.db_connect()
cur_sys = cur_con.cursor()
class MagiaDAO:

    def get_spells_list():
        return dao.get_list('magia')

    def get_spell_name(id):
        return dao.get_name(id, 'magia')

    def get_spell(id):
        query = "SELECT * FROM magia WHERE id=" + str(id)
        cur_sys.execute(query)

        def build_object(row):
            if row is None:
                return None
            spell = Spell(row[1],row[0])
            spell.description = row[2]
            spell.evocation = row[3]
            spell.range = row[4]
            spell.duration = row[5]
            spell.level = row[6]
            return spell

        return build_object(cur_sys.fetchone())

    def get_spell_group_parents():
        query = "SELECT id, nome FROM magia_grupo "\
                "WHERE id_pai=-1"
        cur_sys.execute(query)
        return cur_sys.fetchall()

    def get_spell_group_children(parent_id):
        query = "SELECT id, nome FROM magia_grupo "\
                "WHERE id_pai=" + str(parent_id)
        cur_sys.execute(query)
        return cur_sys.fetchall()

    def get_spells_from_group(spellgroup_id):
        query = "SELECT s.id, sg.custo FROM magia s, magia_magia_grupo sg "\
                "WHERE s.id=sg.id_magia AND sg.id_magia_grupo=" + \
                str(spellgroup_id)
        cur_sys.execute(query)
        result = cur_sys.fetchall()

        return [(id, MagiaDAO.get_spell(id), cost) for id, cost in result]
