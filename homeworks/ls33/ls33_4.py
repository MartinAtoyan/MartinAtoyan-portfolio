class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if self._age > 0:
            self._age = age
        else:
            print("please write your real age")

    def display_details(self):
        print(f"Person's name is {self.name} \nPerson's age is {self._age}")

person = Person("James", 25)
person.set_age(27)
person.display_details()
print(person.get_age())
