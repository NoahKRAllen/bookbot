import sys
from stats import num_words_in_string, amount_of_each_char, sorted_dict
def get_book_text(book_to_parse):
    with open(book_to_parse, encoding="utf-8") as f:
        return f.read()
def pretty_print(num_words, dict_of_chars):
    print("============ BOOKBOT ============"
          f"\nAnalyzing book found at {sys.argv[1]}..."
          "\n----------- Word Count ----------"
          "\nFound " + str(num_words) + " total words"
          "\n--------- Character Count -------")
    for char, count in dict_of_chars.items():
        if char.isalpha():
            print(char + ": " + str(count))
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    num_words = num_words_in_string(get_book_text(sys.argv[1]))
    dict_of_chars = amount_of_each_char(get_book_text(sys.argv[1]))
    sorted_dict_of_chars = sorted_dict(dict_of_chars)
    pretty_print(num_words, sorted_dict_of_chars)

if __name__ == "__main__":
    main()