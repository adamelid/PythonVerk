MinPosition = 1
MaxPosition = 10

def print_mess():
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")

def moving_char(currentPos, choiceInput):
    if choiceInput == "l" and currentPos != MinPosition:
        currentPos -= 1
    elif choiceInput == "r" and currentPos != MaxPosition:
        currentPos += 1
    return currentPos

currentPos = int(input("Input a position between 1 and 10: "))
while True:
    print_mess()
    choice = input("Input your choice: ")
    while choice == "l" or choice == "r":
        currentPos = moving_char(currentPos, choice)
        print("New position is: " + str(currentPos))
        print_mess()
        choice = input("Input your choice: ")
    print("New position is: " + str(currentPos))
    break