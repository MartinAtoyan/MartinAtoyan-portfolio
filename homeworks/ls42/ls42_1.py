class Person:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age >= 0 and isinstance(age, int):
            self.__age = age
        else:
            raise ValueError("Age must be positive integer")


