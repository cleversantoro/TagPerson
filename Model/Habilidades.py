from Model.__Base__ import Base

class Skill(Base):
    def __init__(self, name, id=-1):
        Base.__init__(self, id)
        self.skill_group_id = 0
        self.atribute = None
        self.level_test = False
        self.restricted = False
        self.penalty = None
        self.perfect_tasks = None
        self.levels = []
        self.bonus =  0
        self.has_specialization = False
        self.specialization_suggestions = None

    def __str__(self):
        return 'Skill: %s\nDescription: %s\nr: %s\ne: %s\nsuggestions: %s' % \
                    (self.name, self.description, str(self.restricted),
                    str(self.has_specialization), str(self.specialization_suggestions))
