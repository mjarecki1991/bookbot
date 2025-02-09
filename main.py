def print_terminal(file_contents):
    print(file_contents)

def count_words(file_contents):
    words = file_contents.split()
    counter = 0

    for word in words:
        counter += 1

    print(f"Total word count is: {counter}")







def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print_terminal(file_contents)
        count_words(file_contents)
        
if __name__ == "__main__":
    main()