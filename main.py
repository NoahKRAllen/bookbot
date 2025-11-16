from stats import num_words_in_string
def get_book_text(book_to_parse):
    with open(book_to_parse, encoding="utf-8") as f:
        return f.read()
def main():
    num_words = num_words_in_string(get_book_text("books/frankenstein.txt"))
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()