import pygame
import time 
import random
from globalvariables import *

class tile:

	def __init__(self,size, x, y, screen, currentImg, startTime=None):
	
		self.startTime=startTime
		self.size = size
		self.x = x
		self.y = y
		self.highlight=False
		self.currentImg = currentImg
		self.screen=screen
		self.bugs=False


	def __repr__(self):
		return ("x= %d y= %d startTime=" % (self.x, self.y))

	def clicked(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		return self.x+self.size > mouse[0] > self.x and self.y+self.size > mouse[1] > self.y and click[0]==1
		

	def changeClicked(self):
		self.clickedTile=True

	def hover(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		return self.x+self.size > mouse[0] > self.x and self.y+self.size > mouse[1] > self.y

	def highlight(self):
		if self.currentImg=="grasstile.jpg":

			if self.hover:
				self.highlight=True
			if self.highlight:
				tile(tileSize, singtile.x, singtile.y, gameDisp, "grasstilefaded.jpg")

	def draw(self):
		img=pygame.image.load(self.currentImg)
		scaleImage=pygame.transform.scale(img,(self.size,self.size))
		self.surface= pygame.Surface((self.size,self.size))
		self.surface.blit(scaleImage, (0,0))
		self.screen.blit(self.surface,(self.x,self.y))



