class Rectangle:
    def __init__(self, width, length):
        self.length = length
        self.width = width
    def calculate_perimeter(self):
        return 2 * (self.width + self.length)
Rectangle_1 = Rectangle(3, 4)
print (Rectangle_1.calculate_perimeter())