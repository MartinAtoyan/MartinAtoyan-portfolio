from Car import *
from Customer import customer
from SalesPeople import Salespeople

if __name__ == "__main__":

    car_one = EV("BYD", "SONG PLUS", 30000.0)
    car_two = Hybrid("TOYOTA", "VENZA", 40000.0)

    SaleManager = Salespeople("Bob", 0.08)
    SaleManager.add_car(car_one)
    SaleManager.add_car(car_two)
    SaleManager.view_inventory()


    customer_1 = customer("James", "096 96 96 96")

    SaleManager.sell_car(car_one, customer_1)

    customer_2 = customer("Ann", "077 77 77 77")
    SaleManager.sell_car(car_two, customer_2)


    customer_1.buy_car(car_one)
    customer_2.buy_car(car_two)

    print(customer_1.purchased_cars)
    print(customer_2.purchased_cars)



