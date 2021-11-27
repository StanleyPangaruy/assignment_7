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
    return input('Sentence: ')

def wordCount(sentence):
    word = (' ')
    wordCount = 1
    for c in sentence:
        if c in word:
            wordCount +=  1
    return wordCount

def vowelCount(sentence):
    vowels = ('AaEeIiOoUu')
    vowelCount = 0
    for c in sentence:
        if c in vowels:
            vowelCount +=  1
    return vowelCount

def consonantCount(sentence):
    consonants = ('BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz')
    consonantCount = 0
    for c in sentence:
        if c in consonants:
            consonantCount +=  1
    return consonantCount


    















