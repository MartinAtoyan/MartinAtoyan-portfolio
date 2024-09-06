class Student:
    def __init__(self, name, roll_number) -> None:
        self.__name = name
        self.__roll_number = roll_number
        self.__grades = []


    def set_grade(self, grade):
        if grade in range(0, 101):
            self.__grades.append(grade)

    def calculate_average_grade(self):
        return sum(self.__grades) / len(self.__grades)
    
    def student_info(self):
        print(f"Student's name is {self.__name}")
        print(f"Student's roll number is {self.__roll_number}")
        print(f"Student's average grade is {self.calculate_average_grade()}")
