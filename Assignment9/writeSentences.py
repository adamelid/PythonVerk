input_file = open("words.txt", "r")
output_file = open("sentences.txt", "a")

sentence = ""
sentence_empty = True

for line in input_file:
    word = ""
    for char in line:
        if char != '\n':
            word += char
            sentence_empty = False
        elif sentence_empty == False:
            word += ' '
    sentence += word
    if word == '. ':
        print(sentence)
        print(sentence,file=output_file)
        sentence = ""
        sentence_empty = True

print(sentence)
print(sentence,file=output_file)