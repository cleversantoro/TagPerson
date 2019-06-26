from DataBase.ConexaoSQL import ConexaoSQL
from DAO.GenericDAO import GenericDAO as dao
from Model.Raca import Race

cur_con = ConexaoSQL.db_connect()
cur_sys = cur_con.cursor()
class RacaDAO:

    def get_races_list():
        return dao.get_list('raca')

    def get_race_name(id):
        return dao.get_name(id, 'raca')

    def get_race(id):
        query = "SELECT * FROM raca WHERE id=" + str(id)
        cur_sys.execute(query)
        race_row = cur_sys.fetchone()

        query = "SELECT p.id FROM raca_profissao rp, profissao p WHERE p.id=rp.id_profissao AND rp.id_raca=" + str(id)
        cur_sys.execute(query)
        available_prof_rows = cur_sys.fetchall()

        def build_object(row, av_prof_rows):
            if row is None:
                return None
            else:
                race = Race(row[1], row[0])
                race.image = row[3]
                race.description = row[2]

                for i in range(7):
                    race.attribute_bonus[i] = row[i+4]
                
                race.base_speed = row[11]
                race.ef = row[12]
                race.base_height = row[13]
                race.base_weight = row[14]
                race.age = (row[15], row[16])
                race.available_professions = [av_prof[0] for av_prof in av_prof_rows]
                return race

        return build_object(race_row, available_prof_rows)
