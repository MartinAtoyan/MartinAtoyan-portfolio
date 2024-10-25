from Car import *

class customer:
    def __init__(self, name, cont_info):
        self.name = name
        self.cont_info = cont_info
        self.purchased_cars = []


    def name(self, value):
        if isinstance(value, str) and len(value) >= 1:
            self.name = value
        else:
            raise ValueError("Customer name must be string.")


    def cont_info(self, value):
        if isinstance(value, str) and len(value) >= 1:
            self.cont_info = value
        else:
            raise ValueError

    def buy_car(self, car: Car):
        self.purchased_cars.append(car)