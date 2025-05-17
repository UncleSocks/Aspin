import random


class WordlistProcess:

    def __init__(self, filepaths):
        self.filepaths = filepaths

    def count_lines(self):
        
        filepath_dict = {}
        for filepath in self.filepaths:
        
            with open(filepath, 'rb') as file:
                lines_sum = sum(1 for _ in file) 
                #The underscore (_) is a common variable placeholder for variable values not being used.
                filepath_dict.update({filepath:lines_sum})

        return filepath_dict
    
    def get_word(self, line_number, chosen_filepath):
        
        with open(chosen_filepath, 'r') as file:
            for current_line, line in enumerate(file, start=1):
                if current_line == line_number:
                    return line.strip()
                
    def process_wordlist(self, word_length):
        
        filepath_lines_sum = self.count_lines()
        wordlist = []

        while len(wordlist) < word_length:
            
            randomized_filepath_index = random.randint(0,len(self.filepaths) - 1)
            chosen_filepath = self.filepaths[randomized_filepath_index]
        
            line_number = random.randint(1, filepath_lines_sum[chosen_filepath])
            current_word = self.get_word(line_number, chosen_filepath)

            if current_word and current_word not in wordlist:
                wordlist.append(current_word)

        return wordlist