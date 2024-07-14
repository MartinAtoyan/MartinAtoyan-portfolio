file_name = "exclusive_mode.txt"

text = "input text\n"

try:
    file = open(file_name, "x")
    try:
        file.write(text)
    finally:
        file.close()
except FileExistsError:
    print(f"Error: The file '{file_name}' already exists.")
