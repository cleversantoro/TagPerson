from Model.__Base__ import Base

class Specialization(Base):
    def __init__(self, name, id=-1):
        Base.__init__(self, name, id)
        self.profession = 0
        self.spell_group = 0
        self.combat_group = 0
