class Animal:
    origin = 'I am an animal from the animal kingdom.. (on earth)'
    # Class is a blueprint of an object - stores how it looks and how it behaves
    # Define how it looks
    # and how it behaves (methods)

    def __init__(self, species, colour = '', loc = ''):
        self.species = species
        self.alive = True
        self.colour = colour
        self.location = loc

    # Behaviour (methods)
    def sleep(self):
        print('soooo sleeeeepppy..... zzzllleeeeeeeeeeeep.. zzzzz')

    def breath(self):
        print('Inhaaaallleeee...... (HOLD)... Exhaaaalllleeee')

    def eat(self, food = ''): # (= '') means the argument is optional
        print('NUM NUM NUM YUM YUM!!', food)

    def potty(self):
        print('uhhhhhhhh.... hmmmmm... puuuush.. *PLOP*... :D')

    def what_are_you(self):
        print(self.origin)
        # self refers to the instance of Animal not the class!

# To call the methods, we need an Animal object
# Create and Animal object

dog = Animal()

# print(dog)
# print(type(dog))

#now you have an animal you can call the different methods on it

# dog.breath()
# dog.eat()
# dog.sleep()
# dog.potty()

dog.origin
#and
dog.what_are_you()
#are the same