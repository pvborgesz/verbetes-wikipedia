class WordController:
    def __init__(self, word):
        self.word = word
        self.wordView = WordView(self.word)
        self.wordView.show()

    def getWord(self):
        return self.word

    def getWordView(self):
        return self.wordView

    def updateWord(self, word):
        self.word = word
        self.wordView.updateWord(word)

    def updateWordView(self, wordView):
        self.wordView = wordView
        self.wordView.show()

    def isTitle(self, title):
        if self.word in title.lower():
            self.points += 10
            return True
        return False
        
    def isText(self, text):
        self.count += text.lower().count(self.word)
        self.points += text.lower().count(self.word)
        return self.count

    def searchWord(word, words):
        searchResponse = []
        # words.sort(key=lambda x: x['relevancia'], reverse=True)
        for specificWord in words: 
            if word in specificWord.getWord():
                searchResponse.append(specificWord)
        searchResponse.sort(key=lambda x: x.points, reverse=True)
        # for word in searchResponse:
        #     print(word.__str__())
        return searchResponse