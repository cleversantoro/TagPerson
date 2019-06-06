from DAO.EquipamentoDAO import EquipamentoDAO as dao

class EquipamentoCTR:

    def get_equipment_list():
        return dao.get_equipment_list()

    def get_equipment_item(id):
        return dao.get_equipment_item(id)

    def get_equipment_groups():
        return dao.get_equipment_groups()

    def get_equipment_from_group(group_id):
        return dao.get_equipment_from_group(group_id)

    def get_equipment_from_group_armor(group_id):
        return dao.get_equipment_from_group_armor(group_id)