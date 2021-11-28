# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# ex.
# input: Bahala kayo dyan
# output:
# words: 3
# vowels: 6
# consonants: 8

#imports from string method to use punctuation
#that contains all the set of punctuation
from string import punctuation

#asks a user to input a sentence
def userInput():
    while True:
        sentence = input('Sentence: ')
        #indicates the position of the first character
        capital = sentence[0]
        #indicates the position of the last character
        punctuation = sentence[-1] 
        #loops the code until the user entered the correct syntax for sentences.
        if not capital.isupper(): 
            print('Please start with a capital letter.')
            continue
        elif punctuation not in ['.', '?', '!']:
            print('Please end with a proper punctuation mark.')
            continue
        else:
            return sentence


def count(sentence):
    word = (' ') #variable to recognize each space in the sentence
    vowels = ('aeiou')
    #counts for the word, vowel and consonant 
    wordCount = 1 
    vowelCount = 0
    consonantCount = 0
    for char in sentence:
        if char in word: 
            wordCount +=  1
        elif char in vowels:
            vowelCount +=  1
        elif char not in punctuation: #to except all the special character used
            consonantCount +=  1      
    return wordCount, vowelCount, consonantCount

def display(wordC,vowelC,consonantC):
    print('Word count:', wordC)
    print('Vowel letter count:', vowelC)
    print('Consonant letter count:', consonantC)

def main():
    sentence = userInput().lower()
    wCount, vCount, cCount = count(sentence)
    display(wCount,vCount,cCount)

main()







