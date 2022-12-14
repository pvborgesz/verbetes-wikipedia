import xml.etree.ElementTree as ET
from Model.Word import Word
from Controllers.WordController import WordController
from fastapi import FastAPI, Request, Header, Response
from fastapi.middleware.cors import CORSMiddleware
import time

inicio = time.time()

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tree = ET.parse('data/verbetesWikipedia.xml') 
root = tree.getroot()

words = {}
processedWords = {}
significantWords = {}
visited = {} # lista de paginas visitadas

# definir todas as pages, 
# definir todas as palavras signicantes (len > 3, isalpha)
# processar todas as palavras significativas, adicionando a cada pagina que aparece, o numero de vezes que aparece e o numero de pontos que tem
# fazer a busca por palavra, retornando todas as paginas que contem a palavra, ordenadas por pontos

# for page in root.findall('page'):
#     # add in the words dict
#     words[page.find('title').text.lower()] = Word(page.find('title').text.lower(), page.find('text').text.lower(), page.find('title').text.lower())
#     # words.append(Word(page.find('title').text.lower(), page.find('text').text.lower(), page.find('title').text.lower()))

# # armazenando todas as palavras significantes
# for word in words:
#     if len(word) > 3 and word.isalpha():
#         significantWords[word] = words[word]

# # pontuar todas as palavras
# for page in root.findall('page'):
#     for word in significantWords:
#         if word in page.find('title').text.lower():
#             significantWords[word].isTitle(page.find('title').text.lower())
#         if word in page.find('text').text.lower():
#             significantWords[word].isText(page.find('text').text.lower())

# print("Terminei de pontuar")
# processar todas as palavras significativas, adicionando a cada pagina que aparece, o numero de vezes que aparece e o numero de pontos que tem


# print dict with word  'space'


# searchResponse = WordController.searchWord('computer', words)
# searchResponse = WordController.searchWordByPoints('computer', words, root)


print(WordController.initIndex(root))

fim = time.time()
@app.get("/search")
async def root(request: Request):
    word = request.headers['word']
    # searchResponse = WordController.searchWord(word, words)
    searchResponse = WordController.searchWordByPoints(word, words,significantWords)
    
    print("Tempo de execução: ", fim - inicio)
    return {"data": searchResponse}
