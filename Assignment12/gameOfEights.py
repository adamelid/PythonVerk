#game_of_eights() function goes here
def game_of_eights(chosenList):
    for number in range(len(chosenList)):
        if chosenList[number] == 8:
            try:
                if chosenList[number+1] == 8:
                    return True
            except:
                return False
    return False
def main():
    try:
        a_list = (input("Enter elements of list separated by commas: ").split(','))
        for number in range(len(a_list)):
            a_list[number] = int(a_list[number])
        print(game_of_eights(a_list))
    except ValueError:
        print("Error. Please enter only integers.")
main()