#Path to git repo - https://github.com/adamelid/PythonVerk/tree/master/TileTraveller

# 1. Which implementation was easier and why?
#   - In my opinion programming with functions is way easier than without, mainly because it streamlines and therefore simplifies the coding.
# 2. Which implementation is more readable and why?
#   - I'm not sure which implementation is more readable since if you were to read the main code with functions, -
#   - you would have to scroll up to read what the functions contain, although reading without functions could be -
#   - too confusing as well.
# 3. Which problems in the first implementation were you able to solve with the latter implementation?
#   - I didn't really have any problems with the first implementation, so the latter implementation did not change much, -
#   - the only main difference between the two was the addition of functions instead of a long drawn out program.

#Algorithm is as follows:
#While not at final tile.
#----Show possible directions.
#----Player chooses direction.
#----Check if direction is valid.
#----Move to chosen tile if valid.
#Print victory result.

#Set static variables.
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

#Finds out which directions player can choose from.
def possible_directions(currentTile):
    #Set variables that need to be reset every call.
    howManyDirections = 0
    travelPossibilities = ""
    #If there are no walls, add that direction to possible directions.
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
    return travelPossibilities

#Checks if direction is choosable
def check_if_choosable(direction,currentTile,x,y):
    if direction.lower() == "n" and currentTile[3] == False:
        y += 1
    elif direction.lower() == "e" and currentTile[4] == False:
        x += 1
    elif direction.lower() == "s" and currentTile[5] == False:
        y -= 1
    elif direction.lower() == "w" and currentTile[2] == False:
        x -= 1
    else:
        print("Not a valid direction!")
    return x,y

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

    #Print out travel options.
    print("You can travel: " + possible_directions(currentTile) + ".")

    #Ask player in which direction he would like to go.
    direction = input("Direction: ")

    #See if the chosen direction is valid.
    x, y = check_if_choosable(direction,currentTile,x,y)

    #Move player to chosen tile.
    currentTile = move_player(x,y,currentTile)

#Print result when at tile x == 3 and y == 1 (Tile3)
print("Victory!")