#!/usr/bin/env python
import os
import sys
import random
import msvcrt as m
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
    def __init__(self, name, price, hitPoints, capacity, power,hpregen,shield, rarity):
        Item.__init__(self, name, price, "Hull")
        self.hitPoints = hitPoints
        self.capacity = capacity
        self.rarity = rarity
        self.power = power
        self.shield = shield
        self.hpregen = hpregen
    def toConsole(self,num):
        print("\t\tPick number "+str(num)+") [[ "+self.name+" ]]")
        print("\tCost:")
        print("\tSlots:")
        print("\tHP:")
        print("\tType: Hull (SPECIAL)")
        print("\tRarity: "+RarityToString(self.rarity)+"\n")
class Part(Item):
    def __init__(self, name, price, typeName, rarity, size, powerUse):
        Item.__init__(self, name, price, typeName)
        self.rarity = rarity
        self.size = size
        self.powerUse = powerUse
class Armour(Part):
    def __init__(self, name, hp, price, rarity, size, powerUse):
        Part.__init__(self, name, price, "Armour",rarity,size,powerUse)
        self.hp = hp
    def toConsole(self,num):
        print("\t\tPick number "+str(num)+") [[ "+self.name+" ]]")
        print("\tCost:"+str(self.price))
        print("\tSize:"+str(self.size))
        print("\tAdditional HP:"+str(self.hp))
        print("\tType: Armour")
        print("\tRarity: "+RarityToString(self.rarity)+"\n")
class Ship(object):
    def __init__(self):
        self.parts = list()
        self.hull = False
        self.hitPoints = 0
        self.slots = 0
        self.powerRemaining = 0
        self.hitPointsRegen = 0
        self.shield = 0
    def addPart(self, part):
        self.parts.append(part)
    def addArmour(self,armour):
        self.parts.append(armour)
        self.powerRemaining-=armour.powerUse
        self.hitPoints+=armour.hp
        self.slots-=armour.size
    def addHull(self,hull):
        self.hull = hull
        self.hitPoints+=hull.hitPoints
        self.powerRemaining+=hull.power
        self.slots+=hull.capacity
        self.hitPointsRegen+=hull.hpregen
        self.shield+=hull.shield
    def toConsole(self):
        if self.hull:
            print("This ship is a "+self.hull.name+" class vessel ")
            print("It has "+str(self.hitPoints)+" hitpoints.")
            print("It has "+str(self.shield)+" shield.")
            print("It has "+str(self.hitPointsRegen)+" repair.")
            print("It has "+str(self.powerRemaining)+" power remaining.")
            print("It has "+str(self.slots)+" slots remaining.\n")
            if len(self.parts)>0:
                print("It has the following parts equipped:")
                for part in self.parts:
                    print(" - "+part.name)
def getUserInt(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Please enter just a number")
       continue
    else:
       return userInput 

def draft(partsLibrary,userShip):
    os.system('cls')
    print("\nYour Coins: " + str(playerMoney)+"\n")
    userShip.toConsole()
    parts = list()
    partNames = list()
    for x in range(1, 4):
        part = draw(partsLibrary,x,partNames)
        part.toConsole(x)
        parts.append(part)
        partNames.append(part.name)
    selection = getUserInt("Please select a part by number: ")
    selectedPart = parts[selection-1]
    return selectedPart

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
ships_file_object  = open("./parts/hulls.txt","r")
for line in ships_file_object: 
    lineStats = line.split(",")

    hullName = lineStats[0]
    hullHitPoints = int(lineStats[1])
    hullCapacity = int(lineStats[2])
    hullShield = int(lineStats[3])
    hullHitPointsRegen = int(lineStats[4])
    hullPower = int(lineStats[5])
    hullPrice = int(lineStats[6])
    hullRarity = Rarity(int(lineStats[7]))

    currentHull = Hull(hullName,hullPrice,hullHitPoints,hullCapacity,hullPower,hullHitPointsRegen,hullShield, hullRarity)
    ships.append(currentHull)
armours = list()
armour_file_object  = open("./parts/armour.txt","r")
for line in armour_file_object: 
    lineStats = line.split(",")

    armourName = lineStats[0]
    armourHitPoints = int(lineStats[1])
    armourPrice = int(lineStats[2])
    armourSize = int(lineStats[3])
    armourPowerUse = int(lineStats[4])
    armourRarity = Rarity(int(lineStats[5]))

    currentArmour = Armour(armourName,armourHitPoints,armourPrice,armourRarity,armourSize,armourPowerUse)
    armours.append(currentArmour)

os.system('cls')
print("\t\t\tWelcome to shipBrawl")
print("\t\t The draft-based space combat game")
print("\t\tYou build a ship in 20 draft choices")
print("\t\t  Then fight against a random AI")
print("\tFirst of all, you have to choose a Hull for the ship to be based on.\n\tRemember, you only get a maximum of 100 coins to spend so choose wisely!")
userShip = Ship()
userShip.toConsole()
def PressAnyKeyToContinue():
    print("Press any key to continue...")
    m.getch()
PressAnyKeyToContinue()
hull = draft(ships,userShip)
userShip.addHull(hull)

armour = draft(armours,userShip)
userShip.addArmour(armour)
armour = draft(armours,userShip)
userShip.addArmour(armour)
armour = draft(armours,userShip)
userShip.addArmour(armour)

enemyShip = Ship()
hullName,hullPrice,hullHitPoints,hullCapacity,hullPower,hullHitPointsRegen,hullShield, hullRarity
enemyShip.addHull(Hull("Imperator II",200,200,100,50,10,0,3))
enemyShip.addArmour(Armour("Armour I",10,10,1,1,0))
enemyShip.addArmour(Armour("Armour I",10,10,1,1,0))
class FightShip(object):
    def __init__(self,ship):
        self.ship=ship
        self.hp = ship.hitPoints
def winnerIsYou():
    os.system('cls')
    print("WINNER IS YOU")
    PressAnyKeyToContinue()
    sys.exit(0)
def scrub():
    os.system('cls')
    print("YOUZ BAD N00B")
    PressAnyKeyToContinue()
    sys.exit(0)
def round(playerFightShip,enemyFightShip):
    os.system('cls')
    print("you shoot the enemy for 10 damage")
    enemyFightShip.hp-=10
    print("this leaves him on "+str(enemyFightShip.hp)+" hp.")
    if(enemyFightShip.hp<1):
        PressAnyKeyToContinue()
        winnerIsYou()
    else:
        print("enemy shoots you for 10 damage")
        playerFightShip.hp-=10
        print("this leaves you on "+str(playerFightShip.hp)+" hp.")
        if (playerFightShip.hp<1):
            PressAnyKeyToContinue()
            skrub()
        else:
            print("Noone died yet. Ready for next round?")
            PressAnyKeyToContinue()
            round(playerFightShip,enemyFightShip)

def fight(playerShip,enemyShip):
    os.system('cls')
    print("Two ships are going to battle.")
    print("_______________________  Your Ship:  _______________________\n\n")
    playerShip.toConsole()
    print("_______________________  Enemy Ship:  _______________________\n\n")
    enemyShip.toConsole()
    PressAnyKeyToContinue()
    playerFightShip = FightShip(playerShip)
    enemyFightShip = FightShip(enemyShip)
    round(playerFightShip,enemyFightShip)
fight(userShip,enemyShip)
#comment