class Car:
    model = None
    brand = None 

    def __init__(self,model,brand):
        self.model = model
        self.brand = brand 

class ElectricCar(Car):
    def __init__(self,model,brand,batterSize):
        super().__init__(model,brand)
        self.batterySize = batterSize

eCar1 = ElectricCar('RT-900','Tesla','900kwh')

print(eCar1.__dict__)



