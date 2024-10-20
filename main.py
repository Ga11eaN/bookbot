def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    generate_report(book_path, get_number_words(file_contents), count_chars(file_contents))

def get_number_words(some_string):
    return len(some_string.split())

def count_chars(some_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    char_count = {}
    for ch in some_string.lower():
        if ch in alphabet:
            if ch in char_count:
                char_count[ch] += 1
            else:
                char_count[ch] = 1
    return char_count

def generate_report(book_path, words, chars):
    print(f"--- Report of {book_path} ---")
    sorted_dict = dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))
    for ch, count in sorted_dict.items():
        print(f"The {ch} characters was found {count} times")
    print("--- End of report ---")

if __name__ == "__main__":
    main()
