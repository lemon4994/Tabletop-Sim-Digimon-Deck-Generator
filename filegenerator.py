import os

def cardgenerator(nickname, cardID):
    return f'{{"Nickname":"{nickname}","CardID":"{cardID}","Name":"Card","Transform":{{"posX":0,"posY":0,"posZ":0,"rotX":0,"rotY":180,"rotZ":180,"scaleX":1,"scaleY":1,"scaleZ":1}}}}'

def filegenerator(decklist):
    counter = 1
    contents = '{"ObjectStates":{"Name":"DeckCustom","ContainedObjects":['
    for card in decklist:
        contents += cardgenerator(card, counter) + ','
        counter += 1
    contents = contents[:-1]
    contents += '],"DeckIDs":['
    for i in range(counter-1):
        contents += f'{i+1},'
    contents = contents[:-1]
    contents += '],"CustomDeck":{'
    for i in range(counter-1):
        contents += f'"{i+1}":{{"FaceURL":"https://images.digimoncard.io/images/cards/{decklist[i]}.jpg","BackURL":"http://cloud-3.steamusercontent.com/ugc/809997459557414686/9ABD9158841F1167D295FD1295D7A597E03A7487/","NumHeight":1,"NumWidth":1,"BackIsHidden":true}},'
    contents = contents[:-1]
    contents += '},"Transform":{"posX":0,"posY":1,"posZ":0,"rotX":0,"rotY":180,"rotZ":180,"scaleX":1,"scaleY":1,"scaleZ":1}}]}'
    
    print(contents)