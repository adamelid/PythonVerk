initValue = int(input("Initial value: "))
step = int(input("Step: "))
totalSum = 0
numbString = ""
changingValue = initValue

while totalSum < 100:
    numbString += (str(changingValue) + " ")
    totalSum += changingValue
    changingValue += step
print(numbString)
print("Sum of series: " + str(totalSum))