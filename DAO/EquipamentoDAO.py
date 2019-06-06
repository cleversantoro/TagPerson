from DataBase.ConexaoSQL import ConexaoSQL
from DAO.GenericDAO import GenericDAO as dao 
from Model.Escudo import Shield
from Model.Armas import Weapon
from Model.Defesa import Defense
from Model.Items import Item

cur_con = ConexaoSQL.db_connect()
cur_sys = cur_con.cursor()
class EquipamentoDAO:
    def get_equipment_list():
        return dao.get_list('equipamento')

    def get_equipment_item(id):
        query = "SELECT * FROM equipamento WHERE id=" + str(id)
        cur_sys.execute(query)

        def build_object(row):
            if row is None:
                return None

            is_weapon = (row[6] == 1)
            is_defense = (row[7] == 1)

            if is_weapon:
                if is_defense:
                    item = Shield(row[2])
                else:
                    item = Weapon(row[2])
            elif is_defense:
                item = Defense(row[2])
            else:
                item = Item(row[2])


            if is_weapon:
                query = "SELECT * FROM equipamento_armas WHERE id=" + str(id)
                cur_sys.execute(query)
                wrow = cur_sys.fetchone()

                item.skill_id = wrow[1]
                item.min_strength = wrow[2]
                item.min_damage = wrow[3]
                item.attack_defense['l'] = wrow[4]
                item.attack_defense['m'] = wrow[5]
                item.attack_defense['p'] = wrow[6]
                item.range = wrow[7]

            if is_defense:
                query = "SELECT * FROM equipamento_defesa WHERE id=" + str(id)
                cur_sys.execute(query)
                drow = cur_sys.fetchone()

                item.type = drow[1]
                item.base_defense = drow[2]
                item.absorption = drow[3]

            item.group = row[1]
            item.description = row[3]
            item.price = row[5]

            image_file = row[4]
            if image_file is not None:
                item.image = None #get_image_pixbuf(self.images_path, image_file)
            return item

        return build_object(cur_sys.fetchone())

    def get_equipment_groups():
        return dao.get_list('equipamento_grupos')

    def get_equipment_from_group(group_id):
        query = "SELECT id, nome, descricao, valor FROM equipamento " \
                "WHERE id_grupo =" + str(group_id)
        cur_sys.execute(query)
        return cur_sys.fetchall()

    def get_equipment_from_group_armor(group_id):
        query = "SELECT id, nome, descricao, valor FROM equipamento " \
                "WHERE armadura = 1 and id_grupo =" + str(group_id)
        cur_sys.execute(query)
        return cur_sys.fetchall()