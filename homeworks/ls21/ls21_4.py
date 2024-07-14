

file_name = "text.txt"
rep = open(file_name, "r")
words = ["example", "all", "word", "up", "did", "him"]

word_counts = {word: 0 for word in words}

contents = file_name.read()
contents = contents.lower()

words = contents.split()

for word in words:
    if word in word_counts:
        word_counts[word] += 1

for word, count in word_counts.items():
    print(word_counts)
