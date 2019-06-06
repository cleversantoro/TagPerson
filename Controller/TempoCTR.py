from DAO.TempoDAO import TempoDAO  as dao

class TempoCTR:

    def get_timeline():
        return dao.get_timeline()
