from sys import argv 
script, user_name = argv

prompt = "- "

print(f"Hello {user_name}, I'm the {script} script")
print(f"Where do you work {user_name}?")
firm = input(prompt)

print(f"Where do you live {user_name}?")
location = input(prompt)


