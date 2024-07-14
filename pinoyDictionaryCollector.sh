# This Bash script collects tagalog, hiligaynon, cebuano, and ilocano dictionary entries from hxxps[://]pinoydictionary[.]com.
# The collected dictionary entries are then appended to a text file, which is used by 'Apsin' to generate passphrases.
# The script uses cURL together with grep and cut to parse through the HTTP file and capture the dictionary entries.
# By default, the script will loop through the available dictionaries (tagalog, hiligaynon, cebuano, and ilocano) but you can specify a dialect by passing it as the first argument. Note, it is case-sensitive.
# When a dictionary is passed as an argument, you can also specify which letter to begin as a second argument to avoid starting from scratch every time you run this script.
# Use the --help or -h argument for more information.
#
#
# Please note that I do not own the hxxps[://]pinoydictionary[.]com website.


#!/bin/bash

showHelp () {
    echo "Usage: $0 [dialect] [startingLetter]"
    echo "dialect (optional): The dialect you want to create a dictionary for (tagalog, hiligaynon, cebuano, ilocano). By default, the script will run through all four dialects."
    echo "startingLetter (optional): When a dialect is specified, you can also specify which letter to start. By default, it will capturing start letter A."
}

createDictionary () {

    echo "Checking for $1 dictionary file..."
    if [ -f ./$1.txt ]; then
        echo "A $1 dictionary file was found."
        chmod 666 $1.txt

    else
        echo "Creating a $1 dictionary file..."
        touch $1.txt
        echo "Successfully created the $1.txt dictionary file."
        chmod 666 $1.txt

    fi

    alphabet=('a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z')

    startIndex=0
    if [ -n "$2" ]; then

        findLetter = $2

        for index in "${!alphabet[@]}"; do
            
            if [ ${alphabet[$index]} == $findLetter ]; then
                startIndex=$index
                break
            fi

        done
    
    fi

    for ((currentIndex=startIndex; currentIndex<${#alphabet[@]}; currentIndex++)); do

        currentLetter=${alphabet[$currentIndex]}
        pageCounter=1
        url="https://$1.pinoydictionary.com/list/$currentLetter/"
        
        until curl -s "${url}/$pageCounter/" | grep -q "The page you are looking for could not be found."; do

            currentPage=$pageCounter
            echo "Capturing: dictionary $1 on letter '$currentLetter' on page '$currentPage'."

            curl -s "${url}/$pageCounter/" | grep h2 | cut -d '>' -f 3 | cut -d '<' -f 1 >> $1.txt
            ((pageCounter++))

        done
    done
}

main () {

    dialects=("tagalog" "hiligaynon" "cebuano" "ilocano")

    if [[ $1 == "--help" || $1 == "-h" ]]; then
        showHelp
        exit 0
    fi
    
    if [ $# -gt 0 ]; then

        invalidDialect=1
        for dialect in ${dialects[@]}; do

            if [[ $1 == $dialect ]]; then
                invalidDialect=0
                break
            fi
        done

        if [[ $invalidDialect -eq 0 ]]; then
            createDictionary "$@"
        else
            echo "Invalid dialect. The script currently supports tagalog, hiligaynon, and cebuano dialects."
        fi

    else
        for dialect in ${dialects[@]}; do
            createDictionary "$dialect"
        done
    fi
}

main "$@"