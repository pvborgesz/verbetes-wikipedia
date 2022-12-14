class Word:
    def __init__(self, word, text, title):
        self.word = word
        self.text = text
        self.title = title
        self.count = 1
        self.points = 0
    
    def __str__(self):
        return self.word + " "  + " " + self.title + " " + str(self.count) + " " + str(self.points)
    
    def isTitle(self):
        self.points += 10
        return True

    def isText(self, text):
        self.count += text.lower().count(self.word)
        self.points += text.lower().count(self.word)
        return self.count

    def getWord(self):
        return self.word
    
    def getText(self):
        return self.text
    
    def getTitle(self):
        return self.title
    
    def getPoints(self):
        return self.points