class Vehicle:
    'A base class to define Vehicle classes'
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
                
class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass


Vehicle.color = 'Purple'

volvo = Vehicle('School Volvo', 180, 12)
audi = Vehicle('Audi Q5', 240, 18)

print('Color:',volvo.color, end = ', ')
print('Vehicle name:',volvo.name, end = ', ')
print('Speed:',volvo.max_speed,end = ', ')
print('Mileage:',volvo.mileage)

print('Color:',audi.color, end = ', ')
print('Vehicle name:',audi.name, end = ', ')
print('Speed:',audi.max_speed,end = ', ')
print('Mileage:',audi.mileage)