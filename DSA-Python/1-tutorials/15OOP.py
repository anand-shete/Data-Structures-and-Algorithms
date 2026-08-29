# Object-Oriented Programming (OOP) in Python is a programming paradigm that organizes code into objects, which are instances of classes. 
# OOP is based on four main principles: Encapsulation, Abstraction, Inheritance, and Polymorphism
# Class: A blueprint or template that defines a set of attributes and methods that an object of that class must have.
# Object: An instance of a class, containing the data (attributes) and behavior (methods) defined by the class.


class Person:
    name = "Harry"      # Class attribute
    height = 1.8        # Class attribute
    
obj = Person()          # creating instance of a class (an object)
obj.gender = 'F'        # This is an instance attribute
print(obj.name, obj.height , obj.gender)
print()


class Dog:
    # Constructor to initialize the object
    def __init__(self, name, breed):       # __init__ is a special method known as the constructor, called automatically when a new object is created. It initializes instance attributes.
    # self is a reference to the current instance of the class and allows access to new instance's attributes and methods
        self.name = name        # Instance attribute (defined using __init__ keyword)
        self.breed = breed      # Instance attribute

    def bark(self):         # self always need to be passed except in static methods
        return f"{self.name} says Woof!"
    
    @staticmethod           # Static methods belong to the class itself and not to its instances.
    def greet():
        return "Good morning"    
    
dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.bark())  
print(dog1.greet())         # calling the static method
print()



# Encapsulation is the practice of bundling data (attributes) and methods (functions) that operate on that data into a single unit (a class). This also restricts direct access to some of the object’s components.
# In Python, we achieve encapsulation by marking certain attributes or methods as private by prefixing them with a single or double underscore:
class Account:
    def __init__(self, owner="", balance=0):       # we can pass default values to a constructor which assigns the type to that variable   
        self.owner = owner
        self.__balance = balance                # _ suggests that its a Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        else:
            return "Insufficient balance"

    def get_balance(self):
        return self.__balance

# __balance is a private attribute, meaning it should not be accessed directly outside the class.
# We provide a method get_balance() to retrieve the balance safely, which enforces encapsulation.
user = Account("Nobody" , 34)               
print(user.owner)
# print(acc.owner, acc.__balance)      # Error - cannot access private properties outside a class
print(user.get_balance())              # We can if we define a method for it




# Abstraction is the concept of hiding complex details and only exposing what is necessary. This is often achieved by defining methods that represent actions without revealing the underlying implementation details.
# In the Account class above, methods like deposit() and withdraw() provide a simple interface for interacting with the balance, without exposing the underlying data or implementation details
user = Account("John")                  # Python dynamically manages variables, and when we assign a new value to an existing variable, the old reference is simply overwritten.
user.deposit(500)
print(user.get_balance())   
print()




# Inheritance allows a child class to inherit attributes and methods from its parent class, promoting code reuse. The child class can also override or extend the behavior of the parent class.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I make sounds."

# Dog class inherits from Animal
class Dog(Animal):
    def __init__(self, name):      
        super().__init__(name)      # If the parent class has an __init__ method, we must call it explicitly using super().__init__() inside the child class. It contains properties from parent class other than self
        
    def bark(self):             # self allows access to instance attributes inherited from class Animal
        return f"{self.name} says Woof!"
tom = Dog("Tommy")
print(tom.speak())              # Dog inherited properties and methods, so it has access to speak method
print(tom.bark())  

# class Class can inherit from class Animal and Dog both, iff both classes dont have existing inheritance relation between them.
# class Cat(Animal, Dog):   # Error - Python doesn’t know which Animal class to prioritize, causing an MRO conflict.
class Cat(Animal): 
    def speak(self):        # Inherited class modifying the method inside parent class
        return f"{self.name} says Meow!"
cat = Cat("kitten")
print(cat.speak())
print()




# The super() keyword in Python is used to call a method from a parent (or superclass) in a child (or subclass). This is particularly helpful in inheritance, as it enables us to access the superclass's methods and attributes without directly referencing the superclass by name.
class Employee:
    def __init__(self):
        print("This is a constructor of class Employee")
    a=34
    
class Programmer(Employee):
    def __init__(self):
        super().__init__()  # Calling __init__ method from parent
        print("This is a constructor of class Programmer")
    b=67
        
emp = Programmer()
print(emp.a)    
print(emp.b)  
print()




# Special Methods (Dunder Methods)
# Python classes include special methods (often called "magic methods") that allow objects to integrate with Python's built-in functions and operators. These methods are defined with double underscores:
# __str__() is called when we print the new object.
# __repr__() is string representation of an object, generally used for debugging.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

book = Book("1984", "George Orwell")
print(book)       
print(repr(book))  
print()




# Composition
# Composition is a design principle where a class is composed of other classes to build complex types. Instead of using inheritance, composition allows for creating objects that contain other objects.
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self): 
        self.engine = Engine() 

    def drive(self):
        return self.engine.start() + " and car is moving"

car = Car()
print(car.drive())  
print()





# @classmethod decorator
class Employee:
    a=34
    def show1(self):     # class attrubite has no control here
        print("The value of a is ",self.a)
    
    @classmethod
    def show2(cls):      # If we dont want the instance attribue to change my value
        print("The value of a is ",cls.a)
    
    
emp = Employee()
emp.a = 56      # instance attribue is changing my value
emp.show1()
emp.show2()




# @property decorator
# The @property decorator is very important in Python because it allows us to define methods that can be accessed like attributes, while still maintaining control over getting, setting, and deleting values. This is commonly used for encapsulation, where we want to restrict direct access to an attribute but still need to allow it to be accessed and modified indirectly
class Employee:
    @property
    def name(self):
        return f"{self.fname} + {self.lname}"
    
    @name.setter
    def name(self, name):
        self.fname = name.split(" ")[0]
        self.lname = name.split(" ")[1]
        
x = Employee()
x.name = "Mohit Aggrawal"
print(x.fname , x.lname)
print()




print('Practice Set: ')
class Programmer:
    def __init__(self, name,id,lang):
        self.name = name
        self.id = id
        self.language = lang
        self.company = "Microsoft Inc. "
Employee1 = Programmer("Hitesh", "122A8034", "C++")
print(Employee1.name, Employee1.id, Employee1.language, Employee1.company)
print()


# Q2: create a class which contains methods to calculate squares, cubes, and square roots of a give number
class Calculator:
    def __init__(self, num):
        self.number = num
    def square(self):
        return self.number * self.number
    def cube(self):
        return self.number * self.number * self.number
    def squareRt(self):
        return self.number ** (1/2)
n1 = Calculator(9.45)
print(n1.square())
print(n1.cube())
print(n1.squareRt())
print()

# Create a class 2DVector and use it to create another class 3DVector
class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        
class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):           # This constructor is for ThreeDVector Class 
        super().__init__(i,j)           # This constructor is for TwoDVector Class
        self.k = k
        
    def display(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
vector3D = ThreeDVector(3,4,5)
print(vector3D.display())
print()


# create class Pets from class Animals and further create a class Dog from Pets. Add method bark to class Dog
class Animals:
    def __init__(self,name):
        self.name =name

class Pets(Animals):
    def __init__(self,name):
        super().__init__(name)
        
class Dog(Pets):
    def __init__(self,name):
        super().__init__(name)
    
    def bark(self):
        return f"{self.name} barks "
dog = Dog("Newton")
print(dog.bark())


# create class Employee and add salary and increment properties to it. create method calaryAfterIncrement with @property decorator with a setter that changes value of increment based on salary


# create class Complex to represent complex numbers along with overload operators + and * which adds and multiples them

# create class Vector representing a vector of n dimensions. Overload the + and * operators which calculate the sum and dot product of these vectors

# 