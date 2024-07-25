def accept_updates(**kwargs):
    for key, value in kwargs.items():
        print(f"Parameter {key} was updated to {value}")

def user_setting_updater(id, **kwargs):
    print(f"Settings update for user's id: {id}")    

    accept_updates(**kwargs)

user_setting_updater(id = 5, first_name = "James", last_name = "Brown", age = 20)
print()
user_setting_updater(id = 5, first_name = "Jane", last_name = "Brown", age = 22)
