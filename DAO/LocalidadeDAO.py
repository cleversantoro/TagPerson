from DataBase.ConexaoSQL import ConexaoSQL
from DAO.GenericDAO import GenericDAO as dao
from Model.Localidade import Place

cur_con = ConexaoSQL.db_connect()
cur_sys = cur_con.cursor()
class LocalidadeDAO:

    def get_place_name(id):
        return dao.get_name(id, 'localidade')

    def get_places_parents():
        query = "SELECT id, nome FROM localidade WHERE id_pai=-1"
        cursor = cur_sys.execute(query)
        return cursor.fetchall()

    def get_places_list():
        localidade = dao.get_list('localidade', ', id_pai')
        parent = {}
        for i in range(len(localidade)):
            id, name, parent_id = localidade[i]
            if parent_id == -1:
                parent[id] = [name]
            else:
                try:
                    parent[parent_id].append('%s, %s' % \
                                             (name, parent[parent_id][0]))
                except KeyError:
                    parent[id] = [name]
        localidade = []
        map(localidade.extend, parent.values())
        return localidade

    def get_place(id):
        if id is None:
            return None

        query = "SELECT * FROM localidade WHERE id=" + str(id)
        cur_sys.execute(query)

        def build_object(row):
            if row is None:
                return None
            place = Place(row[2], row[0], row[6], row[7])
            #place.id = row[0],
            place.parent_id = row[1]
            place.name = row[2]
           
            crest_file = row[3]
            if crest_file is not None:
                place.crest = row[3] #None #get_image_pixbuf(images_path, crest_file)

            place.quote = row[4]
            place.autor = row[5]
            place.coord = (row[6],row[7])

            return place

        return build_object(cur_sys.fetchone())
