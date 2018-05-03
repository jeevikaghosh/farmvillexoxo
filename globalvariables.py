import pygame
import sys
import time 
import random
from os import path 


username = ""
dispWidth=750
dispHeight=600
gameDisp=pygame.display.set_mode((dispWidth,dispHeight))

#directory variables
imageDir = path.join(path.dirname(__file__), 'image')

soundDir = path.join(path.dirname(__file__), 'audio')


#dict of letters
keyDict = {48:"0", 49:"1", 50:"2", 51:"3", 52:"4", 53:"5", 54:"6", 55:"7", 56 :"8", 57:"9", 
97:"a", 98:"b", 99:"c", 100:"d", 101:"e", 102:"f", 103:"g", 104:"h", 105:"i",  106:"j",  107:"k", 
108:"l", 109:"m", 110:"n", 111:"o", 112:"p", 113:"q", 114:"r", 115:"s", 116:"t", 117:"u", 118:"v",
119:"w", 120:"x", 121:"y",  122:"z",}

#initialising all of pygames modules
pygame.init()
pygame.font.init()
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Farmville")
myfont = pygame.font.SysFont("monospace", 50)
myfont2 = pygame.font.SysFont("monospace", 23)

#defining colors
white=(255,255,255)
brightGreen=(0,255,0)
green = (50,205,50)
black = (0,0,0)
backgroundGreen=(0,153,0)
brightPink=(255,105,180)
pink=(255,20,147)
blue=(30,144,255)
brightBlue=(0,191,255)
orangeRed=(255,140,0)
red=(255,69,0)
yellow=(255,255,0)

#making position variables for all the image placements 
logoX=dispWidth/5
logoY=dispHeight/6-50
startWidth = dispWidth/5
startHeight = dispHeight/7
startX=2*dispWidth/5
StartY=4*dispHeight/5
usernameY=2*dispHeight/5
userButY=3*dispHeight/5-50
userButX=dispWidth/5+50
userWidth=dispWidth/2
userHeight=dispHeight/10
welcomeTextX=dispWidth/7
charButY=dispHeight/4
charButWidth=dispWidth/3
CharButHeight=dispHeight/2
maleCharButX=dispWidth/12
femCharButX=3*dispWidth/5-dispWidth/25
margin=dispHeight/30
cropButWidth = dispWidth/7
cropButHeight = dispHeight/8
cropButX=4.5*dispWidth/5
cornY=dispHeight/5+dispHeight/20
cabbageY=2*dispHeight/5+dispHeight/20
tomatoY=3*dispHeight/5+dispHeight/20
HouseX=dispWidth/3
saveButX=4*dispWidth/5-40
saveButY=dispHeight/15
contX=2*dispWidth/5-40
contY=3*dispHeight/5
contWidth = dispWidth/3
contHeight = dispHeight/8
friendY1=2*dispHeight/5-50
friendY2=3*dispHeight/5
friendX1=dispWidth/5-70
friendX2=2*dispWidth/5+10
friendX3=4*dispWidth/5-70
friendButHeight=dispHeight/10
friendButHeigth=dispHeight/10
houseSize=int(dispWidth/5)
treeSize=int(dispWidth/6)
bugSize=int(dispWidth/20)
coinSize=int(dispWidth/10)

#camera and other random variables
cameraX=0
cameraY=0
cameraDir=None

character=None
chosenCrop=None
cornTime=10
tomatoTime=20
cabbageTime=30

#loading and scaling the images for future use

theme=pygame.mixer.Sound(path.join(soundDir,"farmtheme.ogg"))

background=pygame.mixer.Sound(path.join(soundDir,"farmbackground.ogg"))

logo=pygame.image.load(path.join(imageDir,"farm112logo.png"))
scaledLogo=pygame.transform.scale(logo,(int(dispWidth/2),int(dispHeight/5)))

house=pygame.image.load(path.join(imageDir,"house.png"))
scaledHouse=pygame.transform.scale(house,(houseSize*2,houseSize))

house2=pygame.image.load(path.join(imageDir,"house2.png"))
scaledHouse2=pygame.transform.scale(house2,(houseSize*2,houseSize))		

house3=pygame.image.load(path.join(imageDir,"farmhouse.gif"))
scaledHouse3=pygame.transform.scale(house3,(houseSize*2,houseSize))	

bush=pygame.image.load(path.join(imageDir,"bushflower.png"))
scaledbush=pygame.transform.scale(bush,(int(houseSize),int(houseSize/2)))	

tree1=pygame.image.load(path.join(imageDir,"tree2.png"))
scaledTree1=pygame.transform.scale(tree1,(treeSize,treeSize))	

tree2=pygame.image.load(path.join(imageDir,"tree3.png"))
scaledTree2=pygame.transform.scale(tree2,(treeSize,treeSize))	

corn=pygame.image.load(path.join(imageDir,"corn.png"))
scaledcorn=pygame.transform.scale(corn,(int(dispWidth/10),int(dispHeight/8)))	

cabbage=pygame.image.load(path.join(imageDir,"cabbag.png"))
scaledcabbage=pygame.transform.scale(cabbage,(int(dispWidth/10),int(dispHeight/8)))

tomato=pygame.image.load(path.join(imageDir,"tomato.png"))
scaledtomato=pygame.transform.scale(tomato,(int(dispWidth/10),int(dispHeight/8)))

farmgirl=pygame.image.load(path.join(imageDir,"farmgirl.jpg"))
scaledFarmgirl=pygame.transform.scale(farmgirl,(int(dispWidth/3),int(dispHeight/2)))
scaledFarmgirl2=pygame.transform.scale(farmgirl,(int(dispWidth/6),int(dispHeight/4)))

farmboy=pygame.image.load(path.join(imageDir,"farmboy.png"))
scaledFarmboy=pygame.transform.scale(farmboy,(int(dispWidth/3),int(dispHeight/2-dispHeight/15)))
scaledFarmboy2=pygame.transform.scale(farmboy,(int(dispWidth/6),int(dispHeight/4-dispHeight/15)))

spray=pygame.image.load(path.join(imageDir,"spray.png"))
scaledSpray=pygame.transform.scale(spray,(treeSize,treeSize))	

bug=pygame.image.load(path.join(imageDir,"bug.png"))
scaledBug=pygame.transform.scale(bug,(bugSize,bugSize))	

coins=pygame.image.load(path.join(imageDir,"coins.png"))
scaledCoins=pygame.transform.scale(coins,(coinSize,coinSize))

soundOn=pygame.image.load(path.join(imageDir,"soundon.png"))
scaledSoundOn=pygame.transform.scale(soundOn,(coinSize,coinSize))	

soundOff=pygame.image.load(path.join(imageDir,"soundoff.png"))
scaledSoundOff=pygame.transform.scale(soundOff,(coinSize,coinSize))	

speech=pygame.image.load(path.join(imageDir,"speech.png"))
scaledSpeech=pygame.transform.scale(speech,(int(4*houseSize/3),houseSize))	

instructions=pygame.image.load(path.join(imageDir,"instructions.png"))
scaledInstructions=pygame.transform.scale(instructions,(dispWidth,dispHeight))	

information=pygame.image.load(path.join(imageDir,"cropinfo.png"))
scaledInformation=pygame.transform.scale(information,(dispWidth,dispHeight))	

farmtheme=pygame.image.load(path.join(imageDir,"farmtheme.jpg"))
scaledfarmtheme=pygame.transform.scale(farmtheme,(dispWidth,dispHeight))	

