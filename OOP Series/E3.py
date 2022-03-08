class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle) :
    pass

New_Bus = Bus('School Volvo', 180, 12)

print('Vehicle Name:', New_Bus.name, 'Speed:', New_Bus.max_speed,'Mileage:', New_Bus.mileage)