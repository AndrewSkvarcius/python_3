def print_upper_words(words) :
    '''Prints each word on seperate line uppercase'''
    for word in words :
        print(word.upper())

def print_lower_words(words) :
    '''Prints each word on seperate line lowercase'''
    for word in words:
        print(word.lower())

def print_upper_words_t (words): 
    "prints words with T"
    for word in words :
        if word.startswith("t") or word.startswith("T"):
            print(word.upper())

def print_upper_wordz(words, must_start_with):
    '''Prints each word upper if it starts with'''
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break

pie_ingredients = ['flour', 'apples', 'eggs', 'sugar', 'salt']