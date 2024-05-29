
class Mammal:
    def __init__(self, species, name):
        self.species = species
        self.name = name
    
    def show_species(self):
        print('I am a', self.species)
    
    def show_name(self):
        print('My name is', self.name)
    
    def make_sound(self):
        pass
    

class Dog(Mammal):
    def __init__(self, name):
        Mammal.__init__(self,'Dog', name)

    def make_sound(self):
        print('Woof! Woof!')

class Cat(Mammal):
    def __init__(self, name):
        Mammal.__init__(self, 'Cat', name)
    
    def make_sound(self):
        print('Meow! Meow!')
    
dog = Dog("Jumby")
dog.show_species()
dog.show_name()
dog.make_sound()

cat = Cat("Furry")
cat.show_species()
cat.show_name()
cat.make_sound()

