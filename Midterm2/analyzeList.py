def create_list():
    userInput = input("Enter integers separated with commas: ")
    userList = userInput.split(",")
    tempList = []
    errorShown = False
    for number in userList:
        try:
            tempList.append(int(number))
        except ValueError:
            if not errorShown:
                print("Incorrect input!")
                errorShown = True
            userList = None
    if userList == None:
        return userList
    else:
        return tempList

def create_sorted(originalList):
    sortedList = originalList.copy()
    sortedList.sort()
    return sortedList

def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True

def create_primeList(sortedList):
    primeList = []
    for number in sortedList:
        if is_prime(number) and number not in primeList:
            primeList.append(number)
    return primeList

def minMaxAverage(originalList):
    sumCounter = 0
    for number in originalList:
        sumCounter += number
    averageNum = (sumCounter/len(originalList))
    minNum = min(originalList)
    maxNum = max(originalList)
    return minNum, maxNum, averageNum

def print_output(ogList, sortList, primeList, minNum, maxNum, avgNum):
    print("Input list: " + str(ogList))
    print("Sorted list: " + str(sortList))
    print("Prime list: " + str(primeList))
    print("Min: {}, Max: {}, Average: {:.2f}".format(minNum, maxNum, avgNum))

# The main program starts here
def main():
    originalList = create_list()
    if originalList:
        sortedList = create_sorted(originalList)
        primeList = create_primeList(sortedList)
        minimum, maximum, average = minMaxAverage(originalList)
        print_output(originalList, sortedList, primeList, minimum, maximum, average)

main()