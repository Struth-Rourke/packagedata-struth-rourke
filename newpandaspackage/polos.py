# newpandaspackage/polos.py

# Polo Class
# attributes / propertiess: size, style, color, texture, price
# methods: wash, fold, pop collar

class Polo():
    def __init__(self, size, color): # "__init__" = constructor function
        self.size = size # Calling that particular thing on the instance itself
        self.color = color
        pass

    @property # decorator - doesn't need parenthesis
    def full_name(self:)
    return f'{self.size} {self.color}'

    def wash(self): # Functions we define inside the Class for METHODS
        print(f'WASHING {self.size} {self.color} POLO!')

    @staticmethod # Doesn't require self 
    def fold():
        print('FOLDING')


if __name__ == "__main__":
    # df = DataFrame(___)
    # df.columns -> Method
    # df.head() -> Method

    # initialize a small blue polo and a large yellow polo


    p1 = Polo(size = 'Small', color = 'Blue')
    print(p1.size, p1.color)
    print(p1.full_name) # Decorator property
    p1.wash()


    p2 = Polo(size = 'Large', color = 'Yellow')
    print(p2.size, p2.color)
    print(p2.full_name)
    p2.fold()