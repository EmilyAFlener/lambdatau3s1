# Emily Fleners LS DS Unit 3 Sprint Challenge 1.

# Part 1 - Keeping it Classy
# Creating a class given the parameters from the assignment.

import random

print(random.randint(1000000, 9999999))
# 8332413 created in the terminal and will be used for this project.
# Should this function be placed into the parameters itself so it generates each time?

class Product:

    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=8332413):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identififer

    # Part 2 - Objects that Go!
    # Creating methods for the product class.
    def stealability(self):
        value = price/weight
        if value < 0.5:
            print('Not so stealable ...')
        elif value >= 0.5 & < 1.0:
            print('Kinda stealable ...')
        else:
            print('Very stealable!')

    
    def explode(self):
        volatility = flammability*weight
        if volatility < 10:
            print('... fizzle.')
        elif volatility >= 10 & <50:
            print('... boom!')
        else:
            print('...BABOOM!')


# Part 3 - A Proper Inheritance
# Creating a subclass and new methods.
class BoxingGlove(Product):

    def noexplode(self):
        print('...its a glove.')

    
    def punch(self):
        if weight < 5:
            print('That tickles.')
        elif weight > 5:
            print('Hey that hurt!')
        else:
            print('OUCH!')