import xml.etree.ElementTree as ET
from Model.Word import Word
from Controllers.WordController import WordController
from fastapi import FastAPI, Request, Header, Response
from fastapi.middleware.cors import CORSMiddleware
import time

inicio = time.time()

app = FastAPI()
print("Servidor Iniciado")

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

words = WordController.initIndex(root)

nonStopWords = WordController.searchNonStopWords(words)
response = WordController.fitWords(words, nonStopWords)

fim = time.time()
print("Tempo de execução: ", fim - inicio)
@app.get("/search")
async def root(request: Request):
    word = request.headers['word']
    print("Procurando pela palavra: ", word)
    searchResponse = WordController.findByWord(word, words)
    # searchResponse = WordController.searchWord(word, words)
    # searchResponse = WordController.searchWordByPoints(word, words,significantWords)

    print("Tempo de execução: ", fim - inicio)
    return {"data": searchResponse}

@app.get("/findTwoWords")
async def root(request: Request):
    word1 = request.headers['word1']
    word2 = request.headers['word2']
    print("Procurando pelas palavras: ", word1, word2)
    searchResponse = WordController.findByTwoWords(word1, words)
    searchResponse2 = WordController.findByTwoWords(word2, words)
    # searchResponse = WordController.searchWord(word, words)
    # searchResponse = WordController.searchWordByPoints(word, words,significantWords)
    response = searchResponse + searchResponse2
    response.sort(key=lambda x: x.points, reverse=True)
    response = set(response)
    print("Tempo de execução: ", fim - inicio)
    return {"data": response}
