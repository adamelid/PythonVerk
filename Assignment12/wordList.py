#build_wordlist() function goes here
def build_wordlist(fileContents):
    wordList = []
    for line in fileContents:
        wordList += line.split()
    return wordList
#find_unique() function goes here
def find_unique(chosenList):
    finalList = []
    for word in chosenList:
        if word not in finalList:
            finalList.append(word)
    return finalList

def main():
    infile = open("test.txt", 'r')
    word_list = build_wordlist(infile)  
    infile.close()  
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)

main()