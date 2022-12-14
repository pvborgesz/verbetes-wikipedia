from Model.Word import Word
import xml.etree.ElementTree as ET
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
        
        for specificWord in words: 
            if word in specificWord.getWord() or word in specificWord.getText():
                searchResponse.append(specificWord)
        searchResponse.sort(key=lambda x: x.points, reverse=True)
        
        return searchResponse
    
    # def searchWordByPoints(word, words, significantWords):
    #     response = []
    #     for specificWord in words:
    #         if word in specificWord.getWord() or word in specificWord.getText():
    #             specificWord.isText(specificWord.getText())
    #             specificWord.isTitle(specificWord.getTitle())
    #             response.append(specificWord)
                
    #     response.sort(key=lambda x: x.points, reverse=True)
    #     return response

    def searchWordByPoints(word, words, significantWords):
        response = []
        for specificWord in words:
            if word in specificWord.getWord() or word in specificWord.getText():
                specificWord.isText(specificWord.getText())
                specificWord.isTitle(specificWord.getTitle())
                response.append(specificWord)
                
        response.sort(key=lambda x: x.points, reverse=True)
        return response

    def isInTitle(word, title):
        if word in title.lower():
            return True
        return False


    def initIndex(root):
        # i wanna use this to create a dict with words, texts and titles
        words = {}
        for child in root:
            title = child.find('title').text
            text = child.find('text').text
            for word in text.split():
                if word in words and len(word)>3:
                    words[word].append(Word(word, text, title))
                else:
                    words[word] = [Word(word, text, title)]
        return words

    #print(words['deadfolks'][0].__str__())

    def isTitle(word, title):
        if word in title.lower():
            return True
        return False

    def isText(word, text):
        return text.lower().count(word)

    def fitWords(words, allWords):
        response = []
        # i wanna map all the words in the dict to a list of words
        for word in words :
            if len(word)>3:
                for specificWord in allWords[word]:
                    # for each word, i wanna check if it is in the title
                    if WordController.isTitle(word, specificWord.getTitle()):
                        Word.isTitle(specificWord)
                    # for each word, i wanna check if it is in the text
                    Word.isText(specificWord, specificWord.getText())
                    response.append(specificWord)
        response.sort(key=lambda x: x.points, reverse=True)
        return response

    def searchNonStopWords(words):
        response = {}
        for i in words:
            if len(i) > 3:
                response[i] = words[i]
        return response
    
    def findByWord(word:str, words: dict):
        response = []
        #if have only one word
        #word is a string and words is a dict
        if len(word.split()) == 1:
            if word in words:
                response = words[word]
        else:
            for i in word.split():
                if i in words:
                    # i dont wanna repetead words
                    if i not in response:
                        response.append(words[i])
        try: 
            response.sort(key=lambda x: x.points, reverse=True)
        except: pass
        response = set(response)
        return response

    def findByTwoWords(word:str, words: dict):
        response = []
        #if have only one word
        #word is a string and words is a dict
        if len(word.split()) == 1:
            if word in words:
                response = words[word]
        else:
            for i in word.split():
                if i in words:
                    # i dont wanna repetead words
                    if i not in response:
                        response.append(words[i])
        try: 
            response.sort(key=lambda x: x.points, reverse=True)
            # response = set(response)
        except: pass
        
        return response

    # def findByWord( word:str, words: dict):
    #     response = {}
    #     #if have only one word
    #     if len(word.split()) == 1:
    #         if word in words:
    #             response = words[word]
    #     else:
    #         for i in word.split():
    #             if i in words:
    #                 # i dont wanna repetead words
    #                 if i not in response:
    #                     response[i] = words[i]
    #     return response