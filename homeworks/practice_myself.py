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



