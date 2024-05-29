
class Vegetable:

    def __init__(self, vegetable_type):
        self.vegetable_type = vegetable_type
    
    def message(self):
        print("This is a vegetable of type: ", self.vegetable_type)
    
class Potato(Vegetable):

    def __init__(self, potato_type):
        super().__init__(vegetable_type="Potato")
        self.potato_type = potato_type
        
    def message(self):
        print("This is a", self.potato_type, "potato, which is a type of vegetable:", self.vegetable_type)

vegetable = Vegetable("Veggie")
vegetable.message()

potato = Potato("Irish")
potato.message()