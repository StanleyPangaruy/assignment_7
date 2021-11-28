# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# ex.
# input: Bahala kayo dyan
# output:
# words: 3
# vowels: 6
# consonants: 8


def userInput():
    while True:
        sentence = input('Enter your sentence: ')
        capital = sentence[0]
        punctuation = sentence[-1]
        if not capital.isupper():
            print('Please start with a capital letter.')
            continue
        elif punctuation not in ['.', '?', '!']:
            print('Please end with a punctuation mark.')
            continue
        else:
            return sentence

def wordCount(sentence):
    word = (' ')
    wordCount = 1
    for count in sentence:
        if count in word:
            wordCount +=  1
    return wordCount

def vowelCount(sentence):
    vowels = ('AaEeIiOoUu')
    vowelCount = 0
    for count in sentence:
        if count in vowels:
            vowelCount +=  1
    return vowelCount

def consonantCount(sentence):
    consonants = ('BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz')
    consonantCount = 0
    for count in sentence:
        if count in consonants:
            consonantCount +=  1
    return consonantCount

def display(wordC,vowelC,consonantC):
    print('Word count:', wordC)
    print('Vowel letter count:', vowelC)
    print('Consonant letter count:', consonantC)

def main():
    sentence = userInput()
    wordCount(sentence)
    vowelCount(sentence)
    consonantCount(sentence)
    wCount = wordCount(sentence)
    vCount = vowelCount(sentence)
    cCount = consonantCount(sentence)
    display(wCount,vCount,cCount)

main()







