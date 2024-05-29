
class Automobile:
    def __init__(self, make, model, mileage, price):
        self._make = make
        self._model = model
        self._mileage = mileage
        self._price = price

    def set_make (self, make):
        self._make = make
    def set_model(self, model):
        self._model = model
    def set_mileage(self, mileage):
        self._mileage = mileage
    def set_price(self, price):
        self._price = price

    def get_make (self):
        return self._make
    def get_model(self):
        return self._model
    def get_mileage(self):
        return self._mileage
    def get_price(self):
        return self._price

vehicle = Automobile("Honda", "Avensis", 450, 3500000)
print(f" Car Make:", vehicle.get_make())
print(f" Car Mileage:", vehicle.get_mileage())
print(f" Car Model:", vehicle.get_model())
print(f" Car Price:", vehicle.get_price())
# This print functions was used to test the above codes

class Car(Automobile):
    def __init__(self, make, model, mileage, price, doors):
        Automobile.__init__(self, make, model, mileage, price)
        self._doors = doors

    def set_doors(self, doors):
        self._doors = doors

    def get_doors(self):
        return self._doors
    
car1 = Car("Honda", "Avensis", 500, 2500000, 4)
print(f" The number of doors before set_doors method is:", car1.get_doors())
car1.set_doors(2)
print(f" The number of doors after set_doors methof is:", car1.get_doors())

# Create a truck class and allowing it to inherit the 'Automobile" attributes
class Truck(Automobile):
    def __init__(self, make, model, mileage, price, doors, drive_type):
        Automobile.__init__(self, make, model, mileage, price)
        self._drive_type = drive_type

    def set_drive_type(self, drive_type):
        self._drive_type = drive_type

    def get_drive_type(self):
        return self._drive_type
    
Truck = Truck("Honda", "Avensis", 650, 4500000, 2, "Automatic")
print(f" The drive type of the Truck is:", Truck.get_drive_type())

class SUV(Automobile):
    def __init__(self, make, model, mileage, price, doors, drive_type, pass_cap):
        Automobile.__init__(self, make, model, mileage, price)
        self._pass_cap = pass_cap

    def set_pass_cap(self, pass_cap):
        self._pass_cap = pass_cap

    def get_pass_cap(self):
        return self._pass_cap

SUV = SUV("Honda", "Avensis", 500, 2500000, 4, "Automatic", 6)
print(f" The Passenger Capacity of the SUV is:", SUV.get_pass_cap())