import string

unique_letters = []
sentence = input("Input a sentence: ")
sentence = sentence.replace(" ","")

# Here you should add the missing part
for i, value in enumerate(sentence):
    if value not in unique_letters:
        if value not in string.punctuation:
            unique_letters += sentence[i]

print("Unique letters:", unique_letters)