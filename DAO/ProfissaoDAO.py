from DataBase.ConexaoSQL import ConexaoSQL
from DAO.GenericDAO import GenericDAO as dao 
from Model.Profissao import Profession

class ProfissaoDAO:

    def get_professions_list():
        return dao.get_list('profissao')

    def get_profession_name(id):
        return dao.get_name(id, 'profissao')

    def get_profession(id):
        cur_con = ConexaoSQL.db_connect()
        cur_sys = cur_con.cursor()

        query = "SELECT * FROM profissao WHERE id=" + str(id)
        cur_sys.execute(query)

        def build_object(row):
            if row is None:
                return None
            else:
                profession = Profession(row[1], row[0])
                profession.image = row[2]
                profession.description = row[3]
                profession.cooper_coins = row[5]
                profession.posessions = row[4].split("|")
                profession.eh = row[6]
                profession.skill_points = row[7]
                profession.weapon_points = row[8]
                profession.combat_points = row[9]
                profession.penalized_skill_group = row[10]
                profession.specialized_skill = row[11]
                profession.attribute_for_magic = row[12]
                profession.spell_group = row[13]
                return profession

        return build_object(cur_sys.fetchone())
