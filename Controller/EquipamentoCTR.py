from DAO.EquipamentoDAO import EquipamentoDAO as dao

class EquipamentoCTR:

    def get_equipment_list():
        return dao.get_equipment_list()
    
    def get_equipment_name(id):
        return dao.get_equipment_name(id)

    def get_equipment_item(id):
        return dao.get_equipment_item(id)

    def get_equipment_groups():
        return dao.get_equipment_groups()

    def get_equipment_from_group(group_id):
        return dao.get_equipment_from_group(group_id)

    def get_equipment_from_group_armour(group_id):
        return dao.get_equipment_from_group_armour(group_id)

    def get_equipment_from_group_shield(group_id):
        return dao.get_equipment_from_group_shield(group_id)

    def get_equipment_from_group_helmet(group_id):
        return dao.get_equipment_from_group_helmet(group_id)

    def get_item_kind(item):
        return dao.get_item_kind(item)