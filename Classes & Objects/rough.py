import math

class Shape:
    definition = 'Area bounded by curve'
    area = 'Give a shape'

class Circle(Shape):
    def __init__(self,radius):
        self.area  = math.pi * (radius ** 2)
        self.definition = 'Circle definition'
    
class Square(Shape):
    def __init__(self,sideLength):
        self.area = sideLength ** 2
        self.definition = " it's all side are equals "

circle = Circle(5)
print(circle.__dict__)
print(circle.definition)

print("------------------------------------")

square = Square(5)
print(square.__dict__)
print(square.definition)