def read_file_lines(file_path):
    data = open(file_path, "r")
    for line in data:
        yield line

file_path = "test.txt"
object = read_file_lines(file_path)
for line in object:
    print(line.strip())