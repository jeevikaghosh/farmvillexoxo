import pygame
import sys
import time 
import random
from os import path 


username = ""
dispWidth=750
dispHeight=600
gameDisp=pygame.display.set_mode((dispWidth,dispHeight))
# clock=pygame.time.clock()

imageDir = path.join(path.dirname(__file__), 'image')



keyDict = {48:"0", 49:"1", 50:"2", 51:"3", 52:"4", 53:"5", 54:"6", 55:"7", 56 :"8", 57:"9", 
97:"a", 98:"b", 99:"c", 100:"d", 101:"e", 102:"f", 103:"g", 104:"h", 105:"i",  106:"j",  107:"k", 
108:"l", 109:"m", 110:"n", 111:"o", 112:"p", 113:"q", 114:"r", 115:"s", 116:"t", 117:"u", 118:"v",
119:"w", 120:"x", 121:"y",  122:"z",}
1 # pygame.K_2:"2", pygame.K_3:"3", pygame.K_4:"4", pygame.K_5:"5", pygame.K_6:"6", pygame.K_7:"7",pygame.K_8:"8", pygame.K_9:"9", pygame.K_a:"a", pygame.K_b:"b", pygame.K_c:"c",pygame.K_d:"d", pygame.K_e:"e", pygame.K_f:"f", pygame.K_g:"g", pygame.K_h:"h", pygame.K_i:"i", pygame.K_j:"j", pygame.K_k:"k", pygame.K_l:"l", pygame.K_m:"m", pygame.K_n:"n", pygame.K_o:"o", pygame.K_p:"p",pygame.K_q:"q", pygame.K_r:"r", pygame.K_s:"s", pygame.K_t:"t", pygame.K_u:"u", pygame.K_v:"v", pygame.K_w:"w", pygame.K_x:"x" pygame.K_y:"y", pygame.K_z:"z" }
pygame.init()
pygame.font.init()
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Farmville")
myfont = pygame.font.SysFont("monospace", 50)
myfont2 = pygame.font.SysFont("monospace", 23)

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



cameraX=0
cameraY=0
cameraDir=None

character=None
chosenCrop=None
cornTime=10
tomatoTime=20
cabbageTime=35



houseSize=int(dispWidth/5)
treeSize=int(dispWidth/6)
bugSize=int(dispWidth/20)
coinSize=int(dispWidth/10)



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



