from Model.__Base__ import Base

class Combat(Base):
    def __init__(self, name, id=-1):
        Base.__init__(self, id)
        self.skill_group_id = 0
        self.category_id = 0
        self.atribute = None
        self.effect = None
        self.requisite = None
        self.Obs = []
        self.scrolling = None
        self.upgrading = None
        self.bonus = 0
        self.has_specialization = False


    def __str__(self):
        return 'Skill: %s\nDescription: %s\nr: %s\ne: %s\nsuggestions: %s' % \
                    (self.name, self.description, str(self.atributed),
                    str(self.has_specialization), str(self.bonus))
