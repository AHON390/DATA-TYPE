'''
class fruit:
    def __init__(self,name,color):
        self.name=name
        self.color=color
pie=fruit('pineapple','yellow')
print(pie.name)
print(pie.color)
'''
'''
class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modelX = vehicle(240, 18)
print('model max speed:',modelX.max_speed)
print('model mileage:',modelX.mileage)
'''
class parrot:
    specias='bird'
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu = parrot('blu',10)
woo = parrot('woo',15)
print(blu.name)
print(blu.age)
print(woo.name)
print(woo.age)
