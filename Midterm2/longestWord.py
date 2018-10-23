# Function definitions start here
def open_file(fileName):
    try:
        fileContents = open(fileName,"r")
        return fileContents
    except FileNotFoundError:
        return None

def get_longest_word(fileContents):
    longestWord = ""
    for item in fileContents:
        wordLength = 0
        itemLength = 0
        item = item.strip("\n")
        for letter in longestWord:
            wordLength += 1
        for letter in item:
            itemLength += 1
        if itemLength > wordLength:
            longestWord = item
    return longestWord

# The main program starts here
filename = input("Enter name of file: ")
file_stream = open_file(filename)
if file_stream:
	longest_word = get_longest_word(file_stream)
	print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
	file_stream.close()
else:
	print('File',filename,'not found!')