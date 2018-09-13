# The function definition goes here
def range_check(number):
    if number < 555 and number > 1:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if range_check(num):
    print(str(num) + " is in range.")
else:
    print(str(num) + " is outside the range!")