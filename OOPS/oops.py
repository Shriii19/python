
#-----------------------------------------------------------------

#calss nd object or Instances
print("**class nd obj**")
class Car:  #class
        def __init__ (self, brand, model): #object
                self.brand = brand
                self.model = model

        def fule(self):
                return "petrol or diesel"


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

