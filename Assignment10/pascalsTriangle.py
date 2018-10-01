# Function for creating rows.
def make_new_row(oldList):

    # Set first number in the new list
    new_list = [1]

    # Check if the old list is not empty
    if oldList:

        # Run for every number in the old list (besides first number which is always == 1)
        for i in range(1, len(oldList)):

            # Combine two numbers of old list and add to new list
            new_list.append(oldList[i] + oldList[i-1])

    # If old list is empty, then make the new list empty as well
    else:   
        new_list = []

    # Add 1 at the end of the new list
    new_list.append(1)

    # Return the finished new list
    return new_list

# Main program starts here - DO NOT CHANGE
height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []
for i in range(height):
    new_row = make_new_row(new_row)
    print(new_row)