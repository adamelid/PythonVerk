word = input("Enter a word: ")
vowels = "aeiou"
while word != ".":
    new_word = word
    word_has_vowels = False
    if word[0] in vowels:
        new_word = word + "yay"
    else:
        for i in new_word:
            if new_word[0] not in vowel:
                new_word = new_word[1::] + new_word[0]
            else:
                word_has_vowels = True
                break
        new_word += "ay"
    print(new_word)
    word = input("Enter a word: ") 
