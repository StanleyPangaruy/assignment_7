# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex.
# input: P@ssw0rd+P@ssw0rd
# ouput: Valid


import string

#asks for the user's password
def userPassword():
    print("""-----------------------------------------------
Password should contain:
• Greater than 15 characters
• At least one capital letter
• At least one number
• At least one special char (!@#$%^&*()_+ etc)
-----------------------------------------------""")
    while True:
        passInput = input('Enter password: ')
        #loops the codeblock until the user entered an input
        if not len(passInput):
            print('No password entered. Try again!')
            continue
        else:
            return passInput

def passLength(passW):
    #returns a boolean value to the function
    if len(passW) <= 15: #password length should be greater than 15
        return False
    else:
        return True

def passChar(passW):
    #initial count for the elements in the password
    countCap = 0
    countNum = 0
    countSChar = 0
    #loops for every character in the string
    for i in passW:
        if i in string.ascii_uppercase: #counts for the capital letters
            countCap += 1
        if i in string.digits: #counts for the numbers
            countNum += 1
        if i in string.punctuation: #counts for the special characters
            countSChar += 1
    #compares the initial values to looped values
    #if the looped values are equal to the initial values
    #returns False 
    if not countCap:
        return False
    elif not countNum:
        return False  
    elif not countSChar:
        return False
    #if none the statements above gets satisfied
    #then it returns True
    else:
        return True
