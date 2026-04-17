'''
Your task here is very special: you must design a vowel eater! 
Write a program that uses:

a for loop;
the concept of conditional execution (if-elif-else)
the continue statement.
Your program must:

ask the user to enter a word;
use user_word = user_word.upper() to convert the word entered by the user 
to upper case; we'll talk about string methods and the upper() method very 
soon – don't worry;
use conditional execution and the continue statement to "eat" the 
following vowels A, E, I, O, U from the inputted word;
print the uneaten letters to the screen, each one of them on a separate line.
'''

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
    print(letter)
    
