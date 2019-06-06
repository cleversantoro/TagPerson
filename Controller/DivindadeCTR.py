from DAO.DivindadeDAO import DivindadeDAO as dao

class DivindadeCTR:
    def get_gods_list():
        return dao.get_gods_list()

    def get_god_name(id):
        return dao.get_god_name(id)
