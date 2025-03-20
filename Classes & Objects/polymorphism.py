# def area(radius):
#     print(radius)


# def area(length,breadth):
#     print(length,breadth)

# area(8,9)
import math
class Circle():
    def area(self,radius):
        print('Circle Area = ',math.pi * (radius ** 2))

class Rectangle():
    def area(self,length,breadth):
        print('Rectangle Area = ',length*breadth)

c = Circle()
c.area(3)

r = Rectangle()
r.area(5,6)

