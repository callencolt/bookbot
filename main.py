from stats import word_count, char_count, compiled_data

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content

def main():
    book_text = get_book_text("books/frankenstein.txt")
    #print(book_text)
    print(f"======================== BOOKBOT ========================\n" )
    print(f"Analyzing book found at books/frankenstein.txt\n")
    
    num_words = word_count(book_text)
    print("--------------------- Word Count --------------------\n")
    print(f"Found {num_words} total words\n")
    char_num = char_count(book_text)
    sorted_pair = compiled_data(char_num)
    print("--------------------- Character Count ---------------------")
    for key, value in sorted_pair.items():
        print(f"{key}: {value}")

main()
