from DAO.CombateDAO import CombateDAO as dao

class CombateCTR:

    def get_combat_list():
        return dao.get_combat_list()

    def get_combat(id):
        return dao.get_combat(id)

    def get_combat_name(id):
        return dao.get_combat_name(id)

    def get_combat_group_parents():
        return dao.get_combat_group_parents()

    def get_combat_group_children(parent_id):
        return dao.get_combat_group_children(parent_id)

    def get_combat_from_group(skillgroup_id):
        return dao.get_combat_from_group(skillgroup_id)

    def get_combat_group_name(id):
        return dao.get_combat_group_name(id)


