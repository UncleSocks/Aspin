# Aspin: Filipino-centric Passphrase Generator
# GitHub @unclesocks: https://github.com/UncleSocks
#
# MIT License
#
# Copyright (c) 2024 Tyrone Kevin Ilisan
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and 
# to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT 
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.




import argparse

from aspin.interactive import InteractiveGeneration
from aspin.generator import NumbersAndSpecialChars, WordCase, separator_multiplier, substitution_parser, parameter_parser
from aspin.wordlist_processor import WordlistProcess


class ArgumentParser:
    
    def __init__(self):
        
        self.parser = argparse.ArgumentParser(prog="ASPIN", description="ASPIN is a Filipino-centric passphrase generator.")
        self._add_arguments()

    
    def _add_arguments(self):
        
        self.parser.add_argument(
            "-l", "--WORDLENGTH",
            type=int,
            default=5,
            dest="word_length",
            help="Specify an integer for the number of words in your passphrase. Default value is 5",
        )

        self.parser.add_argument(
            "-n", "--GENERATENUMBER",
            type=int,
            default=1,
            dest="generate_number",
            help="Specify the number of passphrases to be generated. Default value is 1."
        )

        self.parser.add_argument(
            "-s", "--SEPARATOR",
            type=str,
            default="",
            dest="separator",
            help="Specify a separator character between each word in your passphrase. Default is a no space."
        )

        self.parser.add_argument(
            "-sC", "--SEPARATORCOUNT",
            type=int,
            default=1,
            dest="separator_count",
            help="Specify the number of separators between each word. Default value is 1."
        )

        self.parser.add_argument(
            "-N", "--NUMBERS",
            action="store_true",
            dest="numbers",
            help="Append numbers at the end of each word in your passphrase. Default value is False."
        )

        self.parser.add_argument(
            "-S", "--SPECIALCHARS",
            action="store_true",
            dest="special_characters",
            help="Append special characters at the end of each word in your passphrase. Default value is False."
        )

        self.parser.add_argument(
            "-c", '--WORDCASE',
            type=str,
            default="lowercase",
            dest="word_case",
            help=(
                "Specify a word case for your passphrase. Default value is lowercase. "
                "Options are: lowercase, uppercase, capitalize, randomize, alternate."
            )
        )

        self.parser.add_argument(
            "-x", "--SUBSTITUTION",
            type=str,
            default=None,
            dest="substitution",
            help=(
                "Specify a character substitution using the equals (=) symbol between your old and new character (e.g., l=!). "
                "Default value is None."
            )
        )

        self.parser.add_argument(
            "-w", '--WORDLIST',
            type=str,
            default="./wordlist/tagalog-clean.txt",
            dest="wordlist",
            help="Specify the wordlist file location. Default is the tagalog.txt file."
        )

        self.parser.add_argument(
            "-wC", "--WORDLISTCOMBINE",
            type=str,
            default=None,
            dest="wordlist_combine",
            help="Specify a second language wordlist to be combined. Default value is None."
        )
        
        self.parser.add_argument(
            "-i", "--INTERACTIVE",
            action="store_true",
            dest="interactive",
            help="The program will ask for user inputs to generate the passphrase. Default value is False."
        )


    def parse_arguments(self):
        return self.parser.parse_args()
    
    
    def argument_output(self):

        return {
            'word_length': self.parser.parse_args().word_length,
            'generate_number': self.parser.parse_args().generate_number,
            'separator': self.parser.parse_args().separator,
            'separator_count': self.parser.parse_args().separator_count,
            'numbers': self.parser.parse_args().numbers,
            'special_characters': self.parser.parse_args().special_characters,
            'substitution': self.parser.parse_args().substitution,
            'word_case': self.parser.parse_args().word_case,
            'wordlist': self.parser.parse_args().wordlist,
            'wordlist_combine': self.parser.parse_args().wordlist_combine
        }    


def banner():

    aspin_banner = """
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   
             ████                                               ██                                 
          █    ███                                            ███                                  
          ████  ██              ███                                                                
      █     ███████████          ██       ███       ██                            █████████        
      ████ █████  ███    ███     ██      ███         ███          ████████      █████ ████████     
        ████         █████████   ███    ██████       ████       ████    ██    ███      ███  ███    
       ███         ████     ███  ███  ███    ███    ███       █████     ███  ███       ███   ███   
      ███        ████       ██    ██ ███   ████     ███    ████  ██     ██  ███        ███    ███  
      ███      ████        ██     █████     ███      ███████      █         ███         ██    ███  
       ███  █████                 ████       ███                             ██       ████    ███  
        ██████                       ██   ███████                                     █            
                                   ██████                                          ███████         
                                     ██                                              ██                                                                                   
                                                                                                                       
                                ASPIN: Filipino-centric Passphrase Generator     


\t[+] Feature-rich yet intuitive passphrase generator
\t[+] Supports English, Filipino, Hiligaynon, and Cebuano
\t[+] Use the `-h` option for help

\t@unclesocks
\thttps://github.com/UncleSocks/aspin-filipino-centric-passphrase-generator
\t-------------------------------------------------------------------------------------------------                                                                                              
    """
    return print(aspin_banner)


def main():
    
    banner()

    argument_parser = ArgumentParser()
    argument = argument_parser.parse_arguments()
    init_generate_count = 0

    if argument.interactive:
        user_input_parameters = InteractiveGeneration()
        parameter_output = user_input_parameters.output()

    else:
        parameter_output = argument_parser.argument_output()
        
    word_length, generate_number, separator, separator_count, numbers, special_characters, \
        substitution, word_case, wordlist, wordlist_combine = parameter_parser(parameter_output)
    
    wordlist_list = []
    wordlist_list.append(wordlist)

    if wordlist_combine and wordlist_combine is not None:
        wordlist_list.append(wordlist_combine)
    
    print("\n\tPassphrase Generated:\n\t")
    while init_generate_count < generate_number:
        process_wordlist = WordlistProcess(wordlist_list)

        wordlist = process_wordlist.process_wordlist(word_length)

        multiplied_separator = separator_multiplier(separator, separator_count)
        nums_and_special_chars = NumbersAndSpecialChars(wordlist, word_length)
        wordlist = nums_and_special_chars.special_chars_nums_process(numbers, special_characters)
        
        wordlist = WordCase(wordlist, word_case).process()
        
        passphrase_raw = f'{multiplied_separator}'.join(wordlist)

        if substitution and substitution is not None:
            current_char, new_char = substitution_parser(substitution)
            passphrase_raw = passphrase_raw.replace(current_char, new_char)

        print(f"\t{passphrase_raw}")
        init_generate_count += 1
    print("\n")


if __name__ == "__main__":
    main()