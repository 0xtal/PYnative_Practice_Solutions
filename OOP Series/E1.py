class Vehicle :
    '''A base class for all vehicle properties.'''
    count = 0

    def __init__(self, speed, miles) :
        self.max_speed = speed
        self.mileage = miles
        Vehicle.count += 1
        
    def shout_speed(self) :
        return self.max_speed
    def shout_miles(self) :
        return self.mileage

civic = Vehicle(100,200000)
passport = Vehicle(110, 150000)

print(civic.max_speed, civic.mileage)
print(passport.max_speed, passport.mileage)