from DataBase.ConexaoSQL import ConexaoSQL
from DAO.GenericDAO import GenericDAO as dao 
from Model.Escudo import Shield
from Model.Armas import Weapon
from Model.Defesa import Defense
from Model.Items import Item
from Helpers.constantes import const 

cur_con = ConexaoSQL.db_connect()
cur_sys = cur_con.cursor()
class EquipamentoDAO:
    def get_equipment_list():
        return dao.get_list('equipamento')

    def get_equipment_name(id):
        return dao.get_name(id,'equipamento')

    def get_equipment_item(id):
        query = "SELECT * FROM equipamento WHERE id=" + str(id)
        cur_sys.execute(query)

        def build_object(row):
            if row is None:
                return None

            is_weapon = (row[6] == 1)
            is_defense = (row[7] == 1)
            
            is_armour = (row[8] == 1)
            is_shield = (row[9] ==1)
            is_helmet = (row[10] ==1)

            if is_weapon:
                if is_defense:
                    is_weapon = False
                    is_defense = True
                    item = Shield(row[2])
                else:
                    item = Weapon(row[2])
            elif is_defense:
                item = Defense(row[2])
            else:
                item = Item(row[2])

            if is_weapon:
                query = "SELECT * FROM equipamento_armas WHERE id_equipamento=" + str(id)
                cur_sys.execute(query)
                wrow = cur_sys.fetchone()
                item.equipment_id = wrow[1]
                item.type = wrow[2]
                item.cust = wrow[3]
                item.range = wrow[4]
                item.min_strength = wrow[5]
                item.bonus = wrow[6]
                item.attack_defense['l'] = wrow[7]
                item.attack_defense['m'] = wrow[8]
                item.attack_defense['p'] = wrow[9]
                item._25 =  wrow[10]
                item._50 = wrow[11]
                item._75 = wrow[12]
                item._100 = wrow[13]
                item.Pq = wrow[14]
                item.An = wrow[15]
                item.El = wrow[16]
                item.Me = wrow[17]
                item.Hu = wrow[18]
                item.itemtype = 'weapon'

            if is_defense:
                query = "SELECT * FROM equipamento_defesa WHERE id_equipamento=" + str(id)
                cur_sys.execute(query)
                drow = cur_sys.fetchone()
                item.id = drow[0]
                item.equipment_id = drow[1]
                item.base_defense = drow[2]
                item.absorption = drow[3]
                item.min_strength = drow[4]
                item.max_strength = drow[5]
                item.P = drow[6]
                item.A = drow[7]
                item.E = drow[8]
                item.M = drow[9]
                item.H = drow[10]
                
                if(is_armour):
                    item.itemtype = 'armour'
                elif(is_helmet):
                    item.itemtype = 'helmet'
                elif(is_shield):
                    item.itemtype = 'shield'
                else:                
                    item.itemtype = 'defense'

            if type(item) == Item:
                item.itemtype = 'item'
                item.id = row[0]

            item.group = row[1]
            item.description = row[3]
            item.price = row[5]

            image_file = row[4]
            if image_file is not None:
                item.image = '{}\{}'.format(const.IMAGES, row[4]) 

            return item

        return build_object(cur_sys.fetchone())

    def get_equipment_groups():
        return dao.get_list('equipamento_grupos')

    def get_equipment_from_group(group_id):
        query = "SELECT id, nome, descricao, valor FROM equipamento " \
                "WHERE id_grupo =" + str(group_id)
        cur_sys.execute(query)
        return cur_sys.fetchall()

    def get_equipment_groups_misc():
        query = " SELECT id, nome FROM equipamento_grupos"\
                " WHERE id in (1,2,3,4,5,8,9,10,11,12)"\
                " ORDER BY nome"

        cur_sys.execute(query)
        return cur_sys.fetchall()

    def get_equipment_from_group_armour(group_id):
        query = "SELECT id, nome, descricao, valor FROM equipamento " \
                "WHERE armadura = 1 and id_grupo =" + str(group_id)
        cur_sys.execute(query)
        return cur_sys.fetchall()
    
    def get_equipment_from_group_shield(group_id):
        query = "SELECT id, nome, descricao, valor FROM equipamento " \
                "WHERE escudo = 1 and id_grupo =" + str(group_id)
        cur_sys.execute(query)
        return cur_sys.fetchall()    
    
    def get_equipment_from_group_helmet(group_id):
        query = "SELECT id, nome, descricao, valor FROM equipamento " \
                "WHERE capacete = 1 and id_grupo =" + str(group_id)
        cur_sys.execute(query)
        return cur_sys.fetchall()

    def get_item_kind(item):
        item_type = type(item)

        if item_type == Shield:
            item_kind = const.SHIELD

        elif item_type == Defense:
            if item.is_helmet():
                item_kind = const.HELMET
            else:
                item_kind = const.ARMOUR

        elif item_type == Weapon:
            if item.is_ranged():
                item_kind = const.RANGED_WEAPON
            else:
                item_kind = const.MELEE_WEAPON
        else:
            item_kind = -1

        return item_kind
