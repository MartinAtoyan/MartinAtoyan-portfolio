import Order, Customer, MenuItem

class Review:
    __slots__ = ('customer_name', 'order', 'rating', 'comments')

    def __init__(self, customer_name, order, rating, comments = None):
        self.customer_name = customer_name
        self.order = order
        self.rating = self.validate_rating(rating)
        self.comments = comments

    def validate_rating(self, rating):
        if 1 <= rating <= 10:
            return rating
        else:
            raise ValueError("Rating must be between 1 and 10.")

    def __str__(self):
        return (f"Review by {self.customer_name}:\n"
                f"Order: {self.order}\n"
                f"Rating: {self.rating}/10\n"
                f"Comments: {self.comments}")



if __name__ == "__main__":
    menu_items = [{'name': 'Pizza', 'price': 12.99}, {'name': 'Soda', 'price': 2.50}]
    dine_in_order = Order.DineInOrder('John Doe', menu_items, 5)

    review = Review(customer_name="John Doe", order=dine_in_order, rating=5, comments="Great food and service!")
    print(review)

