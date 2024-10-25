import string

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

    print (f"{count} words found in the document")

def count_characters(file_contents):

    char_dict = {}
    abc_chars = string.ascii_lowercase
    string_words = str(file_contents)
    string_lower = string_words.lower()

    for x in abc_chars:

        char_dict[x] = 0

    for x in string_lower:

        if x in char_dict:

            char_dict[x] += 1
    return char_dict

def sort_on(d):
    return d["num"]

def dict_to_list(char_dict):

    sorted_list = []
    for x in char_dict:
        sorted_list.append({"char": x, "num": char_dict[x]})
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list




def main():

    book_path = "books/frankenstein.txt"
    f = open_file()
    char_dict = count_characters(f)
    sorted_list = dict_to_list(char_dict)



    print (f"--- Begin report of {book_path} ---")
    count_words(f)
    print()

    for item in sorted_list:

        if not item['char'].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

main()