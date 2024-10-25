# class Vehicle:
#     def __init__(self, brand: str, model: str):
#         self.brand = brand
#         self.model = model
#
#     def move(self):
#         print("move vehicle")
#
# class Car(Vehicle):
#     def move(self):
#         print("Car is moving")
#
# class Boat(Vehicle):
#     def move(self):
#         print("Boat is sailing")
#
# class Plane(Vehicle):
#     def move(self):
#         print("Plane is flying")
#
#
# car = Car("Bmw", "5 series")
# boat = Boat("mercury", "1250")
# plane = Plane("Boeing", "777")
#
# for x in (car, boat, plane):
#     x.move()
#     print(x.model, x.brand)
#

# class Book:
#     def __init__(self, title: str, author: str):
#         self.title = title
#         self.author = author
#
#     def book_info(self):
#         print(f"Book's name is {self.title} and author is {self.author}")
#
#
# class Shelf:
#     def __init__(self):
#         self.books = []
#
#     def add_book(self, book):
#         self.books.append(book)
#
#     def remove_book(self, book):
#         self.books.remove(book)
#
#     def show_books(self):
#         if self.books:
#             for book in self.books:
#                 book.book_info()
#         else:
#             print("Shelf is empty")
#
#
# book_1 = Book("Math_analys", "Phixtengolc")
# book_2 = Book("Algebra", "Proskuryakov")
#
# small_shelf = Shelf()
# small_shelf.show_books()
#
# small_shelf.add_book(book_1)
# small_shelf.show_books()
# small_shelf.add_book(book_2)
# small_shelf.show_books()
# small_shelf.remove_book(book_2)
# small_shelf.show_books()
# small_shelf.remove_book(book_1)
# small_shelf.show_books()


# class Singleton:
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance = super(Singleton, cls).__new__(cls)
#         return cls.__instance



class Mlass:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc  # Use __doc__ to store the documentation

    def __get__(self, instance, owner):
        if instance is None:
            return self  # When accessed through the class, return the descriptor itself
        if self.fget is None:
            raise AttributeError("The attribute is not readable")
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("The attribute is not writable")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("The attribute cannot be deleted")
        self.fdel(instance)

# Example Usage
class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    def del_name(self):
        print("Deleting name...")
        del self._name

    name = Mlass(get_name, set_name, del_name, "Property for managing the name")

# Usage
p = Person("Alice")
print(p.name)  # Output: Alice

p.name = "Bob"
print(p.name)  # Output: Bob

del p.name  # Output: Deleting name...




