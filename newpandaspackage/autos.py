# autos.py

class Auto():
    '''
    Params:
        make str
        model str
        year int
        color str
        num_wheels int
        bed_size str
    '''

    def __init__(self, make, model, year, color, num_wheels):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.num_wheels = num_wheels

    def drive(self):
        print("WE ARE DRIVING", self.model)

    def advertise(self):
        print("BUY OUR", self.model)


# designates the Truck class should inherit from the Auto class
class Truck(Auto):  
    def __init__(self, make, model, year, color, num_wheels, bed_size):
        # can invoke parent class methods via super()
        super().__init__(make, model, year, color, num_wheels)
        self.bed_size = bed_size

    # can overwrite parent class methods
    def advertise(self):
        print("VROOOOM", self.model)


if __name__ == "__main__":

    car = Auto("Toyota", "Prius", 2020, "Blue", 4)
    print(car.make)
    print(car.model)
    car.drive()
    car.advertise()
    print('\n')

    car2 = Auto("Tesla", "Model S", 2020, "Blue", 4)
    print(car2.make)
    print(car2.model)
    car2.drive()
    car2.advertise()
    print('\n')

    truck = Truck("Ford", "F150", 2020, "Blue", 4, bed_size="5x5")
    truck.drive()
    truck.advertise()
    print(truck.bed_size)
    print('\n')

    truck2 = Truck("Tesla", "Cybertuck", 2020, "Silver", 6, bed_size="10x10")
    print(truck2.make)
    print(truck2.model)
    print(truck2.year)
    truck2.drive()
    truck2.advertise()
    print(truck2.bed_size)
    print('\n')
