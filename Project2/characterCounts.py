import string

inputString = input("Enter a sentence: ")
upperCount = 0
lowerCount = 0
digitCount = 0
punctuationCount = 0

for i, letter in enumerate(inputString):
    if letter.isupper():
        upperCount += 1
    elif letter.islower():
        lowerCount += 1
    elif letter.isdigit():
        digitCount += 1
    elif letter in string.punctuation:
        punctuationCount += 1

print("{0:>15s} {1:5d}".format("Upper case",upperCount))
print("{0:>15s} {1:5d}".format("Lower case",lowerCount))
print("{0:>15s} {1:5d}".format("Digits",digitCount))
print("{0:>15s} {1:5d}".format("Punctuation",punctuationCount))