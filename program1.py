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
        sentence = input('Sentence: ')
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

def Count(sentence):
    word = (' ')
    vowels = ('aeiou')
    wordCount = 1
    vowelCount = 0
    consonantCount = 0
    for count in sentence:
        if count in word:
            wordCount +=  1
        elif count in vowels:
            vowelCount +=  1
        elif count not in ['.', '?', '!']:
            consonantCount +=  1      
    return wordCount, vowelCount, consonantCount

def display(wordC,vowelC,consonantC):
    print('Word count:', wordC)
    print('Vowel letter count:', vowelC)
    print('Consonant letter count:', consonantC)

def main():
    sentence = userInput().lower()
    Count(sentence)
    wCount, vCount, cCount = Count(sentence)
    display(wCount,vCount,cCount)

main()







