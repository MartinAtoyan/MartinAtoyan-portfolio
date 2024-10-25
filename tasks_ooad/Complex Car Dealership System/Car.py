from abc import abstractmethod, ABC

class Car(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class EV(Car):
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price


    def make(self, value):
        if isinstance(value, str) and len(value) >= 1:
            self.make = value
        else:
            raise ValueError("Brand name must be string and more than 1 letter. ")


    def model(self, value):
        if isinstance(value, str) and len(value) >= 1:
            self.model = value
        else:
            raise ValueError("Model name must be string and more than 1 letter. ")


    def price(self, value):
        if isinstance(value, float) and value >= 0:
            self.price = value
        else:
            raise ValueError("Price must be positive number. ")

    def start(self):
        print(f"EV - {self.make}, {self.model} started.")

    def stop(self):
        print(f"EV - {self.make}, {self.model} stopped.")

    def drive(self):
        print(f"EV - {self.make}, {self.model} is driving.")


class Hybrid(Car):
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price


    def make(self, value):
        if isinstance(value, str) and len(value) >= 1:
            self.make = value
        else:
            raise ValueError("Brand name must be string and more than 1 letter. ")


    def model(self, value):
        if isinstance(value, str) and len(value) >= 1:
            self.model = value
        else:
            raise ValueError("Model name must be string and more than 1 letter. ")


    def price(self, value):
        if isinstance(value, float) and value >= 0:
            self.price = value
        else:
            raise ValueError("Price must be positive number. ")

    def start(self):
        print(f"Hybrid - {self.make}, {self.model} started.")

    def stop(self):
        print(f"Hybrid - {self.make}, {self.model} stopped.")

    def drive(self):
        print(f"Hybrid - {self.make}, {self.model} is driving.")