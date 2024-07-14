# A bash script that separates alternate spellings from Pinoy Dictionary (e.g., ábung, abúng)
# !/bin/bash

processLine () {

        local line=$1

        echo "Processing $line"

        if echo "$line" | grep -q ", "; then
                echo "$line" | cut -d "," -f 1 >> $2
                echo "$line" | cut -d "," -f 2 | sed 's/^[ \t]*//' >> $2

        else
                echo "$line" >> $2

        fi
}

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
