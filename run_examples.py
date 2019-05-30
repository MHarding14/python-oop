from animal_class import*
from reptile_class import*

#run examples here - seperation of concerns

animal_1 = Animal()
# print(animal_1)
# animal_1 only has the behaviours of an animal

ringo = Reptile()
# ringo has all the behaviours of an animal plus that of a reptile
ringo.sleep()
ringo.seek_heat()
ringo.hunt()
ringo.eat('eggs of innocent birds')