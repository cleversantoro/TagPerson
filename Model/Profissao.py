from Model.__Base__ import Base

class Profession(Base):
    def __init__(self, name, prof_id=-1):
        Base.__init__(self, name, prof_id)
        self.eh = 0
        self.equipment = []
        self.posessions = (0, 0, 0)
        self.skill_points = 0
        self.weapon_points = 0
        self.combat_points = 0
        self.penalized_skill_group = -1
        self.specialization_skill = -1
        self.attribute_for_magic = -1
        self.spell_group = -1

    def __str__(self):
        return '%s\n%s\n%s\n%s\neh:%d\nph:%d\nghp:%s\nespH:%s\npa:%d,pc:%d' % \
                    (self.name, self.description, str(self.equipment),
                    str(self.posessions), self.eh, self.skill_points,
                    self.penalized_skill_group, self.specialization_skill,
                    self.weapon_points, self.combat_points)
