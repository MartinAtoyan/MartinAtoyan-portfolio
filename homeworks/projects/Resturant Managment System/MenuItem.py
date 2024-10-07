

class MenuItem:
    __slots__ = ("__name", "__price", "__ingredients")

    def __init__(self, name:str, price:float, ingredients: list):
        self.__name = name
        self.__price = price
        self.__ingredients = ingredients

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.isalpha() and len(name) >= 1:
            self.__name = name
        else:
            raise ValueError("Name must be contains only letters")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if type(price) is float and price >= 0:
            self.__price = price
        else:
            raise ValueError("Price must be positive")

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, value):
        if type(value) is list and len(value) >= 1:
            self.__ingredients = value
        else:
            raise ValueError("Ingredients must be more or equal than one")


class Appetizer(MenuItem):
    __slots__ = ("__piece_of_food", )
    def __init__(self, name, price, ingredients, piece_of_food):
        super().__init__(name, price, ingredients)
        self.__piece_of_food = piece_of_food

    @property
    def piece_of_food(self):
        return self.__piece_of_food

    @piece_of_food.setter
    def piece_of_food(self, value: int):
        if type(value) is int and value >= 1:
            self.__piece_of_food = value
        else:
            raise ValueError("piece size must be positive integer")


class Entree(MenuItem):
    __slots__ = ("__style_food", )
    def __init__(self, name, price, ingredients, style_food):
        super().__init__(name, price, ingredients)
        self.__style_food = style_food

    @property
    def style_food(self):
        return self.__style_food

    @style_food.setter
    def style_food(self, style: str):
        if style.isalpha() and len(style) >= 1:
            self.__style_food = style
        else:
            raise ValueError


class Dessert(MenuItem):
    __slots__ = ("__with_sugar", )
    def __init__(self, name, price, ingredients, with_sugar):
        super().__init__(name, price, ingredients)
        self.with_sugar = with_sugar

    @property
    def with_sugar(self):
        return self.__with_sugar

    @with_sugar.setter
    def with_sugar(self, bool_value):
        if isinstance(bool_value, bool):
            if bool_value:
                self.__with_sugar = "With sugar"
            else:
                self.__with_sugar = "Without sugar"
        else:
            raise TypeError("with_sugar must be a boolean value.")

if __name__ == "__main__":
    appetizer = Appetizer("Spring Rolls", 5.99, ["vegetables", "wrappers"], "2 pieces")
    entree = Entree("Grilled Salmon", 18.99, ["salmon", "lemon", "herbs"], "grilled")
    dessert = Dessert("Chocolate Cake", 7.49, ["chocolate", "flour", "sugar"], True)

    print(appetizer.name, appetizer.price, appetizer.ingredients, appetizer.piece_of_food)
    print(entree.name, entree.price, entree.ingredients, entree.style_food)
    print(dessert.name, dessert.price, dessert.ingredients, dessert.with_sugar)