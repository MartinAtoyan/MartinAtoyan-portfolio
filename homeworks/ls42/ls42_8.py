
def contains_number(value):
    for char in value:
        if char.isdigit():
            return True
    return False


class PasswordValidator:
    def __init__(self, contain_numb = True, min_size = 8):
        self.min_size = min_size
        self.contain_numb = contain_numb

    def __get__(self, instance, owner):
        return self.password

    def __set__(self, instance, value):
        if len(value) < self.min_size:
            raise ValueError(f"Password minimum size is {self.min_size}.")

        if self.contain_numb and not contains_number(value):
            raise ValueError("Password must contain minimum one number.")

        self.password = value

class Account:
    password = PasswordValidator(min_size=8, contain_numb=True)
    def __init__(self, username, password):
        self.username = username
        self.password = password


# user1 = Account("James15", "asdvasda516")
# user2 = Account("James15", "asdvas")

