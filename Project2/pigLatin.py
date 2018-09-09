while True:

    consonants = "bcdfghjklmnpqrstvxzwy"
    vowels = "aeiou"
    consonantAdd = "ay"
    vowelAdd = "yay"
    stringInput = input("Enter a word: ")
    newString = stringInput
    
    if stringInput.lower() == ".":
        exit()
    elif stringInput[0].lower() in vowels:
        stringInput += vowelAdd
        print(stringInput)
    elif stringInput[0].lower() in consonants:
        for i in newString:
            if newString[0] not in vowels:
                newString = newString[1::] + newString[0]
            else:
                break
        newString += consonantAdd
        print(newString)
    else:
        print("Words start with letters...")