![aspin_01](https://github.com/UncleSocks/aspin-filipino-centric-passphrase-generator/assets/79778613/7bccf670-a404-41fc-8ab3-489d7da828f7)

# Aspin: Filipino-centric Passphrase Generator

**Aspin** _[ˈʔas.pɪn]_, short for Asong Pinoy, is a term used for mixed-breed street dogs.

Why create another passphrase generator? 

I wanted to create a passphrase generator that focuses on Philippine dialects as its wordlists -- "mixing" words, separators, case, and others to generate a more secure passphrase. This passphrase generator has the generic features of specifying the word count, word case, and separator. In addition, it also supports character substitution, separator multiplier, and inclusion of randomized numbers and/or special characters.
Furthermore, this allowed me to practice my Python skills and at the same time contribute to the information security knowledge body.

I also included a folder of my photographs to raise awareness to aspins.
```
aspin.py -l 5 -s * -sC 3 -N -S -c randomize -x a=@
SAulI#0***PAngb@hIN#0***bibIG@n/9***TeKNoLohiy@~0***P@GpAp@SAL@m@t?7
```

## Usage and Available Arguments
You can run the `-h` option to display the list of available command-line arguments. 
```
usage: ASPIN [-h] [-l WORD_LENGTH] [-s SEPARATOR] [-sC SEPARATOR_COUNT] [-N] [-S] [-c WORD_CASE] [-x SUBSTITUTION] [-w WORDLIST] [-i]
```
### Available Arguments
Below you will find the list of available options. Each of these options/arguments has their own default value, which will be used when unspecified. Alternatively, you can run interactive mode by specifying the `-i` option. Aspin will then display prompts for you to answer.
- `-l` or `--WORDLENGTH` : Specify an integer for the number of words in your passphrase. Default value is 5
- `-s` or `--SEPARATOR` : Specify a separator character between each word in your passphrase. Default is a space.
- `-sC` or `--SEPARATORCOUNT` : Specify the number of separators between each word. Default value is 1.
- `-N` or `--NUMBERS` :  Append numbers at the end of each word in your passphrase. Default value is False.
- `-S` or `--SPECIALCHARS` :  Append special characters at the end of each word in your passphrase. Default value is False.
- `-x` or `--SUBSTITUTION` :  Specify a character substitution using the '>' symbol between your old and new character (e.g., l>!). Default value is None.
- `-w` or `--WORDLIST` : Specify the wordlist file location. Default is the tagalog.txt file.
- `-i` or `--INTERACTIVE` : The program will ask for user inputs to generate the passphrase. Default value is False.
