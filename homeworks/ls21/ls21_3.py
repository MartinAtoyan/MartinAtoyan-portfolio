file_name = "specific_position.txt"
text = "input text."
pos = 3

initial_text = "This is the initial text.\n"
open(file_name, "w")
file_name.write(initial_text)

file = open(file_name, "r+")

try:
    file.seek(pos)
    file.write(text)
finally:
    file.close()
