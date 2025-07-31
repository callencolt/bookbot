def word_count(text):
    num_words = len(text.split())
    print(f"{num_words} words found in the document")

def char_count(text):
    texts = text.lower()
    char_count = {}
    alph = "abcdefghijklmnopqrstuvwxyz"
    for char in texts:
        if char in char_count:
            char_count[char] += 1
        else:
            if char in alph:
                    char_count[char] = 1        
    return char_count
        
