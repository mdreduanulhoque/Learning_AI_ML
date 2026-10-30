"""
Q9. Create the following classes: Herbivore, Carnivore, Omnivore with some attributes and methods. 
Then create a class Bear that inherits from all the above classes to showcase how multiple inheritance works.
"""
class Herbivore:
    def herbivore(self):
        print("Print from Herbivore")

class Carnivore:
    def carnivore(self):
        print("Print from Carnivore")

class Omnivore:
    def omnivore(self):
        print("Print from Omnivore")

class test(Herbivore, Carnivore, Omnivore):
    def __init__(self):
        super().__init__()

t = test()
t.herbivore()
t.carnivore()
t.omnivore()