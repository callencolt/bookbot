#bookbot
"""
Author: Callen Wilson
Date: JUL 31, 2025
Version: 1.0
"""

BookBot is my first [Boot.dev](https://www.boot.dev) project and GitHub project!

BookBot is a command-line Python tool that analyzes a .txt book file. It reads the file, counts the total number of words, and provides a breakdown of total word count in the book and how frequently each letter appears (case-insensitive, a-z only).

This project is was to practice and use skills in text processing, Python scripting, Git/GitHub version control, refactoring and working in a Linux shell environment.

Features
  Accepts any plain-text .txt book file as input

Counts and displays:

  -Total number of words
  
  -Frequency of each letter (A–Z)
  
  -Designed for command-line usage with dynamic file input by using sys arg

Usage:
  python3 main.py <path_to_book>
Example:
  python3 main.py books/frankenstein.txt

Project Structure:
  bookbot/
  ├── books/
  │   ├── frankenstein.txt
  │   ├── mobydick.txt
  │   └── prideandprejudice.txt
  ├── main.py
  ├── stats.py
  └── README.md

  NOTE: Used a .gitignore file to exclude the books directory from version control, keeping large book files out of the repository while allowing the code to remain lightweight, focusing on the code not the data.

Development Environment:
  -Git was used for version control, tracking changes and managing project history through meaningful commits and branching.

  -GitHub is used to host the code, share progress, and maintain a remote backup of the project.

  -Linux command-line tools (like touch, mkdir, ls, cd, cat, nano, python3) were used for file management and running the script in a 
   Unix-based development environment.

Future Plans (Version 2.0):

  -Add a feature where users can enter a book title, and the program will automatically fetch the book text from 
    Project Gutenberg’s   website, copy the content, and save it as a new text file in the books directory for analysis.
  
  -Include functionality to compare the most common words and characters across multiple books, giving insights into common patterns 
    and unique differences among the texts.

