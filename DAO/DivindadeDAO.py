from DAO.GenericDAO import GenericDAO 

dao = GenericDAO
class DivindadeDAO:

    def get_gods_list():
        return dao.get_list('divindade', ', dominio')

    def get_god_name(id):
        return  dao.get_name(id, 'divindade')
