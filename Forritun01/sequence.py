n = int(input("Enter the length of the sequence: ")) # Do not change this line

a = 0
b = 0
c = 1
for i in range(0,n):
    print(a+b+c)
    total = a+b+c
    a = b
    b = c
    c = total
    if c == 2:
        a = 0