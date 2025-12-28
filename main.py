from stats import count_words, count_characters, sorted_character_count
import sys

def get_book_text(path):
    contents = ""
    with open(path) as file:
        contents = file.read()
    return contents

def main():
    book_path = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    sorted_count = sorted_character_count(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_count:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")

main()
