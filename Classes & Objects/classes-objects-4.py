class Car:
    
    model = None       # class attribute
    company = None

    def __init__(self,company,model):
        # print(self.model,self.company)
        self.model = model
        self.company = company

    def details(self):
        return f"model = {self.model} , company = {self.company}"

car1 = Car(company = 'Toyota', model = 'RE-100')
print(car1.company)
print(car1.model)
print(car1.details())
