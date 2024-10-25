from Car import *
from Customer import customer

class SaleOperation:
    @abstractmethod
    def add_car(self, car:Car):
        pass

    @abstractmethod
    def rem_car(self, car:Car):
        pass

    @abstractmethod
    def view_inventory(self):
        pass

class Salespeople(SaleOperation):
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        self.inventory = []
        self.sales_history = []


    def name(self, value):
        if isinstance(value, str) and len(value) > 1:
            self.name = value
        else:
            raise ValueError("Name must be string.")

    def rate(self, value):
        if isinstance(value, float) and 0 < value < 1:
            self.rate = value
        else:
            raise ValueError("Rate must be float number between 0 and 1.")

    def add_car(self, car: Car):
        if isinstance(car, Car):
            self.inventory.append(car)
        else:
            raise ValueError("You can add only Car type objects.")

    def rem_car(self, car: Car):
        if isinstance(car, Car):
            self.inventory.remove(car)
        else:
            raise ValueError("You can remove only Car type objects.")

    def view_inventory(self):
        return self.inventory

    def sell_car(self, car, buyer: customer):
        buyer.buy_car(car)
        self.sales_history.append(car)
        print(f"{self.name} sold {car.make}, {car.model} to {buyer.name} for {car.price}$.")

    def view_sales_history(self):
        if not self.sales_history:
            print(f"{self.name} has no sales yet.")
        else:
            print(f"{self.name}'s Sales History:")
            for car in self.sales_history:
                print(f"({car.make}, {car.model} - {car.price}$)")