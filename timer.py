import pygame
import time 
import random
# from globalvariables import *
import math 

dispWidth=750
dispHeight=600
gameDisp=pygame.display.set_mode((dispWidth,dispHeight))
# clock=pygame.time.clock()
pygame.init()


# Center and radius of pie chart
cx, cy, r = 100, 320, 75

# Background circle
pygame.draw.circle(gameDisp, (17, 153, 255), (cx, cy), r)

# Calculate the angle in degrees
# angle = val*360/total

# Start list of polygon points
p = [(cx, cy)]

# Get points on arc
for n in range(0,90):
    x = cx + int(r*math.cos(n*math.pi/180))
    y = cy+int(r*math.sin(n*math.pi/180))
    p.append((x, y))
p.append((cx, cy))

# Draw pie segment
if len(p) > 2:
    pygame.draw.polygon(gameDisp, (0, 0, 0), p)



# class timer:

# 	def __init__(self, x, y, screen, time):
# 		# self.tileStatus = "empty"
# 		self.startTime = startTime
# 		self.radius = radius
# 		self.x = x
# 		self.y = y
# 		self.highlight = False
# 		self.currentImg = currentImg
# 		img=pygame.image.load(self.currentImg)
# 		scaleImage=pygame.transform.scale(img,(size,size))
# 		self.surface= pygame.Surface((size,size))
# 		self.surface.blit(scaleImage, (0,0))
# 		self.screen=screen
# 		self.screen.blit(self.surface,(self.x,self.y))
# 		self.clickedTile=False

