from stats import word_count, char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content

def main():
    book_text = get_book_text("books/frankenstein.txt")
    #print(book_text)
    
    num_words = word_count(book_text)
    char_num = char_count(book_text)
    print(char_num)

main()
