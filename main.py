from stats import get_word_count, get_character_count, sort_by_char
import sys


def get_book_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)

    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    sorted_list = sort_by_char(character_count)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for ch in sorted_list:
        if ch["char"].isalpha():
            print(f'{ch["char"]}: {ch["num"]}')
    print('============= END ===============')


main()
