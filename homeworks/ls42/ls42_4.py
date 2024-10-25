class ScoreDescriptor:
    def __init__(self):
        self.__score = 0

    def __get__(self, instance, owner):
        return self.__score

    def __set__(self, instance, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("Score must be between 0 and 100")


class Student:
    score = ScoreDescriptor()

    def __init__(self, name, score):
        self.name = name
        self.score = score


s1 = Student("James", 70)
print(s1.score)
s1.score = 89
print(s1.score)
