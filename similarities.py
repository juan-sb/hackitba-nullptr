import string
import math

# text is what i recieve

def generateWordMap(text):
    wordList = text.split()
    D = {}
    for word in wordList:
        if word in D:
            D[word] = D[word]+1
        else:
            D[word] = 1
    return D

def dotProduct(D1, D2):
    sum = 0.0
    for key in D1:
        if key in D2:
            sum += (D1[key] * D2[key])
    return sum

def similarity(D1, D2):
    numerator = dotProduct(D1, D2)
    denominator = math.sqrt(dotProduct(D1,D1)*dotProduct(D2,D2))
    
    return numerator/denominator

text1 = "hola me soy nigga rojo"
text2 = "hola me llamo juana rojo"
d1 = generateWordMap(text1)
d2 = generateWordMap(text2)
print(similarity(d1, d2))