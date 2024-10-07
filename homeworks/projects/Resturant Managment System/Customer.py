

class Customer:
    __slots__ = ("__name", "__contact_info", "__order_history")

    def __init__(self, name, contact_info, order_history):
        self.__name = name
        self.__contact_info = contact_info
        self.__order_history = order_history

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value:str):
        if type(value) == str and len(value) >= 1:
            self.__name = value
        else:
            raise ValueError("Name must be string")

    @property
    def contact_info(self):
        return self.__contact_info

    @contact_info.setter
    def contact_info(self, value: str):
        if value[0] == "+" and len(value) >= 11:
            self.__contact_info = value

    @property
    def order_history(self):
        return self.__order_history

    @order_history.setter
    def order_history(self, value: list):
        if type(value) == list and len(value) >= 1:
            self.__order_history = value


if __name__ == "__main__":
    p1 = Customer("James", "+37499001122", ["apple", "banana", "pineapple"])
    print(p1.name, p1.contact_info, p1.order_history)
