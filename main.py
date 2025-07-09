from stats import count_words_in_text, count_used_characters,sort_chars
import sys

def get_book_text(filePath):
    with open(filePath) as f:
        return f.read()

def print_report(bookPath):
    book = get_book_text(bookPath)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {bookPath}...')

    words_num = count_words_in_text(book)
    print("----------- Word Count ----------")
    print(f'Found {words_num} total words')

    characters_used = count_used_characters(book)
    sorted_characters = sort_chars(characters_used)
    print("--------- Character Count -------")
    for character in sorted_characters:
        char = character["char"]
        if (char.isalpha()):
            num = character["num"]
            print(f"{char}: {num}")
    print("============= END ===============")


def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print_report(sys.argv[1])


main()