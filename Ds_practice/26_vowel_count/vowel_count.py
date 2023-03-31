VOWELS = set('aeiou')
def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase = phrase.lower()
    count = {}

    for letter in phrase:
        if letter in VOWELS:
            count[letter] = count.get(letter, 0) + 1
    return count

