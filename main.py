def open_file():

    with open("books/frankenstein.txt") as f:

        file_contents = f.read()

    print(file_contents)

def main():

    open_file()

main()