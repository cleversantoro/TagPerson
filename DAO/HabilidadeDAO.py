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
            skill.skill_group_id = row[1]
            skill.name = row[2]
            skill.atribute = row[3]
            skill.level_test = bool(row[4])
            skill.restricted = bool(row[5])
            skill.penalty = row[6]
            skill.perfect_tasks = row[7]
            skill.description = row[8]
            skill.levels = row[9].split("|")
            skill.bonus = row[10]
            skill.has_specialization = bool(row[11])

            if skill.has_specialization:
                skill.specialization_suggestions = HabilidadeDAO.get_skill_specialization_suggestions(row[0])

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
                " FROM habilidade s, habilidade_grupo_custo sg "\
                " WHERE s.id=sg.id_habilidade AND sg.id_habilidade_grupo=" + str(skillgroup_id)
        cur_sys.execute(query)
        return cur_sys.fetchall()

    def get_skill_specialization_suggestions(skill_id):
        query = " SELECT id_habilidade, sugestao FROM "\
                " habilidade_especializacao where id_habilidade = "  + str(skill_id) + \
                " ORDER BY sugestao "
        cur_sys.execute(query)
        return cur_sys.fetchall()

