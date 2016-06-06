# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file not exists just return 0

def count_a(filename):
    try:
        f = open(filename)
        text = f.read()
        f.close()
        count_a = 0
        for letter_a in text:
            if letter_a == 'a':
                count_a += 1
        return count_a
    except FileNotFoundError:
        return 0

print(count_a('file.txt'))
