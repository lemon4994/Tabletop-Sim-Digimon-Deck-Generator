import sys

eggs = ["-01","001","002","003","004","005","006"]
eggstras = ["BT1-007","BT1-008","BT2-007","EX2-007","BT13-007","P-148","P-149","P-157"]
eggceptions = ["EX1-001","EX1-002","EX1-003","EX1-004","EX1-005","EX1-006","EX3-003","EX3-004","EX3-005","EX3-006","EX4-005","EX4-006","LM-001","LM-002","LM-003","LM-004","LM-005","LM-006","RB1-004","RB1-005","RB1-006","P-001","P-002","P-003","P-004","P-005","P-006"]

def filegenerator(decklist):
    counter = 0 #number of cards in deck
    contents = '{"ObjectStates":[{"Name":"Deck","Transform":{"posX":0,"posY":0,"posZ":0,"rotX":0,"rotY":180,"rotZ":180,"scaleX":2.35946536,"scaleY":1.0,"scaleZ":2.35946536},"Nickname":"Digimon Deck","DeckIDs":['
    for card in decklist:
        counter += 1
        contents += f'{counter *100},'
    contents = contents[:-1]
    contents += '],"CustomDeck":{'

    for i in range(counter):
        if decklist[i][-3:] in eggs and decklist[i] not in eggceptions:
            cardBack = "https://file.garden/ZUWEKmrAFHgJ5X5e/DigimonBackEgg.jpg"
        elif decklist[i] in eggstras:
            cardBack = "https://file.garden/ZUWEKmrAFHgJ5X5e/DigimonBackEgg.jpg"
        else:
            cardBack = "https://file.garden/ZUWEKmrAFHgJ5X5e/DigimonBack.jpg"
        contents += f'"{i+1}":{{"FaceURL":"https://world.digimoncard.com/images/cardlist/card/{decklist[i]}.png","BackURL":"{cardBack}","NumHeight":1,"NumWidth":1,"BackIsHidden":true}},'

    contents = contents[:-1]
    contents += '},"ContainedObjects":['
    for i in range(counter):
        if decklist[i][-3:] in eggs and decklist[i] not in eggceptions:
            cardBack = "https://file.garden/ZUWEKmrAFHgJ5X5e/DigimonBackEgg.jpg"
        elif decklist[i] in eggstras:
            cardBack = "https://file.garden/ZUWEKmrAFHgJ5X5e/DigimonBackEgg.jpg"
        else:
            cardBack = "https://file.garden/ZUWEKmrAFHgJ5X5e/DigimonBack.jpg"
        contents += f'{{"Name":"CardCustom","Transform":{{"posX":0,"posY":0,"posZ":0,"rotX":0,"rotY":180,"rotZ":180,"scaleX":2.35946536,"scaleY":1.0,"scaleZ":2.35946536}},"Nickname":"{decklist[i]}", "CardID":{(i+1)*100},"CustomDeck":{{"{i+1}":{{"FaceURL":"https://world.digimoncard.com/images/cardlist/card/{decklist[i]}.png","BackURL":"{cardBack}","NumHeight":1,"NumWidth":1,"BackIsHidden":true}}}}}},'

    contents = contents[:-1]
    contents += ']}]}'
    return contents

file = "Digimon Deck.json"
input = input("Enter Decklist: ")
#input comes from digimoncard.dev TTS export

try:
    decklist = eval(input)
except:
    print("Invalid List")
    sys.exit()
#converts string to list

decklist.pop(0) #first element is garbage
jsoncontents = filegenerator(decklist)

with open(file, "w") as f:
    f.write(jsoncontents)

print("Deck object generated successfully")