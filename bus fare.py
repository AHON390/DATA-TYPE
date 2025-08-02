class vehicle:
    def __init__(self,name,sit_capasity,rent,mileage):
        self.name=name
        self.sit_capasity=sit_capasity
        self.rent=rent
        self.mileage=mileage
class bus(vehicle):
    pass
school_bus = bus('school bus',50,5500,20)
print('vehicle name: ',school_bus.name,"sit capasity : ",school_bus.sit_capasity,"rent : ",school_bus.rent)
