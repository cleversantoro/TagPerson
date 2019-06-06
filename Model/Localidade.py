from Model.__Base__ import Base

class Place(Base):
    def __init__(self, name, id=-1, x=0, y=0):
        Base.__init__(self, name, id)
        self.parent_id = -1
        self.crest = None
        self.coord = (x, y)
        self.quote = None
        self.autor = None

    #def set_quote(self, quote, author):
    #    if quote is None or quote == '':
    #        self.quote = None
    #    else:
    #        if author is None:
    #            author = ''
    #        self.quote = (quote, author)
