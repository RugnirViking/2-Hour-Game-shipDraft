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
    def __init__(self, name, price, type):
        self.name = name
        self.price = price

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

def draw(partsLibrary):
    commonParts = list()
    rareParts = list()
    epicParts = list()

    print random.randrange(1,1000)
    


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
pickNum=1
draw(ships)
# for hull in ships:
#     hull.toConsole(pickNum)
#     pickNum+=1