from DataBase.ConexaoSQL import ConexaoSQL
from DAO.GenericDAO import GenericDAO as dao
from Model.Habilidades import Skill

cur_con = ConexaoSQL.db_connect()
cur_sys = cur_con.cursor()
class HabilidadeDAO:

    def get_skills_list():
        return dao.get_list('habilidade')

    def get_skill_name(id):
        return dao.get_name(id, 'habilidade')

    def get_skill_group_name(id):
        return dao.get_name(id, 'habilidade_grupo')

    def get_skill(id):
        query = "SELECT * FROM habilidade WHERE id=" + str(id)
        cur_sys.execute(query)

        def build_object(row):
            if row is None:
                return None
            skill = Skill(row[1], row[0])
            skill.id = row[0]
            skill.name = row[1]
            skill.description = row[2]
            skill.bonus = row[3]
            skill.has_specialization = bool(row[4])
            skill.specialization_suggestions = HabilidadeDAO.get_skill_specialization_suggestions()#row[0])
            return skill

        return build_object(cur_sys.fetchone())

    def __get_skill_group_list(parent_id='-1'):
        query = "SELECT id, nome FROM habilidade_grupo "\
                "WHERE id_pai=%s" % parent_id
        cur_sys.execute(query)
        return cur_sys.fetchall()

    def get_skill_group_parents():
        return HabilidadeDAO.__get_skill_group_list()

    def get_skill_group_children(parent_id):
        return HabilidadeDAO.__get_skill_group_list(parent_id)

    def get_skills_from_group(skillgroup_id):
        query = " SELECT s.id, s.nome, sg.custo, s.bonus, s.possui_especializacao "\
                " FROM habilidade s, habilidade_habilidade_grupo sg "\
                " WHERE s.id=sg.id_habilidade AND sg.id_habilidade_grupo=" + str(skillgroup_id)
        cur_sys.execute(query)
        return cur_sys.fetchall()

    def get_skill_specialization_suggestions():
        query = " SELECT id_habilidade, sugestao FROM "\
                " habilidade_especializacao ORDER BY sugestao "
        cur_sys.execute(query)
        return cur_sys.fetchall()

