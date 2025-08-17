from stats import words_count
from stats import characters_count
from stats import sort_characters_count
import sys

def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    #file_path = 'books/frankenstein.txt'
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    try:
        book_text = get_book_text(file_path)
        #print("Book text loaded successfully.")
        # Further processing of book_text can be done here
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    print("============ BOOKBOT ============")
    #print("Analyzing book found at books/frankenstein.txt...")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count(book_text)} total words")
    print("--------- Character Count -------")
    list_of_sorted_char_count_dict = sort_characters_count(characters_count(book_text))
    for item in list_of_sorted_char_count_dict:
        if not item['char'].isalpha():
            continue
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

main()