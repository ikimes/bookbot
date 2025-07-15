import sys
from stats import words_in_text, character_frequency, sorted_character_frequency


def get_book_text(filepath):
    with open(filepath) as file:
        text = file.read()
    return text


def main():
    # Ensure a file path is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]  # Get the file path from the command-line arguments
    book_text = get_book_text(filepath)
    word_count = words_in_text(book_text)
    char_freq = character_frequency(book_text)
    sorted_freq = sorted_character_frequency(char_freq)
    # print(char_freq)
    # print(sorted_freq)


        # Print the structured report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    for item in sorted_freq:
        if item['char'].isalpha():  # Skip non-alphabetical characters
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()