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
    print (char_dict)
    return char_dict

def dict_to_list(char_dict):

    my_dict = char_dict
    print (my_dict)




def main():

    f = open_file()
    count_characters(f)
    dict_to_list(count_characters(f))

main()