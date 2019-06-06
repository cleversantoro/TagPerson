from Model.__Base__ import Base

class Spell(Base):
    def __init__(self, name, id=-1):
        Base.__init__(self, name, id)
        self.evocation = None
        self.range = None
        self.duration = None
        self.level = None

    def __str__(self):
        return '%s\n%s\n%s, %s, %s\n%s' % (self.name, self.description, self.evocation, self.range, self.duration, self.level)
