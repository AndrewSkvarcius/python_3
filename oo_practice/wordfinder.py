"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
    def __init__(self, filename):
        '''Reads dict shows # items read '''
        dict_file = open(filename)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words found")
    
    def parse(self, dict_file):
        """Parses dict_file and returns list of words"""
        return [w.strip() for w in dict_file]
    def rando(self):
        "Random Word"
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    def parse(self, dict_file):
        """Parses dict_file returns list of words skippong blanks and comments"""
        return [w.strip() for w in dict_file
        if w.strip() and not w.startswith('#')]