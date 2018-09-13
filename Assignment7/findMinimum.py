# find_min function definition goes here
def find_min(number1, number2):
    if number1 >= number2:
        return number2
    else:
        return number1

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
    
# Call the function here
minimum = find_min(first, second)
print("Minimum: ", minimum)