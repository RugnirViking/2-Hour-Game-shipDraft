#!/usr/bin/env python
import os
import sys
import random
from enum import Enum

playerMoney = 1000

class Rarity(Enum):
    COMMON = 1
    RARE = 2
    EPIC = 3
    RELIC = 4
    LEGENDARY = 5
    ARTEFACT = 6
    MYTHIC = 7

def RarityToString(rarity):
    if rarity == Rarity.COMMON:
        return "Common"
    elif rarity == Rarity.RARE:
        return "Rare"
    elif rarity == Rarity.EPIC:
        return "Epic"
    elif rarity == Rarity.RELIC:
        return "Relic"
    elif rarity == Rarity.LEGENDARY:
        return "Legendary"
    elif rarity == Rarity.ARTEFACT:
        return "Artefact"
    elif rarity == Rarity.MYTHIC:
        return "Mythic"
    else:
        return "???"+str(Rarity.COMMON==1)
class Item(object):
    def __init__(self, name, price, typeName):
        self.name = name
        self.price = price
        self.type = typeName

class Hull(Item):
    def __init__(self, name, price, hitPoints, capacity, rarity):
        Item.__init__(self, name, price, "Hull")
        self.hitPoints = hitPoints
        self.capacity = capacity
        self.rarity = rarity
    def toConsole(self,num):
        print("\t\tPick number "+str(num)+") [[ "+self.name+" ]]")
        print("\tCost:")
        print("\tSlots:")
        print("\tHP:")
        print("\tType: Hull (SPECIAL)")
        print("\tRarity: "+RarityToString(self.rarity)+"\n")

class Ship(object):
    def __init__(self, hull):
        self.hull = hull
        self.parts = list()
    def addPart(self, part):
        self.parts.append(part)

def getUserInt(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Please enter just a number")
       continue
    else:
       return userInput 
       break
def draft(partsLibrary):
    parts = list()
    partNames = list()
    for x in range(0, 3):
        part = draw(ships,x,partNames)
        part.toConsole(x)
        parts.append(part)
        partNames.append(part.name)
def draw(partsLibrary,num,partNames):
    commonParts = list()
    rareParts = list()
    epicParts = list()

    for part in partsLibrary:
        if part.rarity == Rarity.COMMON:
            commonParts.append(part)
        elif part.rarity == Rarity.RARE:
            rareParts.append(part)
        elif part.rarity == Rarity.EPIC:
            epicParts.append(part)
        # TODO: ill add more rarities later
    
    roll = random.randrange(1,1000)
    part = 0
    if roll<800:
        ## common time
        while True:
            part = commonParts[random.randrange(len(commonParts))]
            if not part.name in partNames:
                return part
    elif roll<950:
        ## rare time
        while True:
            part = rareParts[random.randrange(len(rareParts))]
            if not part.name in partNames:
                return part
    elif roll<990:
        ## epic time
        while True:
            part = epicParts[random.randrange(len(epicParts))]
            if not part.name in partNames:
                return part
    else:
        # wildcard
        while True:
            part = partsLibrary[random.randrange(len(partsLibrary))]
            if not part.name in partNames:
                return part
    part.toConsole(num)

ships = list()
file_object  = open("./parts/hulls.txt","r")
for line in file_object: 
    lineStats = line.split(",")

    hullName = lineStats[0]
    hullHitPoints = lineStats[1]
    hullCapacity = lineStats[2]
    hullPrice = lineStats[6]
    hullRarity = Rarity(int(lineStats[7]))

    currentHull = Hull(hullName,hullPrice,hullHitPoints,hullCapacity,hullRarity)
    ships.append(currentHull)
os.system('cls')
print("\t\t\tWelcome to shipBrawl")
print("\t\t The draft-based space combat game")
print("\t\tYou build a ship in 20 draft choices")
print("\t\t  Then fight against a random AI")
print("\tFirst of all, you have to choose a Hull for the ship to be based on.\n\tRemember, you only get a maximum of 100 coins to spend so choose wisely!")
print("\nYour Coins: " + str(playerMoney)+"\n")

draft(ships)
