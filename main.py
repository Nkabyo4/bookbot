def open_file():

    with open("books/frankenstein.txt") as f:

        file_contents = f.read()

    return file_contents

def count_words(file_contents):
    
    count = 0
    string_words = str(file_contents)
    split_words = string_words.split()

    for x in split_words:
        count += 1

    print (count)


def main():

    f = open_file()
    count_words(f)

main()