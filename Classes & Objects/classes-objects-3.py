class Person:

    name = None  # attributes / class attributes 
    age = None 
    height = None 

    def __init__(self,name,age,height):
        print("__init__ : ", name,age,height)
        # name = name # both have same name 
        # age = age
        # height = height
        self.name = name 
        self.age = age 
        self.height = height

    def getSummary(self):
        pass

    def getHeight(self):
        pass 

    def getName(self):
        pass

    def getAge(self):
        pass 


hamza = Person('Hamza',20,'110cm') # creating an object of Person Class 
print(hamza.name) # Hamza
print(hamza.age) # 20
print(hamza.height) # 110cm

print('-----------------------------------------------')

john = Person('Jhon',40,'100cm') # creating an object of Person Class
print(john.name) # Jhon
print(john.height) # 100cm
print(john.age) # 40

print('------------------------------------------')

aradhya = Person('aradhya',20,'45cm')
print(aradhya.name)
print(aradhya.age)
print(aradhya.height)

print('-------------------------------------------')

# kevin = Person() # TypeError: __init__() missing 3 required positional arguments: 'name', 'age', and 'height' 

kevin = Person(20,'Kevin','40cm')
# arguments passed in wrong order

print('name',kevin.name)
print('age',kevin.age)
print('height',kevin.height)

