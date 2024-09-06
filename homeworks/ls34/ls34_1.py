class Employee:
    def __init__(self, employee_id, name, salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__salary = salary

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id
    
    def set_name(self, name):
        self.__employee_id = name

    def get_name(self):
        return self.__name
    
    def set_salary(self, salary):
        if salary >= 0:
            self.__employee_id = salary
        
    def get_salary(self):
        return self.__salary

