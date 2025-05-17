![aspin_01](https://github.com/user-attachments/assets/6c3282e3-46eb-4692-87dd-7e590fddb499)

# Aspin: Filipino Passphrase Generator

**Aspin** _[ˈʔas.pɪn]_, short for Asong Pinoy, is a term used for mixed-breed street dogs.

Why create another passphrase generator? 

I wanted to create a passphrase generator that focuses on Philippine dialects as its wordlists -- "mixing" words, separators, case, and others to generate a more secure passphrase. 

This passphrase generator has the typical features of specifying the word count, word case, and separator. However, Aspin also supports character substitution, separator multiplier, inclusion of randomized numbers and/or special characters, and combining two dictionaries.
Furthermore, this allowed me to practice my Python skills and, at the same time, contribute to the information security knowledge base.

I also included a folder of my photographs to raise awareness of aspins.

## Preview

![image](https://github.com/user-attachments/assets/5da2f24e-7012-420e-a670-fbc378d992bb)

Aspin can be used from the CLI or as a browser extension. When using the CLI, you can set all options either through command arguments or by entering interactive mode.
```
aspin.py -l 5 -s * -sC 3 -N -S -c randomize -x a=@

Passphrase Generated:
@LPAS.2***P@glAL@IB/0***ItuWAD=8***sALIGWIl(5***SuGid,2
```
The above example looks very complicated, but this would be ideal if you need extra security. Specifying fewer arguments can result in a more memorable passphrase:
```
aspin.py -l 5 -s - -sC 3 -N -c capitalize

Passphrase Generated:
Mahigit9---Nakakabit6---Maulol1---Tukuyin9---Kalinga5
```

## Usage and Available Arguments
You can run the `-h` option to display the list of available command-line arguments. 
```
ASPIN [-h] [-l WORD_LENGTH] [-n GENERATE_NUMBER] [-s SEPARATOR] [-sC SEPARATOR_COUNT] [-N] [-S] [-c WORD_CASE] [-x SUBSTITUTION] [-w WORDLIST] [-wC WORDLIST_COMBINE] [-i]
```
### Available Arguments
The table below lists the available options. Each of these options/arguments has its own default value, which will be used when unspecified. Alternatively, you can run interactive mode by specifying the `-i` option. Aspin will then display prompts for you to answer.

| Option | Description | Default Value |
| ------ | ----------- | :-----------: |
| `-l` or `--WORDLENGTH` | Specify an integer for the number of words in your passphrase. | 5
| `n` or `--GENERATENUMBER` | Specify an integer for the number of passphrases to generate. | 1 |
| `-s` or `--SEPARATOR` | Specify a separator character between each word in your passphrase. | space |
| `-sC` or `--SEPARATORCOUNT` | Specify the number of separators between each word. | 1 |
| `-N` or `--NUMBERS` | Append numbers at the end of each word in your passphrase. | False |
| `-S` or `--SPECIALCHARS` | Append special characters at the end of each word in your passphrase. | False |
| `-c` or `--WORD_CASE` | Specify passphrase's word case. | Lowercase |
| `-x` or `--SUBSTITUTION` | Specify a character substitution using the '>' symbol between your old and new character (e.g., l>!). | None |
| `-w` or `--WORDLIST` | Specify the wordlist file location. | .\tagalog.txt |
| `-wC` or `--WORDLISTCOMBINE` | Specify another wordlist file location to combine with the current chosen wordlist. | None |
| `-i` or `--INTERACTIVE` | The program will ask for user inputs to generate the passphrase. | False |

### Word Case Options
- lowercase: All characters are in lowercase
- uppercase: All characters are in uppercase
- capitalize: The beginning character of each word is in uppercase
- randomize: Randomize uppercase and lowercase on each word
- alternate: Alternate between lowercase and uppercase on each character.

### Numbers and Special Characters
When specifying the `-N` or `--NUMBERS` argument, it will append a random number to each word. Similarly, when specifying `-S` or `-SPECIALCHARS`, it will also append a special character to each word.

## Wordlists/Dictionaries
Aspin currently supports the following Filipino languages/dialects:
- Tagalog
- Hiligaynon
- Cebuano

The Filipino languages/dialects are all collected from Pinoy Dictionary (hxxps[://]www[.]pinoydictionary[.]com/) using a custom Bash script. The Bash script performs cURL operations and parses the HTML code for the dictionary entries. Then, another Bash script is used to clean up the raw dictionary text file -- removing any duplicates.

An English wordlist/dictionary is also available (this is the most common foreign language in the Philippines), which is from NSACyber's RandPassGenerator.

## Browser Extension
The tool is also now available as a browser extension and was tested on Chrome-based browsers. Currently, you can install this unpublished extension locally by enabling **Developer Mode** then clicking the **Load Unpacked** and selecting the **extension** directory to install it manually to your browsers.

![image](https://github.com/user-attachments/assets/87f542d5-ce3c-40c6-9e90-d45e9bcb93c2)

It has the same options as its CLI counterpart, except for using your own custom wordlist/dictionary.

### Chrome Extension
The browser extension is also available in the Chrome Web Store, which has the same functionality as the local version, but currently only supports Filipino (Tagalog) and English.

![image](https://github.com/user-attachments/assets/911382f8-d954-402e-8778-546418b49009)

## Supporting Aspins (and Puspins) in the Philippines
Please consider donating to various NGOs and volunteers focusing on rescuing Aspins and Puspins, such as:
- The Philippine Animal Welfare Society (PAWS): https://paws.org.ph/donate/
- SCARA-Animal Rescuers & Adopters: https://www.facebook.com/Scaraanimalrescuersandadopter
- Pawssion Project: https://pawssionproject.org.ph/donate/
- Strays Worth Saving (SWS): https://www.facebook.com/straysworthsaving/
- BACH Project PH: https://www.facebook.com/bachprojectphilippines
- Community Animal Rescue Efforts (CARE): https://www.facebook.com/CAREbacolod
- Animal Kingdom Foundation (AFK): https://www.akfrescues.org/
