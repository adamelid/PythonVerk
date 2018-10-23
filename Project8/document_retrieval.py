import string

def read_file(selectedFile):
    try:
        fileContents = open(selectedFile, "r")
    except FileNotFoundError:
        print("Documents not found.")
        fileContents = None
    return fileContents

def create_document_list(fileContents):
    documentList = []
    for line in fileContents:
        documentList.append(line.split("<NEW DOCUMENT>"))
    return documentList

def print_options():
    print("What would you like to do?")
    print("1. Search Documents")
    print("2. Print Documents")
    print("3. Quit Program")

def search_docs(documentList):
    answerString = ""
    userInput = input()
    for i, document in enumerate(documentList):
        for word in str(document).split():
            if userInput.lower() == word.strip(string.punctuation).lower():
                answerString += (" " + str(i))
    print(answerString)

def print_docs(documentList):
    userInput = input("Enter document number: ")
    print("Document #" + userInput)
    print(documentList[int(userInput)])

def quit_program():
    print("Exiting program.")

def main():
    option = "1"
    nameOfFile = input()
    fileContents = read_file(nameOfFile)
    if fileContents:
        documentList = create_document_list(fileContents)
        while option == "1" or option == "2":
            print_options()
            option = input()
            if option == "1":
                search_docs(documentList)
            elif option == "2":
                print_docs(documentList)
        quit_program()
main()