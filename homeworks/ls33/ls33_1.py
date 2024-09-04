class Person:
    def setter(self, name: str, age: int):
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Person's name is {self.name} \nPerson's age is {self.age}")


person = Person()
person.setter("James", 25)
person.display_details()
