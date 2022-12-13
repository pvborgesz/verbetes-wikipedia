class Word:
    def __init__(self, word):
        self.word = word
        self.count = 1
        self.points = 0
    
    def __str__(self):
        return f"Palavra: {self.word}, Ocorrências: {self.count}, Pontos: {self.points}"
    
    def isTitle(self, title):
        if self.word in title.lower():
            self.points += 10
            return True
        return False

    def isText(self, text):
        self.count += text.lower().count(self.word)
        self.points += text.lower().count(self.word)
        return self.count

    def getWord(self):
        return self.word