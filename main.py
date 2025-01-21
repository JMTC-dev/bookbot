def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_number_of_words(text)
    num_characters = count_number_of_letters(text)
    print(f"{num_words} words found in the document")
    print(num_characters)

def count_number_of_words(content):
    words = content.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_number_of_letters(content):
    character_dict = {}
    for c in content:
        char = c.lower()
        if(char in character_dict):
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict
main()


