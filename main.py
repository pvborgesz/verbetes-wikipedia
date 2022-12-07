import xml.etree.ElementTree as ET

tree = ET.parse('data/verbetesWikipedia.xml') 
root = tree.getroot()


# print(len(root.findall('page')))

# for page in root.findall('page'):
#     print(page.find('title').text, page.find('id').text)

count = 0

# for page in root.findall('page'):
#     if 'computer' in page.find('title').text.lower():
#         print(page.find('id').text,page.find('title').text)
#         count +=1
# print (count)

# for page in root.findall('page'):
#     if 'computer' in page.find('title').text.lower():
#         print(page.find('id').text,page.find('title').text, "Ocorrências: ", int(page.find('title').text.count('computer')) + 1)


# for page in root.findall('page'):
#     if 'computer' in page.find('title').text.lower():
#         print(page.find('id').text,page.find('title').text, "Ocorrências: ", int(page.find('title').text.count('computer')) + 1)


# for page in root.findall('page'):
#     if 'computer' in page.find('text').text.lower():
#         print(page.find('id').text,page.find('title').text, "Ocorrências: ", (page.find('text').text.count('computer')))


# for page in root.findall('page'):
#     if 'computer' in page.find('title').text.lower():
#         print(page.find('id').text,"|",page.find('title').text,"| Ocorrências: ", (page.find('text').text.lower().count('computer')))


# words = []
# for page in root.findall('page'):
#     if 'computer' in page.find('title').text.lower():
#         words.append({"id": page.find('id').text, "title":page.find('title').text,"quantidade": (page.find('text').text.lower().count('computer'))})
# words.sort(key=lambda x: x['quantidade'], reverse=True) 

# procurar em todos os verbetes o número de ocorrências da palavra "computer" no título e no texto, verbetes com 'computer' no titulo tem maior peso
# ocorrencia no titulo += 10, no texto += 1
# ordenar por quantidade de ocorrências


words = []
for page in root.findall('page'):
    if 'computer' in page.find('title').text.lower():
        words.append({"id": page.find('id').text, "title":page.find('title').text,"relevancia": (page.find('text').text.lower().count('computer')) + 10})
    else:
        words.append({"id": page.find('id').text, "title":page.find('title').text,"relevancia": (page.find('text').text.lower().count('computer'))})
# words = []
# for page in root.findall('page'):
#     words.append({"id": page.find('id').text, "title":page.find('title').text,"relevancia": (page.find('text').text.lower().count('computer')) + 10})
words.sort(key=lambda x: x['relevancia'], reverse=True)

for i in words:
    print(i)
