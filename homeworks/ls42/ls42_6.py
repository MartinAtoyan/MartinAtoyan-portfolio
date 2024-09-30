class SalaryDescriptor:

    def __init__(self, max_salary):
        self.max_salary = max_salary
        self.salary = 0

    def __get__(self, instance, owner):
        return self.salary

    def __set__(self, instance, salary):
        if 0 < salary < self.max_salary:
            self.salary = salary
        else:
            raise "Salary must be more than 0 and less then maximum salary"


class Employee:
    salary = SalaryDescriptor(5000)

    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary


emp1 = Employee("James", 2500)
print(emp1.salary)
emp1.salary = 3000
print(emp1.salary)
emp1.salary = 6000
print(emp1.salary)
