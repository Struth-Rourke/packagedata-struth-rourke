# autos.py

class Auto():
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

class Truck(Auto): # designates the Truck class should inherit from the Auto class
    def __init__(self, make, model, year, color, num_wheels, bed_size):
        super().__init__(make, model, year, color, num_wheels) # can invoke parent class methods via super()
        self.bed_size = bed_size

    # can overwrite parent class methods
    def advertise(self):
        print("VROOOOM", self.model)

if __name__ == "__main__":

    car = Auto("Toyota", "Prius", 2020, "Blue", 4)
    car.make
    car.model
    car.drive()
    car.advertise()

    car2 = Auto("Tesla", "Model S", 2020, "Blue", 4)
    car.make
    car.model
    car2.drive()
    car2.advertise()

    truck = Truck("Ford", "F150", 2020, "Blue", 4, bed_size="5x5")
    truck.drive()
    truck.advertise()
    print(truck.bed_size)

    truck2 = Truck("Tesla", "Cybertuck", 2020, "Silver", 6, bed_size="10x10")
    truck2.make
    truck2.model
    truck2.year
    truck2.drive()
    truck2.advertise()
    print(truck2.bed_size)