file = open("test.txt","r")
fileContents = file.read()
fileContents = fileContents.replace(" ","")
fileContents = fileContents.replace("\n","")
print(fileContents)