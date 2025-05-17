class InteractiveGeneration():

    def __init__(self):
        
        self.word_length = 5
        self.generate_number = 1
        self.separator = ""
        self.separator_count = 1
        self.numbers = False
        self.special_characters = False
        self.substitution = None
        self.word_case = "lowercase"
        self.wordlist = "./wordlist/tagalog-clean.txt"
        self.wordlist_combine = None

        self._collect_user_inputs()

            
    def _verify_int_input(self, prompt, default):
        user_input = input(prompt)
        return int(user_input) if user_input.isdigit() else default
    
    def _verify_bool_input(self, prompt):
        user_input = input(prompt)
        return user_input in ('yes', 'y', 'true', 't', '1')
    

    def _collect_user_inputs(self):
        
        self.word_length = self._verify_int_input(f"\tEnter passphrase word count (default {self.word_length}): ", self.word_length)
        self.generate_number = self._verify_int_input(f"\tNumber of passphrase to generate (default {self.generate_number}): ", self.generate_number)
        self.separator = input(f"\tSeparator character (default is no space): ").strip() or self.separator
        self.separator_count = self._verify_int_input(f"\tEnter separator count (default {self.separator_count}): ", self.separator_count)
        self.numbers = self._verify_bool_input(f"\tInclude numbers (default {self.numbers}): ")
        self.special_characters = self._verify_bool_input(f"\tInclude special characters (default {self.special_characters}): ")
        self.substitution = input(f"\tSpecify character substitution (default {self.substitution}): ") or self.substitution
        self.word_case = input (f"\tWord case (default {self.word_case}): ") or self.word_case
        self.wordlist = input(f"\tWordlist file path (defult {self.wordlist}): ") or self.wordlist
        self.wordlist_combine = input(f"\tCombine another wordlist (default {self.wordlist_combine}): ") or self.wordlist_combine

    
    def output(self):
        
        return {
            'word_length': self.word_length,
            'generate_number': self.generate_number, 
            'separator': self.separator,
            'separator_count': self.separator_count,
            'numbers': self.numbers,
            'special_characters': self.special_characters,
            'substitution': self.substitution,
            'word_case': self.word_case,
            'wordlist': self.wordlist,
            'wordlist_combine': self.wordlist_combine
        }
