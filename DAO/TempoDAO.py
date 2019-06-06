from DataBase.ConexaoSQL import ConexaoSQL

cur_con = ConexaoSQL.db_connect()
cur_sys = cur_con.cursor()
class TempoDAO:

    def get_timeline():
        query = "SELECT ano, evento FROM linha_tempo"
        cursor = cur_sys.execute(query)
        timeline = {}

        for year, event in cursor.fetchall():
            timeline[year] = event

        return timeline
