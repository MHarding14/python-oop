class Animal:

    def __init__(self, colour = ''):
        self.lungs = True
        self.eyes = True
        self.alive = True
        self.colour = colour

    def sleep(self):
        print('Zzzzzzzzzz.......')

    def eat(self, food = ''):
        print('Nom Nom Nom Yum Yum!!', food)

    def breathe(self):
        pass