# class Collage:
#     collageName = 'MU Collage'

# class Student(Collage):
#     studentName = None

# a1 = Student()
# print(a1.studentName)
# print(a1.collageName)

class Car:

    model = None
    brand = None

    def __init__(self,model,brand):
        self.model = model
        self.brand = brand

    def details(self):
        return f'model = {self.model} , brand = {self.brand}'


class ElectricCar(Car):
    def __init__(self,model,brand,batterySize):
        super().__init__(model,brand)
        self.batterySize = batterySize
    
    def electricDetails(self):
        return f'model = {self.model} , brand = {self.brand} , batterySize = {self.batterySize}'
    
ecar1 = ElectricCar("MG" , 'Honda','300kwh')
print(ecar1.__dict__)
print(ecar1.model)
print(ecar1.brand)
print(ecar1.batterySize)
print(ecar1.details())
print(ecar1.electricDetails())


