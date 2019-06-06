from DAO.RacaDAO import RacaDAO as dao

class RacaCTR:

    def get_races_list():
        return dao.get_races_list()

    def get_race_name(id):
        return dao.get_race_name(id)

    def get_race(id):
        return dao.get_race(id)
