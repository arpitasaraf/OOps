class Person:

    name = None  # attributes / class attributes 
    age = None 
    height = None 

    def __init__(self,name,age,height):
        print("__init__ : ", name,age,height)
        self.name = name
        self.age = age
        self.height = height

    def getSummary(self):
        return f"your name is {self.name} , your age is {self.age} ,your height is {self.height} " 

    def getHeight(self):
        return f"your height is {self.height}"

    def getName(self):
        return f"your name is {self.name}"

    def getAge(self):
        return f"your age is {self.age}"


hamza = Person('Hamza',20,'110cm') # creating an object of Person Class 
print(hamza.name) # None
print(hamza.age) # None
print(hamza.height) # None
print(hamza.getSummary())
print(hamza.getName())
print(hamza.getAge())
print(hamza.getHeight())

print('-----------------------------------------------')

john = Person('John',40,'100cm') # creating an object of Person Class
print(john.name) # None
print(john.height) # None
print(john.age) # None
print(john.getSummary())
print(john.getName())
print(john.getAge())
print(john.getHeight())



