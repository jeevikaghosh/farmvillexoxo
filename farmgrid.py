import pygame
import time 
import random
from globalvariables import *

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




