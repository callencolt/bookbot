"""
Author: Callen Wilson
Date: JUL 31, 2025
Version: 1.0

Supporting files: stats.py( contains functions for word and alphabet character count)

Project Summary: Book Bot

Description: This personal project is a book bot that reads a text file containing a 
book and analyzes it to count the number of words and characters.

"""
import sys
from stats import word_count, char_count, compiled_data

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_content = f.read()
        return file_content

def main():
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # else: completes the code to read the file and analyze it
    else:
        path_to_book = sys.argv[1]
        book_text = get_book_text(path_to_book)
        
        print(f"======================== BOOKBOT ========================\n" )
        print(f"Analyzing book found at {path_to_book}\n")
        
        #fetch the word count and prints header/count
        num_words = word_count(book_text)
        print("--------------------- Word Count --------------------\n")
        print(f"Found {num_words} total words\n")

        #fetch and sorts the character count and prints header/count
        char_num = char_count(book_text)
        sorted_pair = compiled_data(char_num)
        print("--------------------- Character Count ---------------------")
        for key, value in sorted_pair.items():
            print(f"{key}: {value}")

main()
