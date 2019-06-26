from DAO.HabilidadeDAO import HabilidadeDAO as dao

class HabilidadeCTR:

    def get_skills_list():
        return dao.get_skills_list()

    def get_skill(id):
        return dao.get_skill(id)

    def get_skill_name(id):
        return dao.get_skill_name(id)

    def get_skill_group_parents():
        return dao.get_skill_group_parents()

    def get_skill_group_children(parent_id):
        return dao.get_skill_group_children(parent_id)

    def get_skills_from_group(skillgroup_id):
        return dao.get_skills_from_group(skillgroup_id)

    def get_skill_group_name(id):
        return dao.get_skill_group_name(id)

    def get_skill_specialization_suggestions(id):
        return dao.get_skill_specialization_suggestions(id)

