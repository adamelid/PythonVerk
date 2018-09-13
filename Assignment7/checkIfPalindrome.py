def check_palindrome(someString):
    newString = ""
    for i in someString:
        if i not in [",","!",".","'"," "]:
            newString+=i
    if newString.lower() == newString.lower()[::-1]:
        return True
    else:
        return False

in_str = input("Enter a string: ")

if check_palindrome(in_str):
    print('"' + in_str + '"' + " is a palindrome.")
else:
    print('"' + in_str + '"' + " is not a palindrome.")