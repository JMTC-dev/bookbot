def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_number_of_words(text)
    num_characters = count_number_of_letters(text, True)
    generate_report(num_words, num_characters, book_path)   


def count_number_of_words(content):
    words = content.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_number_of_letters(content, alpha):
    character_dict = {}
    for c in content:
        char = c.lower()
        if(not alpha):
            if(char in character_dict):
                character_dict[char] += 1
            else:
                character_dict[char] = 1
        else:
            if(char.isalpha()):
                if(char in character_dict):
                    character_dict[char] += 1
                else:
                    character_dict[char] = 1
        
    return character_dict

def generate_report(num_words, num_characters, book_path):
    print(f"--- Begin report of {book_path} --- ")
    print(f"{num_words} words found in the document \n")
    for char in num_characters:
        print(f"The '{char}' character was found {num_characters[char]} times")
    print("--- End report ---")

main()


