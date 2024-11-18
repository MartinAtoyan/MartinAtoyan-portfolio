# 1 and 2 
{

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model 
#         self.year = year

#     def __repr__(self):
#         return f"{self.year}, {self.make}, {self.model}"    
#     # (str-user firendly) (repr-programmer)

# car = Car("Toyota", "Corolla", 2021)
# print(car) 
}

# 3 Encapsulation
{

# '''
# Attributes and methods 
# that should not be accessed 
# or modified directly by external 
# code are made private (often 
# indicated by a leading underscore, 
# like _attribute or __attribute in Python).

# Public methods (also called "getter" and "setter" 
# methods) provide controlled access to these private 
# attributes, allowing the user to interact with the data
#  in a safe, controlled way.
# '''
}

# 4 how do you make attribute private within a class?
{
"""We can make attribute private with dunder in init, with propperty decorator and with setter public method"""

# class Person:
#     def __init__(self, name):
#         self.__name = name

# p1 = Person("James")
# print(p1.__name)

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def name(self, value):
#         if isinstance(value, str) and len(value) >= 1:
#             self.__name = value

# p1 = Person("James")
# p1.name = "Daniel"
# print(p1.name)

# class Person:
#     def __init__(self, name):
#         self.__name = name

#     @property
#     def name(self):
#         return self.__name
    
#     @name.setter
#     def name(self, value):
#         if isinstance(value, str) and len(value) >= 1:
#             self.__name = value
#         else:
#             raise ValueError
        
# p1 = Person("James")
# print(p1.name)

}

# 5 Method vs Function

{
""" 
Function aranc instance-i a ashxatum

Methods - staticmethod, classmethod, simple

staticmethod - kap chuni class-i instanci het
classmethod - menak class attributneri het a gorc anum
simple - foo(self)

"""

# class MyStaticMethod:
#     def __init__(self, function):
#         self.function = function

#     def __get__(self, instance, owner):
#         # `instance` is the instance of the class, `owner` is the class itself
#         # We ignore `instance` here because static methods do not depend on any instance.
#         return self.function  # Just return the function itself

# class MyClassMethod:
#     def __init__(self, function):
#         self.function = function

#     def __get__(self, instance, owner):
#         # `owner` is the class itself, which we pass as the first argument (cls) to the function
#         def method(*args, **kwargs):
#             return self.function(owner, *args, **kwargs)
#         return method


}

# 6 Define a class ElectricCar that inherits from Car and adds an attribute battery_size.
{
# class Car:
#     def __init__(self, make, model):
#         self.make = make 
#         self.model = model 

#     def drive(self):
#         print("driving") 

# class ElectricCar(Car):
#     def __init__(self, make, model, battery_size):
#         super().__init__(make, model)
#         self.battery_size = battery_size

}

# 7 polymorphism basics 

{
'''
 Different classes can define 
 methods with the same name, and the method that gets 
 called depends on the type of the object calling it. 
 In Python, polymorphism is achieved through method overriding and duck typing.

 "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."
'''

# class Duck:
#     def quack(self):
#         return "Quack"
    
# class Person:
#     def quack(self):
#         return "i'm quacking like a duck"
    
# def make_it_quack(instance):
#     print(instance.quack())

# duck = Duck()
# person = Person()

# make_it_quack(duck)
# make_it_quack(person)

}

# 8 @classmethod and @staticmethod

{
# class Car:
#     total_cars = 0

#     def __init__(self, make, year):
#         self.make = make 
#         self.year = year
#         Car.total_cars += 1

#     @staticmethod
#     def filter(year):
#         return year > 2000
    
#     @classmethod
#     def get_total_cars(cls):
#         return f"Total cars: {cls.total_cars}"
    

# car1 = Car("Honda", 2001)
# car2 = Car("Toyota", 1990)
# car3 = Car("Nissan", 2022)

# print(Car.total_cars)
# print(car1.filter(2001))
# print(car2.filter(1990))
# print(car3.filter(2022))
}

# 9 What is composition in OOAD? Create a Battery class and use composition in the ElectricCar class to include Battery as an attribute
{
# ''' Strong life cycle '''

# class Battery:
#     def __init__(self, mah, kw):
#         self.mah = mah
#         self.kw = kw

# class ElectricCar:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#         self.battery = Battery(5000, 150)
}

# 10 Abstract class
{
# from abc import ABC, abstractmethod

# class vehicle(ABC):
#     def __init__(self, make):
#         self.make = make

#     @abstractmethod
#     def drive(self):
#         pass
}

# 11 Multiple inheritance
{
# class A:
#     def show(self):
#         print("This is from class A.")

# class B:
#     def show(self):
#         print("This is from class B.")

# class C(A, B):  # Inherits from both A and B
#     pass
}

# 12 MRO

# 13 inheritance vs composition
{
''''
inheritance "is-a" relationship. When you inherit a class, you can use his methods and attributes.

compositon "has-a" relationship. When composit two objects. You use a methods and attributes of instance that initalizes from class

'''
}

# 14 Class and static method / verevy ka

# 15 @property 

{
'''
define methods in a class that can be accessed like attributes.
'''

# class CustomProperty:
#     def __init__(self, getter=None, setter=None, deleter=None):
#         self.getter = getter
#         self.setter = setter
#         self.deleter = deleter

#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         if self.getter is None:
#             raise AttributeError("Attribute is not readable")
#         return self.getter(instance)

#     def __set__(self, instance, value):
#         if self.setter is None:
#             raise AttributeError("Attribute is not writable")
#         self.setter(instance, value)

#     def __delete__(self, instance):
#         if self.deleter is None:
#             raise AttributeError("Attribute is not deletable")
#         self.deleter(instance)

#     def getter(self, func):
#         self.getter = func
#         return self

#     def setter(self, func):
#         self.setter = func
#         return self

#     def deleter(self, func):
#         self.deleter = func
#         return self
}

# 16 Design pattern - factory


# 17 Design pattern - singleton

{
# class coustomSingleton:
#     __instance = None
#     def __new__(cls):
#         if cls.__instance is None:
#             cls.__instance = super().__init__(cls)
#         return cls.__instance
}

# 18 Data encapsulation

{
# class BankAccount:
#     def __init__(self, account_number, balance):
#         # Private attributes
#         self.__account_number = account_number  # Protected with double underscore

#     # Getter for account number
#     def get_account_number(self):
#         return self.__account_number
}

# 19 Point class __eq__

{
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
    
# p1 = Point(1, 2)
# p2 = Point(1, 2)
# print(p1 == p2)
}

# 20 Vector1 + Vector2 + Vector3

{
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
    
#     def __str__(self):
#         return f"Vector ({self.x}, {self.y})"


# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# v3 = Vector(5, 6)
# print(v1 + v2 + v3)
}

# 21 Duck typing
{
# def make_it_speak(obj):
#     if hasattr(obj, "speak"):
#         return obj.speak()

# class Dog:
#     def speak(self):
#         return "Woof"
    
# class Cat:
#     def speak(self):
#         return "Meow"
    
# class Human:
#     def speak(self):
#         return "Hello"
    
# dog = Dog()
# cat = Cat()
# person = Human()

# print(make_it_speak(dog))
# print(make_it_speak(cat))
# print(make_it_speak(person))
}

# 22 Abstract Base Class(ABC)

{

# from abc import ABC, abstractmethod

# class shape(ABC):
#     def __init__(self, side1, side2):
#         self.side1 = side1
#         self.side2 = side2


#     @abstractmethod
#     def area(self):
#         return self.side1 * self.side2
    
}

# 23 open-clsoe

{
# '''open for extend, close for changes'''

# from abc import ABC, abstractmethod

# class PaymentMethod(ABC):
#     @abstractmethod
#     def process_payment(self):
#         pass

# class CreditCardPayment(PaymentMethod):
#     def process_payment(self):
#         print("Processing credit card payment")

# class PayPalPayment(PaymentMethod):
#     def process_payment(self):
#         print("Processing PayPal payment")

# class CryptoPayment(PaymentMethod):
#     def process_payment(self):
#         print("processing crypto payment")

# class PaymentProcessor:
#     def process(self, payment_method: PaymentMethod):
#         if isinstance(payment_method, PaymentMethod):
#             payment_method.process_payment()
#         else:
#             raise TypeError
}        

# 24 interface segregation
{
# class Printer:
#     def print_doc(self):
#         print("Printing document")

# class Scanner:
#     def scan_doc(self):
#         print("Scanning document")

# class Supermachine(Printer, Scanner):
#     def __init__(self, printer:Printer, scanner:Scanner):
#         self.printer = printer
#         self.scanner = scanner
}

# 25 Dependency injection 
{
# class Sender:
#     def send(self, message):
#         raise NotImplementedError("Subclass must implement this method")
    
# class EmailSender(Sender):
#     def send(self, message):
#         print(f"Send: {message}")

# class SMSsender(Sender):
#     def send(self, message):
#         print(f"send: {message}")

# class Notification:
#     def __init__(self, sender: Sender):
#         self.sender = sender

#     def notify(self, message):
#         self.sender.send(message)

}

# 26 Template method
{
# from abc import ABC, abstractmethod

# class Recipe(ABC):
#     """Abstract base class that defines the template method"""

#     def prepare_dish(self):
#         """Template method defining the skeleton of the recipe"""
#         self.gather_ingredients()
#         self.prepare_ingredients()
#         self.cook()
#         self.serve()

#     @abstractmethod
#     def gather_ingredients(self):
#         """Step to gather ingredients (to be implemented by subclasses)"""
#         pass

#     @abstractmethod
#     def prepare_ingredients(self):
#         """Step to prepare ingredients (to be implemented by subclasses)"""
#         pass

#     @abstractmethod
#     def cook(self):
#         """Step to cook the dish (to be implemented by subclasses)"""
#         pass

#     @abstractmethod
#     def serve(self):
#         """Step to serve the dish (to be implemented by subclasses)"""
#         pass


# # Concrete implementation for preparing pasta
# class PastaRecipe(Recipe):
#     def gather_ingredients(self):
#         print("Gathering ingredients for pasta: pasta, tomatoes, garlic, olive oil, basil")

#     def prepare_ingredients(self):
#         print("Chopping garlic and tomatoes, boiling water for pasta")

#     def cook(self):
#         print("Cooking pasta and preparing tomato sauce")

#     def serve(self):
#         print("Serving pasta with tomato sauce and fresh basil")


# # Concrete implementation for preparing salad
# class SaladRecipe(Recipe):
#     def gather_ingredients(self):
#         print("Gathering ingredients for salad: lettuce, cucumber, tomatoes, olive oil, lemon juice")

#     def prepare_ingredients(self):
#         print("Washing and chopping vegetables")

#     def cook(self):
#         print("Tossing vegetables with olive oil and lemon juice (no actual cooking)")

#     def serve(self):
#         print("Serving fresh salad in a bowl")


# # Client code
# print("Preparing Pasta:")
# pasta = PastaRecipe()
# pasta.prepare_dish()

# print("\nPreparing Salad:")
# salad = SaladRecipe()
# salad.prepare_dish()
}

# 27 overload operator __lt__
{
# class Employee:
#     def __init__(self, age):
#         self.age = age

#     def __lt__(self, other):
#         return self.age < other.age
    
# p1 = Employee(25)
# p2 = Employee(60)

# print(p1 < p2 )
}

# Proxy Pattern 

{
# class RealImage:
#     def __init__(self, filename):
#         self.filename = filename
#         self._load_image()

#     def _load_image(self):
#         print(f"Loading image from: {self.filename}")

#     def display(self):
#         print(f"Displaying: {self.filename}")

# class ProxyImage:
#     def __init__(self, filename):
#         self.filename = filename
#         self._real_image = None

#     def display(self):
#         if self._real_image is None:
#             print("Initializing the real image")
#             self._real_image = RealImage(self.filename)
#         self._real_image.display()

    
# proxyIamge = ProxyImage("large.jpg")
# proxyIamge.display()

# proxyIamge.display()
}

