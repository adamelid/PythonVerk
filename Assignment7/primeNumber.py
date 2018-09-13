# is_prime function definition goes here
def is_prime(number):
    if number == 2:
        return True
    else:
        for i in range(2, number):
            if (number % i == 0):
                return False
        return True

num = int(input("Input an integer greater than 1: "))
if is_prime(num):
    print(str(num) + " is a prime")
else:
    print(str(num) + " is not a prime")
# Call the function here and print out the appropriate message