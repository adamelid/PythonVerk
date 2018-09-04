stars = int(input("Max number of stars: ")) # Do not change this line

stars_str = str("*")

for x in range(stars -1):
    print(stars_str)
    stars_str = stars_str + "*"



for b in range(stars -1 , -1, -1):
    bullshit_str = str("*")
    for l in range(b):
        bullshit_str = bullshit_str + "*"
    print(bullshit_str)