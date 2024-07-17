
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('passphrase-form').addEventListener('submit', function(event) {
        event.preventDefault();
        generatePassphrase();
    });

    document.getElementById('copy-button').addEventListener('click', function(event) {
        copyPassphraseToClipboard();
    });
});


function generatePassphrase() {
    const wordCount = parseInt(document.getElementById('word-count').value);
    const generateCount = parseInt(document.getElementById('generate-count').value);
    const separator = document.getElementById('separator').value;
    const separatorCount = parseInt(document.getElementById('separator-count').value);
    const includeNumbers = document.getElementById('numbers').checked;
    const includeSpecialChars = document.getElementById('special-chars').checked;
    const wordCase = document.getElementById('word-case').value;
    const substitutionFrom = document.getElementById('substitution-from').value;
    const substitutionTo = document.getElementById('substitution-to').value;
    const wordlist = document.getElementById('wordlist').value;
    const secondWordlist = document.getElementById('second-wordlist').value;

    const wordlistFiles = {
        tagalog: 'dictionaries/tagalog.txt',
        hiligaynon: 'dictionaries/hiligaynon.txt',
        cebuano: 'dictionaries/cebuano.txt',
        ilocano: 'dictionaries/ilocano.txt',
        english: 'dictionaries/english.txt'
    }

    const wordlistLoad = [wordlistFiles[wordlist]];
    if (secondWordlist !== 'none') {
        wordlistLoad.push(wordlistFiles[secondWordlist]);
    }

    Promise.all(wordlistLoad.map(loadWordlistFile)).then(wordlists => {
        const combinedWordlist = wordlists.flat();

        let passphrases = [];

        for (let generateCounter = 0; generateCounter < generateCount; generateCounter++) {
            let passphrase = [];
            for (let wordCounter = 0; wordCounter < wordCount; wordCounter++) {
                let word = combinedWordlist[Math.floor(Math.random() * combinedWordlist.length)];

                if (includeNumbers) {
                    word += Math.floor(Math.random() * 10);
                }

                if (includeSpecialChars) {
                    word += String.fromCharCode(33 + Math.floor(Math.random() * 15));
                }

                switch (wordCase) {
                    case 'uppercase':
                        word = word.toUpperCase();
                        break;
                    case 'lowercase':
                        word = word.toLowerCase();
                        break;
                    case 'capitalize':
                        word = word.charAt(0).toUpperCase() + word.slice(1)
                        break;
                    case 'randomize':
                        word = word.split('').map(char =>
                            Math.random() > 0.5 ? char.toUpperCase() : char.toLowerCase()
                        ).join('');
                        break;
                    case 'alternate':
                        word = word.split('').map((char, index) => 
                            index % 2 === 0 ? char.toUpperCase() : char.toLowerCase()
                        ).join('');
                        break;
                }

                passphrase.push(word);
            }

            let passphraseStr = passphrase.join(separator.repeat(separatorCount));

            if (substitutionFrom && substitutionTo) {
                passphraseStr = passphraseStr.replace(new RegExp(substitutionFrom, 'g'), substitutionTo);
            }

            passphrases.push(passphraseStr);
        }

        document.getElementById('output').innerText = passphrases.join('\n\n');
    });
}

function loadWordlistFile(file) {
    return fetch(file)
        .then(response => response.text())
        .then(text => text.split('\n').map(word => word.trim()).filter(Boolean));
}

function copyPassphraseToClipboard () {
    const passphraseText = document.getElementById('output').innerText;
    navigator.clipboard.writeText(passphraseText)
        .then(() => {
            const copyNotification = document.getElementById('copy-notification');
            copyNotification.style.display = 'block';

            setTimeout(() => {
                copyNotification.style.display = 'none';
            }, 2000)
        })
        .catch(err => {
            console.error('Failed to copy to clipboard: ', err);
            alert('Failed to copy to clipboard, try again.')
        })
}
