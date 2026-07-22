
#-----------------------------------------------------------------

#calss nd object or Instances
print("**class nd obj**")
class Car:  #class
        total_Car = 0

        def __init__ (self, brand, model): #object
                self.brand = brand
                self.model = model
                Car.total_Car += 1

        def fule(self):
                return "petrol or diesel"

        @classmethod
        def get_total_car(cls):
                return cls.total_Car

        @staticmethod
        def general_description():
                return "Cars are used for transportation."


Car1 = Car ("tata", "Neno")
print(Car1.brand)
print(Car1.model)



#-----------------------------------------------------------------
# inherients
print("**inherients**")
class EleCar (Car):
        def __init__ (self, brand, model, battary):
                super().__init__ (brand, model)
                self.battary = battary

        def fule(self):
                return "electric"


#-----------------------------------------------------------------

##encapsulation

# same as above we hide the imp data from user or we hide from user but we can access them in code



#-----------------------------------------------------------------

## polimoriphism 
print("**poli**")

pet = Car("tata", "safari")
print(pet.fule())

ev = EleCar("tata", "Neno EV", "40kWh")
print(ev.fule())


print("*** polyi nd inheri use in one ")

#-----------------------------------------------------------------

#class method and static method
print("**class method and static method**")

Car("tata", "Punch")
Car("tata", "Harrier")
Car("tata", "Nexon")

print(Car.get_total_car())
# print(Car.general_description())

#static method can be called using class name or object name
print(Car.general_description())


