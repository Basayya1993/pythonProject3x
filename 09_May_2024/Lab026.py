class Car():

    def Suzuki(self):
        return "Maruti Brand"

    def Ford(self):
        return "Ford Brand"

class Bike():
    def Splendor(self):
        return "Honda Brand"


vehicle = Car()
print(vehicle.Suzuki())
print(vehicle.Ford())
vehicle = Bike()
print(vehicle.Splendor())

