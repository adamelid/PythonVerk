#list_to_tuple function goes here
def list_to_tuple(a_list):
    a_tuple = ()
    intList = []
    try:
        for i, value in enumerate(a_list):
            intList.append(int(value))
            a_tuple += tuple(intList[i])
    except ValueError:
        print("Error. Please enter only integers.")
    return a_tuple
# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)