def get_char_count(char, filepath):
    with open(filepath) as readfile:
        count = [a for a in readfile.read() if char == a]
    return len(count)


print(get_char_count("a", "files/bear.txt"))
