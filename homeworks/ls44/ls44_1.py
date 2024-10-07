class Person:
    __slots__ = ("name", "age", "email")

    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email


p1 = Person("James", 50, "Jamesbond@mail.com")
p1.name = "Brown"
p1.email = "asdasd@mail.com"
p1.age = 56
print(p1.__dict__)
p1.x = "abc"