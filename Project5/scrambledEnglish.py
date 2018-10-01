# The function get_word_string takes in a filename,
# it turns the text inside a file to a string and returns it,
# if the input file is not found, it returns an empty string and prints out an error message.
# The function scramble_string takes the string and scrambles all letters except the first and last.

import random
import string

# Checks if the file exists and turns the contents to a returned string.
def get_word_string(filename):
    wordString = ""
    try:
        fileContents = open(filename, "r")
        for line in fileContents:
            wordString += line
    except FileNotFoundError:
        print("File " + filename + " not found")
    return wordString

# Goes through every word in the string and scrambles (shuffles) all letter except first and last.
def scramble_string(wordString):
    wordList = list(wordString.split())
    scrambledString = ""
    for word in wordList:
        currentString = word
        if len(word) > 3:
            firstLetter, middleBit, lastLetter = word[0], list(word[1:-1]), word[-1]
            ifPunctuation = ""
            if word[-1] in string.punctuation:
                middleBit, lastLetter = list(word[1:-2]), word[-2]
                ifPunctuation = word[-1]
            random.shuffle(middleBit)
            currentString = (firstLetter + "".join(middleBit) + lastLetter + ifPunctuation)
        scrambledString += (currentString + " ")
    return scrambledString

# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)