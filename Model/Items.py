from Model.__Base__ import Base

class Item(Base):
    def __init__(self, name):
        Base.__init__(self, name)
        self.price = 0
        self.description = None
        self.itemtype = None

    def __str__(self):
        return '%s\t%s\t%s' % \
                    (self.name, str(self.price), self.description)


