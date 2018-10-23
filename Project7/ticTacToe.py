def createBoard():
    dimensions = input("Input dimensions of the board: ")
    dimensions = int(dimensions)
    completeList = []
    tempRowList = []
    counter = 1
    for row in range(1, (dimensions+1)):
        for column in range(1, (dimensions+1)):
            tempRowList.append(counter)
            counter += 1
        completeList.append(tempRowList)
        tempRowList = []
    return completeList

def printBoard(currentBoardList):
    for row in currentBoardList:
        tempString = ""
        for number in row:
            tempString += "{:>5}".format(number)
        print(tempString)

def checkVictory(currentBoardList):
    xWon = False
    oWon = False
    for i, row in enumerate(currentBoardList):
        xRowCounter = 0
        xColumnCounter = 0
        xDiagonalCounter = 0
        yRowCounter = 0
        yColumnCounter = 0
        yDiagonalCounter = 0
        for number in row:
            if number.lower() == "x":
                xRowCounter += 1
            elif number.lower() == "y":
                yRowCounter += 1
            if row[i] == "x":
        
def main():
    boardList = createBoard()
    printBoard(boardList)

main()