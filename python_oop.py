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





my_car = Car("Toyota","Corolla")
print(my_car.brand)
print(my_car.full_name())

class Bank:
    def __init__(self,balance,withdraw):
        self.balance = balance
        self.withdraw = withdraw
    def total_balance (self):
        return (self.balance-self.withdraw)
    



Customer1 =Bank(500,200)
Customer2 = Bank("1000","5000")
print(f"After withdrawal ₹{Customer1.withdraw} now account balance ₹{Customer1.total_balance()}")

class Store:
    def __init__(self,phone,price):
        self.phone=phone
        self.price=price
    def full_details(self):
        return f"{self.phone} price ₹{self.price}" 
phone1=Store("iphone",1000)
phone2=Store("Samsung",30000)
print(phone1.price)
print(phone2.full_details())

class Student:
    college_name = "ABC college"

    def __init__(self,name,cgpa):
        self.name= name
        self.cgpa=cgpa

stu1 = Student("Arif",9.5)        
print(Student.college_name)
print(stu1.college_name)
# instance , class & static
class Laptop:
    storage_type = "SSD"
    def __init__(self,RAM,storage):
        self.RAM = RAM
        self.storage = storage
    @classmethod    
    def get_storage_info(cls):
        print(f"the storage type was {cls.storage_type}")   

    def get_info(self):
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")
        
l1 = Laptop("8gb","1TB")
l2 = Laptop("4gb","500gb")
l1.get_storage_info()
l2.get_info()
