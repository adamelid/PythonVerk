# Your functions should appear here
def populate_list(emptyList):
    while True:
        userInput = input("Enter value to be added to list: ")
        if userInput.lower() != "exit":
            emptyList.append(userInput)
            newList = emptyList
        else:
            return newList
def triple_list(newList):
    newList *= 3
    return newList
# Main program starts here - DO NOT change it.
initial_list = []
populate_list(initial_list)
new_list = triple_list(initial_list)

for items in new_list:
    print(items)
