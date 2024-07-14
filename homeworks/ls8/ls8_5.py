strings = ["apsd", "gfdhgfh", "sdf", "sdf", "aspd", "apsd", "sdf"]

string_counts = {}

for string in strings:
    if string in string_counts:
        string_counts[string] += 1
    else:
        string_counts[string] = 1

for string in string_counts:
    print(f"'{string}' - {string_counts[string]} ")

