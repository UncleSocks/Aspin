import random
import string


def parameter_parser(parameter_dict):
    
    word_length = parameter_dict['word_length']
    generate_number = parameter_dict['generate_number']
    separator = parameter_dict['separator']
    separator_count = parameter_dict['separator_count']
    numbers = parameter_dict['numbers']
    special_characters = parameter_dict['special_characters']
    substitution = parameter_dict['substitution']
    word_case = parameter_dict['word_case']
    wordlist = parameter_dict['wordlist']
    wordlist_combine = parameter_dict['wordlist_combine']

    return word_length, generate_number, separator, separator_count, numbers, \
        special_characters, substitution, word_case, wordlist, wordlist_combine


class NumbersAndSpecialChars:

    def __init__(self, wordlist, word_length):
        self.wordlist = wordlist
        self.word_length = word_length


    def add_special_chars(self):
        special_chars = ''.join(random.choice(string.punctuation) for _ in range(self.word_length))
        wordlist_with_special_chars = [f"{word}{special_char}" for word, special_char in zip(self.wordlist, special_chars)]
        return wordlist_with_special_chars
    

    def add_numbers(self):
        numbers = ''.join(random.choice(string.digits) for _ in range(self.word_length))
        wordlist_with_numbers = [f"{word}{number}" for word, number in zip(self.wordlist, numbers)]
        return wordlist_with_numbers
    

    def special_chars_nums_process(self, numbers_args, special_chars_args):
        
        if special_chars_args == True:
            self.wordlist = self.add_special_chars()
        
        if numbers_args == True:
            self.wordlist = self.add_numbers()

        return self.wordlist


def separator_multiplier(separator, multiplier):

    if isinstance(multiplier, int):
        multiplied = f"{separator*multiplier}"
        return multiplied
    else:
        ValueError("ERR02: Separator multiplier must be an integer.") 


def substitution_parser(substitution):

    if substitution:
        parsed_substitution = substitution.split("=")
        current_char = parsed_substitution[0]
        new_char = parsed_substitution[1]
        return current_char, new_char
    
    else:
        return
    

class WordCase:

    def __init__(self, wordlist, word_case):
        self.wordlist = wordlist
        self.word_case = word_case
    
    def lowercase(self):
        lowercase_wordlist = [word.lower() for word in self.wordlist]
        return lowercase_wordlist
    
    def uppercase(self):
        uppercase_wordlist = [word.upper() for word in self.wordlist]
        return uppercase_wordlist
    
    def capitalize(self):
        capitalize_wordlist = [word.capitalize() for word in self.wordlist]
        return capitalize_wordlist
    
    def randomize(self):
        randomize_wordlist = []
        for word in self.wordlist:
            randomize_word = ''.join(random.choice([char.upper(), char]) for char in word)
            randomize_wordlist.append(randomize_word)
        return randomize_wordlist
    
    def alternate(self):
        alternate_wordlist = []
        for word in self.wordlist:
            alternate_word = ''.join(char.upper() if index % 2 == 0 else char.lower() for index, char in enumerate(word))
            alternate_wordlist.append(alternate_word)
        return alternate_wordlist

    def process(self):
        word_case_method = {
            'lowercase':self.lowercase,
            'uppercase':self.uppercase,
            'capitalize':self.capitalize,
            'randomize':self.randomize,
            'alternate':self.alternate
        }

        if self.word_case in word_case_method:
            return word_case_method[self.word_case]()
        else:
            ValueError(f"ERR01: Unsupported word case method: {self.word_case}")