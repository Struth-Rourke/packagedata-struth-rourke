# newpandaspackage/polos.py

# Polo Class
# attributes / propertiess: size, style, color, texture, price
# methods: wash, fold, pop collar

class Polo():
    def __init__(self, size, color): # "__init__" = constructor function
        self.size = size # Calling that particular thing on the instance itself
        self.color = color
        pass

    def wash(self): # Functions we define inside the Class for METHODS
        print('WASHING')

    def fold(self):
        print('FOLDING')


if __name__ == "__main__":
    # df = DataFrame(___)
    # df.columns -> Method
    # df.head() -> Method

    # initialize a small blue polo and a large yellow polo


    p1 = Polo(size = 'Small', color = 'Blue')
    print(p1.size, p1.color)
    p1.wash()


    p2 = Polo(size = 'Large', color = 'Yellow')
    print(p2.size, p2.color)
    p2.fold()