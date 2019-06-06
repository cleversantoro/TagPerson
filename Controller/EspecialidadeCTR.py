from DAO.EspecialidadeDAO import EspecialidadeDAO as dao

class EspecialidadeCTR:

    def get_specializations_list():
        return dao.get_specializations_list()

    def get_specialization_name(id):
        return dao.get_specialization_name(id)

    def get_specialization(id):
        return dao.get_specialization(id)

