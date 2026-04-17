'''
Your program must:

ask the user to enter a word;
use user_word = user_word.upper() to convert the word entered by the user 
to upper case; we'll talk about string methods and the upper() method very 
soon - don't worry;
use conditional execution and the continue statement to "eat" the following 
vowels A, E, I, O, U from the inputted word;
assign the uneaten letters to the word_without_vowels variable and print 
the variable to the screen.
'''

word_without_vowels = ""

# Prompt the user to enter a word
word = input("Ingresa una palabra: ")
# and assign it to the user_word variable.
user_word = word.upper()
for letter in user_word:
    # Complete the body of the for loop.
    if letter == "A":  
        continue
    if letter == "E":
        continue
    if letter == "I":    
        continue
    if letter == "O": 
        continue
    if letter == "U":
        continue
    word_without_vowels=word_without_vowels+letter
print(word_without_vowels)    
    
