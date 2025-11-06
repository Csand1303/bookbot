# python
import os
import sys
from stats import count_words, count_characters, report

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        book_contents = (get_book_text(filepath))
        word_count = count_words(book_contents)
        charators = count_characters(book_contents)
        sorted_chr = report(charators)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for item in sorted_chr:
            if item["char"].isalpha():
                print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
            
if __name__ == "__main__":
    main()