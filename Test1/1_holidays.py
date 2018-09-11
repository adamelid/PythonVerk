monthInput = input("Month: ")
dayInput = input("Day: ")
newString = monthInput.capitalize() + " " + dayInput

if newString == "January 1":
    print("New year's day")
elif newString == "June 17":
    print("National holiday")
elif newString == "December 25":
    print("Christmas day")
else:
    print("Not a holiday")