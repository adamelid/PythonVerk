def to_list(string):
    string = string.replace(","," ")
    newList = string.split()
    return newList
# The main program starts here - DO NOT change it
the_string = input("Enter the string: ")
the_list = to_list(the_string)
print(the_list)