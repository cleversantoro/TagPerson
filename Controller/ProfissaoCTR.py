from DAO.ProfissaoDAO import ProfissaoDAO as dao

class ProfissaoCTR:

    def get_professions_list():
        return dao.get_professions_list()

    def get_profession_name(id):
        return dao.get_profession_name(id)

    def get_profession(id):
        return dao.get_profession(id)
