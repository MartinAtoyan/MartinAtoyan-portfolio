def reader(file, output_file):
    open_file = open(file, 'r')
    word_count = 0
    char_count = 0
    line_count = 0
    for line in open_file:
        line_count += 1
        word_count += len(line.split())
        char_count += len(line)

    res_of_counts = (
        f"Lines: {line_count}\n"
        f"Words: {word_count}\n"
        f"Characters: {char_count}\n"
    )

    # Write the statistics to the output file
    res = open(output_file, 'w')
    res.write(res_of_counts)
    print(res_of_counts)


reader("reader.txt", "result.txt")



