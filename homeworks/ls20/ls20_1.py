users_info_list = []

username = input("Please input your username. ")
size_username = len(username)
reserved_names = ['admin', 'root', 'superuser', 'administrator']

if size_username < 5:
    print("Username is so long. Username must be between 5 and 20")
elif size_username > 20:
    print("Username is so short. Username must be between 5 and 20")
elif not username.isalnum():
    print("Username must contain letters and digits")
elif username in reserved_names:
    print("Username should not be reserved")
else:
    print("username is valid")
    users_info_list.append(username)

email = input("Please input your email. ")

index_dot = 0
index_sign = 0
for i in email:
    if i != "@":
        index_sign += 1
    else:
        break
for i in email:
    if i != ".":
        index_dot += 1
    else:
        break
res = index_dot - index_sign - 1

if "@" not in email and "." not in email:
    print("Your email is invalid. Email must have a ' @ ' and ' . '.")   
elif res <= 1:
    print("email is invalid")
elif len(email[index_dot + 1:]) <= 1:
    print("email is invalid")
elif len(email[:index_sign]) <= 1:
    print("email is invalid")
else:
    print("email is valid")
    users_info_list.append(email)
    

phone = input("Please input your phone. ")
temp = phone[1:]

if phone[0] == '0' and len(phone) == 9 and phone.isdigit():
    print("phone is valid")
elif phone[0] == "+" and len(phone) == 12 and temp.isdigit():
    print("phone is valid")
else:
    print("phone is invalid")
    print("phone number must look like this +374 XX XXX XXX or 0XX XXX XXX. X is digit")


password = input("Please input your password. ")
spec_sym = "!@#$%^&*"
digits = []
flag = 0
for i in range(10):
    digits.append(str(i))

if len(password) < 8:
    print("Your password shouldn't be shorter than 8 characters")

elif password.islower():
    print("Must contain at least one uppercase letter, one lowercase letter, one digit, and one special character (e.g., !@#$%^&*).")

elif password.isupper():
    print("Must contain at least one uppercase letter, one lowercase letter, one digit, and one special character (e.g., !@#$%^&*).")


for i in password:
    if i not in digits:
        flag = False
    else:
        flag = True
    if i not in spec_sym:
        flag = False
    else:
        flag = True


if flag != False:
    print("Your password is valid")
    users_info_list.append(password)
else: 
    print("Must contain at least one uppercase letter, one lowercase letter, one digit, and one special character (e.g., !@#$%^&*).")

if flag != False:
    repeat_password = input("Please repeat your password. ")
    if password == repeat_password:
        print("Repeated password is correct")
        users_info_list.append(repeat_password)
    else:
        print("Repeated password isn't correct") 