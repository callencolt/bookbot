
def word_count(text):
    num_words = len(text.split())
    return num_words
    
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

def compiled_data(char_count):

    sort_dict = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    sort_char = {}
    for key, value in sort_dict:
        sort_char[key] = value
    return sort_char
    




