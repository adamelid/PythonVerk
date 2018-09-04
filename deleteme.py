secs_str = input("Input seconds: ") # do not change this line
secs_int = int(secs_str)

hours = secs_int // 3600
minutes = (secs_int % 3600) // 60
seconds = ((secs_int % 3600) % 60)
print(hours,":",minutes,":",seconds) # do not change this line
