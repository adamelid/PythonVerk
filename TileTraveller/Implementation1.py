#Path to git repo - https://github.com/adamelid/PythonVerk/tree/master/TileTraveller

#Algorithm is as follows:
#While not at final tile.
#----Show possible directions.
#----Player chooses direction.
#----Check if direction is valid.
#----Move to chosen tile if valid.
#Print victory result.

#Set static variables
Tile1 = 1,1,1,0,1,1
Tile2 = 2,1,1,0,1,1
Tile3 = 3,1,1,0,1,1
Tile4 = 1,2,1,0,0,0
Tile5 = 2,2,0,1,1,0
Tile6 = 3,2,1,0,1,0
Tile7 = 1,3,1,1,0,0
Tile8 = 2,3,0,1,0,1
Tile9 = 3,3,0,1,1,0

currentTile = Tile1
x = currentTile[0]
y = currentTile[1]
hasNotRun = True
#While loop which contains the program
while x != 3 or y != 1:

    #Set variables that need to be reset within the loop
    howManyDirections = 0
    travelPossibilities = ""
    #Find out which directions player can choose from
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
        #print out travel options
        print("You can travel: " + travelPossibilities + ".")

        hasNotRun = False

    #Let player choose direction to go
    direction = input("Direction: ")

    #Check if direction is choosable
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

    #Move player to next tile
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

#Print result when at tile x == 3 and y == 1 (Tile3)
print("Victory!")