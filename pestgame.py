import pygame
import sys
import time 
import random
from button import Button
from farmgrid import tile
from globalvariables import *


class Spray(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image=scaledSpray
		self.rect=self.image.get_rect()
		self.rect.center=(int(dispWidth/2), int(5*dispHeight/6))
		self.speed=8
		self.moveX=0
		self.moveY=0

	def update(self):

		self.moveX=0
		self.moveY=0
		
		pressedKey=pygame.key.get_pressed()
		if pressedKey[pygame.K_LEFT]:
			self.moveX=-self.speed
		if pressedKey[pygame.K_RIGHT]:
			self.moveX=+self.speed
		if pressedKey[pygame.K_UP]:
			self.moveY=-self.speed
		if pressedKey[pygame.K_DOWN]:
			self.moveY=self.speed
		self.rect.x+=self.moveX
		self.rect.y+=self.moveY



class Bugs(pygame.sprite.Sprite):
	def __init__(self, image, direction):
		super().__init__()
		self.direction=direction
		self.image=image
		self.rect=self.image.get_rect()
		if self.direction=="top":
			self.rect.x=random.randint(0,dispWidth-self.rect.width)
			self.rect.y=random.randint(-int(dispHeight/2),-self.rect.height)
			self.speedX=random.randint(-3,3)
			self.speedY=8
		if self.direction=="bottom":
			self.rect.x=random.randint(0,dispWidth-self.rect.width)
			self.rect.y=random.randint(self.rect.height+dispHeight,int(dispHeight*1.5))
			self.speedX=random.randint(-3,3)
			self.speedY=-8
		if self.direction=="right":
			self.rect.y=random.randint(0,dispHeight-self.rect.height)
			self.rect.x=random.randint(self.rect.width+dispWidth,int(dispWidth*1.5))
			self.speedX=-8
			self.speedY=random.randint(-3,3)
		if self.direction=="left":
			self.rect.x=random.randint(0,dispHeight-self.rect.height)
			self.rect.y=random.randint(-int(dispWidth/2),-self.rect.width)
			self.speedX=random.randint(-3,3)
			self.speedY=8

	def update(self):
		self.rect.x+=self.speedX
		self.rect.y+=self.speedY

		if (self.rect.y>dispHeight+self.rect.height or self.rect.y<(-self.rect.height) or 
			self.rect.x<(-self.rect.width) or self.rect.x>dispWidth+self.rect.width):
			if self.direction=="top":
				self.rect.x=random.randint(0,dispWidth-self.rect.width)
				self.rect.y=random.randint(-int(dispHeight/2),-self.rect.height)
				self.speedX=random.randint(-3,3)
				self.speedY=8
			if self.direction=="bottom":
				self.rect.x=random.randint(0,dispWidth-self.rect.width)
				self.rect.y=random.randint(-int(dispHeight/2),-self.rect.height)
				self.speedX=random.randint(-3,3)
				self.speedY=8
			if self.direction=="right":
				self.rect.y=random.randint(0,dispHeight-self.rect.height)
				self.rect.x=random.randint(self.rect.width+dispWidth,int(dispWidth*1.5))
				self.speedX=-8
				self.speedY=random.randint(-3,3)
			if self.direction=="left":
				self.rect.x=random.randint(0,dispHeight-self.rect.height)
				self.rect.y=random.randint(-int(dispWidth/2),-self.rect.width)
				self.speedX=random.randint(-3,3)
				self.speedY=8	
	
		
		
