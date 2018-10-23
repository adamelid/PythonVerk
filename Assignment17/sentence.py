class Sentence:
    def __init__(self, inputString):
        self.inputString = inputString
    def get_first_word(self):
        wordList = self.inputString.split()
        return wordList[0]
    def get_all_words(self):
        wordList = self.inputString.split()
        return wordList
    def replace(self, index, new_word):
        wordList = self.inputString.split()
        if len(wordList) >= index:
            wordList[index] = new_word
        self.inputString = " ".join(wordList)