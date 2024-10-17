# ls_1 = [5, 20, 15, 11, 84, 6, 2, 63]
# print(ls_1)

def insertion_sort(ls):
    size = len(ls)

    for i in range(1, size):
        temp = ls[i]
        j = i - 1

        while j >= 0 and temp < ls[j]:
            ls[j + 1] = ls[j]
            j-=1
        ls[j + 1] = temp

# insertion_sort(ls_1)
# print(ls_1)


class Student:
    __slots__ = ("__name", "__age")

    def __init__(self, name, age):
        self.age = age
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" and len(value) <= 1:
            raise ValueError("Student's name can't be empty and les or equal than one letter")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if not isinstance(age, int) and age <= 0:
            raise ValueError("Age must be positive integer")
        self.__age = age

    def __lt__(self, other):
        return self.__age < other.__age

    def __le__(self, other):
        return self.__age <= other.__age

    def __str__(self):
        return f"{self.__name} : {self.__age}"

    def __repr__(self):
        return f"{self.__name} : {self.__age}"



if __name__ == "__main__":
    s1 = Student("Ann", 45)
    s2 = Student("James", 12)
    s3 = Student("Bob", 36)
    s4 = Student("Smith", 69)
    list_of_students = [s1, s2, s3, s4]
    insertion_sort(list_of_students)
    print(list_of_students)


def insertion_sort_modificated(ls):
    size = len(ls)

    for i in range(1, size):
        temp = ls[i]
        j = i - 1
        if ls[j] < temp:
            continue

        while j >= 0 and temp < ls[j]:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j + 1] = temp


ls_2 = [5, 4, 2, 10, 63, 8]
insertion_sort_modificated(ls_2)
print(ls_2)



