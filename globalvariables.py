import pygame
import sys
import time 
import random

dispWidth=750
dispHeight=600
gameDisp=pygame.display.set_mode((dispWidth,dispHeight))
# clock=pygame.time.clock()
pygame.init()
pygame.font.init()
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Farmville")

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



houseSize=int(dispWidth/5)
treeSize=int(dispWidth/6)
bugSize=int(dispWidth/20)



logo=pygame.image.load("farm112logo.png")
scaledLogo=pygame.transform.scale(logo,(int(dispWidth/2),int(dispHeight/5)))

house=pygame.image.load("house.png")
scaledHouse=pygame.transform.scale(house,(houseSize*2,houseSize))	

bush=pygame.image.load("bushflower.png")
scaledbush=pygame.transform.scale(bush,(int(houseSize),int(houseSize/2)))	


tree1=pygame.image.load("tree2.png")
scaledTree1=pygame.transform.scale(tree1,(treeSize,treeSize))	

tree2=pygame.image.load("tree3.png")
scaledTree2=pygame.transform.scale(tree2,(treeSize,treeSize))	


corn=pygame.image.load("corn.png")
scaledcorn=pygame.transform.scale(corn,(int(dispWidth/10),int(dispHeight/8)))	

cabbage=pygame.image.load("cabbag.png")
scaledcabbage=pygame.transform.scale(cabbage,(int(dispWidth/10),int(dispHeight/8)))

tomato=pygame.image.load("tomato.png")
scaledtomato=pygame.transform.scale(tomato,(int(dispWidth/10),int(dispHeight/8)))


farmgirl=pygame.image.load("farmgirl.jpg")
scaledFarmgirl=pygame.transform.scale(farmgirl,(int(dispWidth/3),int(dispHeight/2)))
scaledFarmgirl2=pygame.transform.scale(farmgirl,(int(dispWidth/6),int(dispHeight/4)))

farmboy=pygame.image.load("farmboy.png")
scaledFarmboy=pygame.transform.scale(farmboy,(int(dispWidth/3),int(dispHeight/2-dispHeight/15)))
scaledFarmboy2=pygame.transform.scale(farmboy,(int(dispWidth/6),int(dispHeight/4-dispHeight/15)))


spray=pygame.image.load("spray.png")
scaledSpray=pygame.transform.scale(spray,(treeSize,treeSize))	

bug=pygame.image.load("bug.png")
scaledBug=pygame.transform.scale(bug,(bugSize,bugSize))	



