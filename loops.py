import pygame
import sys
import time 
import random
from button import Button
from farmgrid import tile
from globalvariables import *


def intro_loop():
	running = True
	while running: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 0
				
			gameDisp.fill(white)

			startButton = Button(green,100,100,100,100,gameDisp)


			startButton.addText("Start>",black)

			if startButton.clicked():
				return 1


			pygame.display.update()


def startGameLoop():
	running = True
	numOfTiles=6
	tileSize=int(dispWidth/numOfTiles)

	gameDisp.fill(backgroundGreen)

	allTiles = []

	for i in range(0,numOfTiles*tileSize,tileSize):
		for j in range(0,numOfTiles*tileSize,tileSize):
			newTile = tile(tileSize, i, j, gameDisp)
			allTiles.append(newTile)

	while running: 
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running=False


			for singtile in allTiles:
				if singtile.clicked():
					print("clicked tile at " + str(singtile.x) + ", " + str(singtile.y))
				if singtile.hover():
					print("hovered tile at " + str(singtile.x) + ", " + str(singtile.y))

			pygame.display.update()
