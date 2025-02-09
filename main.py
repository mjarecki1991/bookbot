def print_terminal(file_contents):
    print(file_contents)





def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print_terminal(file_contents)
        
if __name__ == "__main__":
    main()