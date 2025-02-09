def print_terminal(file_contents):
    print(file_contents)

def count_words(file_contents):
    words = file_contents.split()
    counter = 0

    for word in words:
        counter += 1 

    print(f"Total word count is: {counter}")


    

def count_characters(file_contents):
    low_end = file_contents.lower()
    my_dict = {}
    
    for character in low_end:
        if character not in my_dict:
            my_dict[character] = 1
        else:
            my_dict[character] += 1

    print(f"{my_dict}")    
    return my_dict
    
    



def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print_terminal(file_contents)
        count_words(file_contents)
        count_characters(file_contents)
        
if __name__ == "__main__":
    main()