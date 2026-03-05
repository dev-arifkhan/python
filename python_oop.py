# object oriented programming.
class Car:
    def __init__(self, brand, model):
        self.brand =brand
        self.model =model
    def full_name(self):
        return f"{self.brand} {self.model}"    

class EletricCar (Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize
        
my_tesla =EletricCar("Tesla","Model S", "85kwh")       

print(my_tesla.full_name())     
















# my_car = Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.full_name())