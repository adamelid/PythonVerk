#sort_list() function goes here
def sort_list(integerList):
    integerList.sort()

def main():
    #loop to accept integers until a non-digit is entered goes here
    userInput = ""
    a_list = []
    while True:
        userInput = input("")
        if userInput.isdigit():
            a_list.append(int(userInput))
        else:
            break
        
    ######Do not modify this part######
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    ######Do not modify this part######
    
main()