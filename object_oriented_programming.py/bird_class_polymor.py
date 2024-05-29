
class Bird:

    def __init__(self, bird_type):
        self.bird_type = bird_type
    def message(self):
        print("I am a bird and classified under an", self.bird_type, "specie")

class Duck(Bird):
    def __init__(self, duck_type):
        Bird.__init__(self, bird_type= 'white duck')
        self.duck_type = duck_type

    def message(self):
        print("A duck is classified as a bird family, that lives on the land and is domesticated")
    
bird = Bird('Eagle')
bird.message()

duck = Duck('White duck')
duck.message()
