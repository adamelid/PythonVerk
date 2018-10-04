def merge_lists(firstList, secondList):
    mergedList = list(set(firstList + secondList))
    mergedList.sort()
    return mergedList

# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
