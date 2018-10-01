# User creates list
# User can mutate or remove from list
# Print out new mutated, removed or unchanged list.

def mutate_list(a_list, index_num, v):
    ''' Inserts v at index index_num in a_list'''
    a_list.insert(index_num, v)
    
def remove_ch(a_list, index_num):
    ''' Removes character at index_num from a_list'''
    a_list.pop(index_num)
    
def get_list():
    ''' Reads in values for a list and returns the list '''
    user_list = input("Enter values in list separated by commas: ")
    user_list = user_list.split(",")
    user_list = [int(i) for i in user_list]
    return user_list

# Main program starts here
user_list = get_list()
print(user_list)
m_or_r = input("Enter choice (m,r): ")

if m_or_r == "m":
    mutationInput = input()
    userChoiceList = mutationInput.split(",")
    indexNumber = int(userChoiceList[0])
    replaceWith = int(userChoiceList[1])
    mutate_list(user_list, indexNumber, replaceWith)
elif m_or_r == "r":
    removeInput = int(input())
    remove_ch(user_list, removeInput)
print(user_list)