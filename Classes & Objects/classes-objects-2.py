class Person:

    name = None  # attributes / class attributes 
    age = None 
    height = None 

    def __init__(self,name,age,height):
        print("__init__ : ", name,age,height)
        pass 

    def getSummary(self):
        pass

    def getHeight(self):
        pass 

    def getName(self):
        pass

    def getAge(self):
        pass 


hamza = Person('Hamza',20,'110cm') # creating an object of Person Class 
print(hamza.name) # None
print(hamza.age) # None
print(hamza.height) # None

print('-----------------------------------------------')

john = Person('Jhon',40,'100cm') # creating an object of Person Class
print(john.name) # None
print(john.height) # None
print(john.age) # None