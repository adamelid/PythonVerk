#Algorithm is as follows:
#While not at final tile.
#----Show possible directions.
#----Player chooses direction.
#----Check if direction is valid.
#----Move to chosen tile if valid.
#Print victory result.

#Set static variables.
# -     x, y, walls(west, north, east, south), lever.
Tile1 = 1,1,1,0,1,1,0
Tile2 = 2,1,1,0,1,1,0
Tile3 = 3,1,1,0,1,1,0
Tile4 = 1,2,1,0,0,0,1
Tile5 = 2,2,0,1,1,0,1
Tile6 = 3,2,1,0,1,0,1
Tile7 = 1,3,1,1,0,0,0
Tile8 = 2,3,0,1,0,1,1
Tile9 = 3,3,0,1,1,0,0
currentTile = Tile1
x = currentTile[0]
y = currentTile[1]
hasNotRun = True
totalCoins = 0

def pull_lever(totalCoins):
    leverChoice = input("Pull a lever (y/n): ").lower()
    if leverChoice == "y":
        totalCoins += 1
        print("You received 1 coins, your total is now " + str(totalCoins) + ".")
    return totalCoins

#Finds out which directions player can choose from.
def possible_directions(currentTile,hasNotRun):
    #Set variables that need to be reset every call.
    howManyDirections = 0
    travelPossibilities = ""
    #If there are no walls, add that direction to possible directions.
    if hasNotRun:
        if not currentTile[3]:
            travelPossibilities += "(N)orth"
            howManyDirections += 1
        if not currentTile[4]:
            if howManyDirections > 0:
                travelPossibilities += " or (E)ast"
            else:
                travelPossibilities += "(E)ast"
            howManyDirections += 1
        if not currentTile[5]:
            if howManyDirections > 0:
                travelPossibilities += " or (S)outh"
            else:
                travelPossibilities += "(S)outh"
            howManyDirections += 1
        if not currentTile[2]:
            if howManyDirections > 0:
                travelPossibilities += " or (W)est"
            else:
                travelPossibilities += "(W)est"
            howManyDirections += 1
        #Print out travel options.
        print("You can travel: " + travelPossibilities + ".")
        hasNotRun = False
        return hasNotRun

#Checks if direction is choosable
def check_if_choosable(hasNotRun,direction,currentTile,x,y):
    if direction.lower() == "n" and currentTile[3] == False:
        y += 1
        hasNotRun = True
    elif direction.lower() == "e" and currentTile[4] == False:
        x += 1
        hasNotRun = True
    elif direction.lower() == "s" and currentTile[5] == False:
        y -= 1
        hasNotRun = True
    elif direction.lower() == "w" and currentTile[2] == False:
        x -= 1
        hasNotRun = True
    else:
        print("Not a valid direction!")
    return hasNotRun,x,y

#Moves player to next tile.
def move_player(x,y,currentTile):
    if x == 1 and y == 1:
        currentTile = Tile1
    elif x == 2 and y == 1:
        currentTile = Tile2
    elif x == 3 and y == 1:
        currentTile = Tile3
    elif x == 1 and y == 2:
        currentTile = Tile4
    elif x == 2 and y == 2:
        currentTile = Tile5
    elif x == 3 and y == 2:
        currentTile = Tile6
    elif x == 1 and y == 3:
        currentTile = Tile7
    elif x == 2 and y == 3:
        currentTile = Tile8
    elif x == 3 and y == 3:
        currentTile = Tile9
    return currentTile

#While loop which contains the program (While not at victory x,y coordinates).
while x != 3 or y != 1:
    leverActive = currentTile[6]
    if leverActive:
        totalCoins = pull_lever(totalCoins)
    hasNotRun = possible_directions(currentTile,hasNotRun)
    direction = input("Direction: ")
    hasNotRun,x,y = check_if_choosable(hasNotRun,direction,currentTile,x,y)
    currentTile = move_player(x,y,currentTile)
#Print result when at tile x == 3 and y == 1 (Tile3)
print("Victory!")