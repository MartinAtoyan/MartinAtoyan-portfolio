class ValidatedString:
    def __init__(self):
        self.str = None

    def __get__(self, instance, owner):
        return self.str

    def __set__(self, instance, string):
        if len(string) <= 0:
            raise ValueError("String size must be more than 0")
        else:
            self.str = string


class User:
    username = ValidatedString()

    def __init__(self, username):
        self.__username = username


user1 = User("James")
user1.username = "Bob"
print(user1.username)
user1.username = ""
