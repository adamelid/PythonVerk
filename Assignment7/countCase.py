# Your function definition goes here
def count_case(someString):
    upperCount = 0
    lowerCount = 0
    for c in someString:
        if c.isupper():
            upperCount+=1
        elif c.islower():
            lowerCount+=1
    return upperCount, lowerCount

user_input = input("Enter a string: ")

# Call the function here
upper, lower = count_case(user_input)

print("Upper case count: ", upper)
print("Lower case count: ", lower)