#Prints the book to the terminal
#def print_terminal(file_contents):
#    print(file_contents)

def sort_on(dict):
    return dict["num"]


# counts the number of words in the file
def count_words(file_contents):
    words = file_contents.split()
    counter = 0

    for word in words:
        counter += 1 
    
    return counter

    #print(f"Total word count is: {counter}")


    
#creates a new dictionary with count for particular word
def count_characters(file_contents):
    low_end = file_contents.lower()
    my_dict = {}
    
    for character in low_end:
        if character not in my_dict:
            my_dict[character] = 1
        else:
            my_dict[character] += 1

#new dictionary with the new names to be later used for sorting    
    char_list = []

    for char, count in my_dict.items():
        if char.isalpha():
            char_list.append({"character": char, "num": count})
            
    char_list.sort(reverse=True, key=sort_on)

   
    return char_list
    
#printing report to the console

def report_print(file_contents):
    print("--- Begin report of books/frankenstein.txt ---")
    wordcount = count_words(file_contents)
    print(f"{wordcount} words found in the document")
    print()
    print()
    char_list = count_characters(file_contents)
    for char_dict in char_list:
        char = char_dict["character"]
        count = char_dict["num"]
        print(f"The '{char}' character was found '{count}' times")
    print("--- End report ---")



def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print_terminal(file_contents)
        count_words(file_contents)
        count_characters(file_contents)
        report_print(file_contents)
        
if __name__ == "__main__":
    main()