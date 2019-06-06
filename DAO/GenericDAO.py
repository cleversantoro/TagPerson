from DataBase.ConexaoSQL import ConexaoSQL

cur_con = ConexaoSQL.db_connect()
cur_sys = cur_con.cursor()
class GenericDAO:

    def get_name(id, table):
        
        if id is None or table is None:
            return None
        else:
            query = "SELECT nome FROM %s WHERE id=%s" % (table, str(id))
            cur_sys.execute(query)
            result = cur_sys.fetchone()

            if len(result) == 0:
                return None
            else:
                return result[0]

    def get_list(table, columns=''):
        if table is None:
            return None
        else:
            query = "SELECT id, nome%s FROM %s" % (columns, table)
            cursor = cur_sys.execute(query)
            return cursor.fetchall()


