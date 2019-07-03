from DAO.PersonagemDAO import PersonagemDAO as dao

class PersonagemCTR:

    def get_persona_list():
        return dao.get_persona_list()

    def get_players_names():
        return dao.get_players_names()

    def get_persona(id):
        return dao.get_persona(id)

    def get_persona_combat(persona_id):
        return dao.get_persona_combat(persona_id)
    
    def get_persona_skills(persona_id):
        return dao.get_persona_skills(persona_id)

    def get_persona_spells(persona_id):
        return dao.get_persona_spells(persona_id)

    def get_persona_equipment(persona_id):
        return dao.get_persona_equipment(persona_id)

    def save_persona(persona):
        return dao.save_persona(persona)

    def save_persona_spells(persona):
        return dao.save_persona_spells(persona)
    
    def save_persona_combat_skills(persona):
        return dao.save_persona_combat_skills(persona)

    def save_persona_skills(persona):
        return dao.save_persona_skills(persona)

    def save_persona_equipment(persona):
        return dao.save_persona_equipment(persona)

    def save_persona_weapon(persona):
        return dao.save_persona_weapon(persona)

    def get_combat_persona(persona_id,combat_group_id):
        return dao.get_combat_persona(persona_id,combat_group_id)

    def get_spell_persona(persona_id,spell_group_id):
        return dao.get_spell_persona(persona_id,spell_group_id)

    def get_skills_persona(persona_id,skills_group_id):
        return dao.get_skills_persona(persona_id,skills_group_id)
    