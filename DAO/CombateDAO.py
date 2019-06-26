from DataBase.ConexaoSQL import ConexaoSQL
from DAO.GenericDAO import GenericDAO as dao
from Model.Combate import Combat

cur_con = ConexaoSQL.db_connect()
cur_sys = cur_con.cursor()
class CombateDAO:

    def get_combat_list():
        return dao.get_list('combate')

    def get_combat_name(id):
        return dao.get_name(id, 'combate')

    def get_combat_group_name(id):
        return dao.get_name(id, 'combate_grupo')

    def get_combat(id):
        query = "SELECT * FROM combate WHERE id=" + str(id)
        cur_sys.execute(query)

        def build_object(row):
            if row is None:
                return None
            combat = Combat(row[3], row[0])
            combat.id = row[0]
            combat.skill_group_id = row[1]
            combat.category_id = row[2]
            combat.name = row[3]
            combat.atribute = row[4]
            combat.effect = row[5]
            combat.requisite = row[6]
            combat.Obs = row[7].split("|") 
            combat.scrolling = row[8]
            combat.upgrading = row[9]
            combat.bonus = row[10]
            combat.has_specialization = bool(row[11])
            return combat

        return build_object(cur_sys.fetchone())

    def __get_combat_group_list(parent_id='-1'):
        query = "SELECT id, nome FROM combate_grupo "\
                "WHERE id_pai=%s" % parent_id
        cur_sys.execute(query)
        return cur_sys.fetchall()

    def get_combat_group_parents():
        return CombateDAO.__get_combat_group_list()

    def get_combat_group_children(parent_id):
        return CombateDAO.__get_combat_group_list(parent_id)

    def get_combat_from_group(skillgroup_id):
        query = " SELECT c.id, c.nome, cg.custo, c.bonus, c.possui_especializacao "\
                " FROM combate c, combate_grupo_custo cg "\
                " WHERE c.id=cg.id_combate AND cg.id_combate_grupo=" + str(skillgroup_id)
        cur_sys.execute(query)
        return cur_sys.fetchall()

