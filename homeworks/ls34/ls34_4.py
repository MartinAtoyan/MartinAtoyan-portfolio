class ShoppingCart:
    def __init__(self):
        self.__items = []
        # self.__price =

    def add_item(self, name: str, price: float):
        item = {"name": name, "price": price}
        self.__items.append(item)
        print(f"You added to cart {name}")

    def remove_item(self, name: str):
        for item in self.__items:
            if item["name"] == name:
                self.__items.remove(item)
        print(f"Your removed from cart {name}")

    def item_count(self):
        return len(self.__items)

    def display_cart(self):
        if not self.__items:
            print("The cart is empty.")
        else:
            for item in self.__items:
                print(f'{item["name"]}: {item["price"]:}')

        print(f"Total number of items: {self.item_count()}")
        value = 0
        for item in self.__items:
            value += item["price"]
        print(f"Total amount is {value} \n")

box = ShoppingCart()
box.display_cart()

box.add_item("table", 250)
box.display_cart()

box.add_item("chair", 200)
box.display_cart()

box.remove_item("table")
box.display_cart()

