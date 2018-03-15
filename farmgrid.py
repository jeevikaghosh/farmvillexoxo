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
numOfTiles=15

crashed= False
tileSize=int(dispWidth/numOfTiles)

#grass= pygame.image.load("grass.png")
#logo= pygame.image.load("LOGOfarm.png")

class tiles:
	def tileType(file, size):
		tile=pygame.image.load(file)
		tile=pygame.transform.scale(tile,(tileSize,tileSize))
		surface= pygame.Surface((tileSize,tileSize))
		surface.blit(tile, (0,0))
		return surface

	grassTile= tileType("grasstile.jpg", tileSize)

while not crashed: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed=True
		
			#if event.key==pygame.KEYDOWN:



		gameDisp.fill(backgroundGreen)

		for i in range(0,numOfTiles*tileSize,tileSize):
			for j in range(0,numOfTiles*tileSize,tileSize):
				gameDisp.blit(tiles.grassTile, (i, j))




		pygame.display.update()
		clock.tick(60)

pygame.quit()






