class Base:
    def __init__(self, name='', id=-1):
        self.id = id
        self.name = name
        self.description = None
        self.image = None

    def __str__(self):
        return '%s\n%s' % (self.name, self.description)

