import xml.etree.ElementTree as ET
from Model.Word import Word
from Controllers.WordController import WordController
from fastapi import FastAPI, Request, Header, Response
from fastapi.middleware.cors import CORSMiddleware

tree = ET.parse('data/verbetesWikipedia.xml') 
root = tree.getroot()

words = []

words.sort(key=lambda x: x['relevancia'], reverse=True)

for page in root.findall('page'):
    words.append(Word(page.find('title').text.lower()))

for page in root.findall('page'):
    for word in words:
        if len(word.word) > 3:
            if word.isTitle(page.find('title').text):
                word.isText(page.find('text').text)
                # print(word.__str__())

searchResponse = WordController.searchWord('computer', words)



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


@app.get("/search")
async def root(request: Request):
    word = request.headers['word']
    searchResponse = WordController.searchWord(word, words)
    return {"data": searchResponse}
