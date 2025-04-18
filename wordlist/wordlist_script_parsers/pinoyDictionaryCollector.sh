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

    local dialect="$1"
    local startLetter="$2"

    echo "Checking for $dialect dictionary file..."
    if [ -f ./$dialect.txt ]; then
        echo "A $dialect dictionary file was found."
        chmod 666 $dialect.txt

    else
        echo "Creating a $dialect dictionary file..."
        touch $dialect.txt
        echo "Successfully created the $dialect.txt dictionary file."
        chmod 666 $dialect.txt

    fi

    alphabet=('a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z')

    startIndex=0
    if [ -n "$startLetter" ]; then

        for index in "${!alphabet[@]}"; do
            
            if [ ${alphabet[$index]} == $startLetter ]; then
                startIndex=$index
                break
            fi

        done
    
    fi

    for ((currentIndex=startIndex; currentIndex<${#alphabet[@]}; currentIndex++)); do

        currentLetter=${alphabet[$currentIndex]}
        pageCounter=1
        url="https://$dialect.pinoydictionary.com/list/$currentLetter/"
        
        until curl -s "${url}/$pageCounter/" | grep -q "The page you are looking for could not be found."; do

            currentPage=$pageCounter
            echo "Capturing: $dialect dictionary on letter '$currentLetter', page '$currentPage'."

            curl -s "${url}/$pageCounter/" | grep h2 | cut -d '>' -f 3 | cut -d '<' -f 1 >> $dialect.txt
            ((pageCounter++))

        done
    done
}


processLine () {

    local rawDictionary="$2"
    local line="$1"
    local tempDictionary="$3"

    if echo "$line" | grep -q ", "; then

        wordCounter=1
        while true; do
            
            catchWord=$(echo "$line" | cut -d "," -f $wordCounter | sed 's/^[ \t]*//')

            if [ -z "$catchWord" ]; then
                break
            fi

            echo "Cleaning line: $line"
            echo "$catchWord" >> "$tempDictionary"
            ((wordCounter++))
        done

    else
        echo "Cleaning line: $line"
        echo "$line" >> "$tempDictionary"
    fi

}


removeDuplicates () {

    echo -e "\nRemoving word duplicates in the clean dictionary text file..."

    local processedDictionary="$1"
    local newTempDictionary=$(mktemp)

    sort "$processedDictionary" | uniq > "$newTempDictionary"
    mv "$newTempDictionary" "$processedDictionary"
    chmod 666 "$processedDictionary"

    echo "Successfully removed all duplicates."

}


dictionaryCleanup () {
    
    rawDictionary="$1"
    echo -e "Initializing dictionary text file cleanup."

    touch "${rawDictionary}Temp.txt"
    tempDictionary="${rawDictionary}Temp.txt"

    while IFS= read -r line; do
        processLine "$line" "$rawDictionary" "$tempDictionary"
    done < "$rawDictionary"
    echo -e "\nDone writing the clean dictionary text file..."

    mv "$tempDictionary" "$rawDictionary"
    chmod 666 "$rawDictionary"
    removeDuplicates "$rawDictionary"
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

            if [ -f "$dialect.txt" ]; then

                rawDictionary="$dialect.txt"
                dictionaryCleanup "$rawDictionary"

            else
                echo "The $dialect.txt file cannot be found."
                exit 1
            fi

        else
            echo "Invalid dialect. The script currently supports tagalog, hiligaynon, and cebuano dialects."
        fi

    else
        for dialect in ${dialects[@]}; do
            createDictionary "$dialect"

            if [ -f "$dialect.txt" ]; then

                rawDictionary="$dialect.txt"
                dictionaryCleanup "$rawDictionary"

            else
                echo "The $dialect.txt file cannot be found."
                exit 1
            fi

        done
    fi
}

main "$@"