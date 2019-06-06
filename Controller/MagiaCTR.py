from DAO.MagiaDAO import MagiaDAO as dao

class MagiaCTR:

    def get_spells_list():
        return dao.get_spells_list()

    def get_spell(id):
        return dao.get_spell(id)

    def get_spell_name(id):
        return dao.get_spell_name(id)

    def get_spell_group_parents():
        return dao.get_spell_group_parents()

    def get_spell_group_children(parent_id):
        return dao.get_spell_group_children(parent_id)

    def get_spells_from_group(spellgroup_id):
        return dao.get_spells_from_group(spellgroup_id)
