class BMW():
    def fuel_type(self):
        print("BMW's maximum fuel is 45 litre.")
    def max_speed(self):
        print("BMW's maximum speed is 460 km .")
class Ferari():
    def fuel_type(self):
        print("Ferari's maximum fuel is 30 litre.")
    def max_speed(self):
        print("Ferari's maximum speed is 420 km.")
obj1=BMW()
obj2=Ferari()
for car in (obj1,obj2):
    car.fuel_type()
    car.max_speed()
