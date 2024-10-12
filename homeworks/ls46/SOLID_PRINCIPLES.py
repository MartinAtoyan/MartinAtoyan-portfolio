"""SOLID PRINCIPLES"""

"""S - Single Responsibility Principle. A class should have only one reason to change"""
"""Bad example"""
# class Car:
#     def __init__(self, color, year):
#         self.color = color
#         self.year = year
#
#     def unlock_vehicle(self):
#         print("Car unlocked")
#
#     def StartEngine(self):
#         print("Engine started")
#
"""Refactor"""
# class Car:
#     def __init__(self, color, year):
#         self.color = color
#         self.year = year
#
#     def unlock_vehicle(self):
#         print("Car unlocked")
#
# class Start_Engine:
#     def Start_engine(self, car:Car):
#         print(f"{car}'s engine started")

"""O - Open/Close Principle. Open for extension, closed for changes"""
"""Bad example"""
# class AreaCalculator:
#     def calculate(self, shape):
#         if shape['type'] == 'circle':
#             return 3.14 * shape['radius'] ** 2
#         elif shape['type'] == 'rectangle':
#             return shape['width'] * shape['height']

"""Refactor"""
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height


"""L - Luskov Substitution Principle. Child classes must be substitutable for their base or parent classes"""
"""Bad example"""
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def set_width(self, width):
#         self.width = width
#
#     def set_height(self, height):
#         self.height = height
#
#     def area(self):
#         return self.height * self.width
#
# class Square(Rectangle):
#     def set_width(self, width):
#         self.width = width
#
#     def set_height(self, height):
#         self.width = height
#
#     def area(self):
#         return self.width * self.height

"""Refactor"""
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# class Square:
#     def __init__(self, a):
#         self.side = a
#
#     def area(self):
#         return self.side * self.side



"""I - Interface Segregation Principle """
"""Bad example"""
# from abc import abstractmethod
# class vehicle:
#     def __init__(self, color):
#         self.color = color
#
#     @abstractmethod
#     def fly(self):
#         pass
#
# class Bike(vehicle):
#     def __init__(self, color):
#         self.color = color
#
#     def fly(self):
#         print("Bike can't fly")
#
# class Plane(vehicle):
#     def __init__(self, color):
#         self.color = color
#
#     def fly(self):
#         print("Plane is flying")

"""Refactor"""
# class vehicle:
#     def __init__(self, color):
#         self.color = color
#
# class Bike(vehicle):
#     def __init__(self, color):
#         self.color = color
#
# class Plane(vehicle):
#     def __init__(self, color):
#         self.color = color
#
#     def fly(self):
#         print("Plane is flying")



"""D - Dependency Inversion Principle"""
"""Bad example"""
# class EmailNotifier:
#     def send_email(self, message):
#         print(f"Sending email: {message}")
#
# class NotificationService:
#     def __init__(self):
#         self.notifier = EmailNotifier()
#
#     def notify(self, message):
#         self.notifier.send_email(message)

"""Refactor"""
# from abc import ABC, abstractmethod
#
# class Notifier(ABC):
#     @abstractmethod
#     def send(self, message):
#         pass
#
# class EmailNotifier(Notifier):
#     def send(self, message):
#         print(f"Sending email: {message}")
#
# class SMSNotifier(Notifier):
#     def send(self, message):
#         print(f"Sending sms: {message}")
#
# class NotificationService:
#     def __init__(self, notifier: Notifier):
#         self.notifier = notifier
#
#     def notify(self, message):
#         self.notifier.send(message)



