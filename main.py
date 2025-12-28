import sys
from stats import word_count, character_count, sorted_dicts

def get_book_txt(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        print("============= END ===============")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        print(f"Analyzing book found at {book_path}...")

        print("----------- Word Count ----------")
        book_text = get_book_txt(book_path)
        word_total = word_count(book_text)
        print(f"Found {word_total} total words")

        print("--------- Character Count -------")
        character_totals = character_count(book_text)
        char_dicts_sorted = sorted_dicts(character_totals)
        #print(char_dicts_sorted)
        for char_dict in char_dicts_sorted:
            if char_dict["char"].isalpha():
                print(f"{char_dict["char"]}: {char_dict["num"]}")

    print("============= END ===============")

main()