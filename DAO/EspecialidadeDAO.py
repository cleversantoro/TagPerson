from DataBase.ConexaoSQL import ConexaoSQL
from DAO.GenericDAO import GenericDAO as dao
from Model.Especializacao import Specialization


cur_con = ConexaoSQL.db_connect()
cur_sys = cur_con.cursor()
class EspecialidadeDAO:

    def get_specializations_list():
        return dao.get_list('especializacao')

    def get_specialization_name(id):
        return dao.get_name(id, 'especializacao')

    def get_specialization(id):
        if id is None:
            return None

        query = "SELECT * FROM especializacao WHERE id=" + str(id)
        cur_sys.execute(query)

        def build_object(row):
            if row is None:
                return None
            special = Specialization(row[1], row[0])
            special.description = row[2]
            special.profession = row[3]
            special.spell_group = row[4]
            special.combat_group = row[5]
            return special

        return build_object(cur_sys.fetchone())

    def get_specialization_from_profession(profession_id):
        query = " SELECT id, nome FROM especializacao " \
                " WHERE id_profissao=" + str(profession_id)

        cur_sys.execute(query)
        return cur_sys.fetchall()

