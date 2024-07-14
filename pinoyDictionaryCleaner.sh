# A bash script that separates alternate spellings from Pinoy Dictionary (e.g., ábung, abúng)
# !/bin/bash

processLine () {

        local line=$1

        if echo "$line" | grep -q ", "; then

                wordCounter=1
                while true; do

                        catchWord=$(echo "$line" | cut -d "," -f $wordCounter | sed 's/^[ \t]*//')

                        if [ -z $catchWord ]; then
                                break
                        fi

                        echo "Processing $line"
                        echo "$catchWord" >> $2
                        ((wordCounter++))

                done

        else
                echo "Processing $line"
                echo "$line" >> $2

        fi
}

removeDuplicates () {

        echo -e "\nRemoving word duplicates in the dictionary..."

        echo "Creating a temp file."
        local tempFile=$(mktemp)

        sort "$1" | uniq > "$tempFile"

        echo "Overwriting temp file..."
        mv "$tempFile" "$1"

        chmod 666 $1

        echo "Successfully removed all duplicates."


}

main () {
        processedDictionary=$2

        if [ -f $processedDictionary ]; then
                chmod 666 $processedDictionary
        else
                touch $processedDictionary
                chmod 666 $processedDictionary
        fi

        while ISR= read -r line; do
                processLine "$line" "$processedDictionary"
        done < "$1"

        removeDuplicates "$processedDictionary"

}

main "$@"