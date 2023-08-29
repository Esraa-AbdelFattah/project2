class car():
    def __init__(self, Car_Type, modle, year):
        self.Car_Type = Car_Type
        self.modle = modle
        self.year = year
        self.speed = 0

    def acceleration(self):
        self.speed += 10

    def breaks(self):
        self.speed -= 10

    def get_speed(self):
        return self.speed


my_car = car("BMW", "XM", 2022)
print(my_car.Car_Type, my_car.modle, my_car.year)

my_car.acceleration()
my_car.acceleration()
my_car.acceleration()
my_car.breaks()

print(my_car.get_speed())

