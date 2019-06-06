from DAO.LocalidadeDAO import LocalidadeDAO as dao

class LocalidadeCTR:

    def get_places_parents():
        return dao.get_places_parents()

    def get_places_list():
        return dao.get_places_list()

    def get_place_name(id):
        return dao.get_place_name(id)

    def get_place(id):
        return dao.get_place(id)
