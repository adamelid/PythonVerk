def find_longest_word(words):
    longestWord = ""
    for currentWord in fileContent:
        if len(currentWord) > len(longestWord):
            longestWord = currentWord
    return longestWord

myFile = open("words.txt","r")
fileContent = myFile.read()
fileContent = fileContent.split("\n")
longestWord = find_longest_word(fileContent)

print("Longest word is '" + longestWord + "' of length " + str(len(longestWord)))