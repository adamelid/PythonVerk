def read_file(selectedFile):
    listOfLists = []
    try:
        fileContents = open(selectedFile, "r")
        for line in fileContents:
            listOfLists.append(line.split(","))
    except FileNotFoundError:
        print("Cannot find file " + selectedFile)
    return listOfLists

def find_indicator(i, listOfLists):
    column = ""
    indicator = ""
    indicatorList = listOfLists[0]
    if i == 1:
        indicator = indicatorList[1]
        column = 1
    elif i == 2:
        indicator = indicatorList[5]
        column = 5
    elif i == 3:
        indicator = indicatorList[7]
        column = 7
    elif i == 4:
        indicator = indicatorList[11]
        column = 11
    elif i == 5:
        indicator = indicatorList[13]
        column = 13
    return column, indicator

def find_min_max(i, listOfLists, column):
    maxNum = 0
    minNum = 0
    maxState = ""
    minState = ""
    for lineList in listOfLists:
        if lineList[column] > maxNum:
            maxNum = lineList[column]
            maxState = lineList[0]
        if lineList[column] < minNum:
            minNum = lineList[column]
            minState = lineList[0]
    return minNum, minState, maxNum, maxState
        
def print_header():
    print("{:33}{:21}{:>6}{:6}{:15}{:>6}".format("Indicator","Min","","","Max",""))
    print("-" * 87)

def print_output(indicator, minValue, minState, maxValue, maxState):
    print("{:33}{:21}{:>6}{:6}{:15}{:>6}".format(indicator,minState,minValue,"",maxState,maxValue))

def main():
    fileName = input("Enter filename containing csv data: ")
    listOfLists = read_file(fileName)
    print_header()
    for i in range(1,6):
        column, indicator = find_indicator(i,listOfLists)
        minValue, minState, maxValue, maxState = find_min_max(i, listOfLists, column)
        print_output(indicator, minValue, minState, maxValue, maxState)
main()