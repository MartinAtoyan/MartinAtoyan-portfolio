users_di = {}
users_ls = []

user1 = {
    "user_id": 68,
    "first_name": "James",
    "last_name": "Bond",
    "email": "jmsbnd@gml.com",
    "password": "password",
    "phone": "+374567890"
}

user2 = {
    "user_id": 86,
    "first_name": "Meri",
    "last_name": "Smith",
    "email": "mrsmth@gml.com",
    "password": "password6",
    "phone": "+374654321"
}

users_di[user1["first_name"]] = user1
users_di[user2["first_name"]] = user2

users_ls.append(user1)
users_ls.append(user2)

user_for_found = "James"
if user_for_found in users_di:
    user_found = users_di[user_for_found]
else:
    user_found = "Not found"

print(user_found)

user_for_found = "Ann"
if user_for_found in users_di:
    user_found = users_di[user_for_found]
else:
    user_found = "Not found"

print(user_found)

