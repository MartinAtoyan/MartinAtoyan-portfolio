class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Person's name is {self.name} \nPerson's age is {self.age}")


person = Person("James", 25)
person.display_details()
