import pygame
import time 
import random

pygame.init()
pygame.font.init()
dispWidth=650
dispHeight=450

lightBlue= (200,255,255)
backgroundGreen=(0,153,0)
white=(255,255,255)
gameDisp=pygame.display.set_mode((dispWidth,dispHeight))

pygame.display.set_caption("Farmville")
clock=pygame.time.Clock()
numOfTiles=6

crashed= False
tileSize=int(dispWidth/numOfTiles)

#grass= pygame.image.load("grass.png")
#logo= pygame.image.load("LOGOfarm.png")

class tile:

	def __init__(self,size, x, y, screen):
		self.tileStatus = "empty"
		self.size = size
		self.x = x
		self.y = y
		self.currentFile = "grasstile.jpg"
		img=pygame.image.load(self.currentFile)
		scaleImage=pygame.transform.scale(img,(size,size))
		self.surface= pygame.Surface((size,size))
		self.surface.blit(scaleImage, (0,0))
		self.screen=screen

		self.screen.blit(self.surface,(self.x,self.y))


	def clicked(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		return self.x+self.size > mouse[0] > self.x and self.y+self.size > mouse[1] > self.y and click[0]==1

	def hover(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		return self.x+self.size > mouse[0] > self.x and self.y+self.size > mouse[1] > self.y

	# def tileType(file, size):
	# 	tile=pygame.image.load(file)
	# 	tile=pygame.transform.scale(tile,(tileSize,tileSize))
	# 	surface= pygame.Surface((tileSize,tileSize))
	# 	surface.blit(tile, (0,0))
	# 	return surface

	# grassTile= tileType("grasstile.jpg", tileSize)

gameDisp.fill(backgroundGreen)

allTiles = []

for i in range(0,numOfTiles*tileSize,tileSize):
	for j in range(0,numOfTiles*tileSize,tileSize):
		newTile = tile(tileSize, i, j, gameDisp)
		allTiles.append(newTile)

while not crashed: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed=True


		for tile in allTiles:
			if tile.clicked():
				print("clicked tile at " + str(tile.x) + ", " + str(tile.y))
			if tile.hover():
				print("hovered tile at " + str(tile.x) + ", " + str(tile.y))

		pygame.display.update()
		clock.tick(60)

pygame.quit()






