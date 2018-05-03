import pygame
import sys
import time 
import random
from globalvariables import *


class Button:

	def __init__(self,color,x,y,w,h,screen):
		
		self.color = color
		self.x = x
		self.y = y
		self.height = h
		self.width = w
		self.screen = screen
		pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.width,self.height))

	def __repr__(self):
		return ("x= %d y= %d color=%s" % (self.x, self.y, self.color))

	def addText(self,text,color):
		self.font = pygame.font.SysFont('Arial', 25)
		locx = (self.x+(self.width/2))
		locy = (self.y+(self.height/2))
		textSurface = self.font.render(text, True, color)

		textRect = textSurface.get_rect()
		textRect.center = (locx, locy)
		self.screen.blit(textSurface,textRect)

	def hover(self):
		mouse = pygame.mouse.get_pos()
		return self.x+self.width > mouse[0] > self.x and self.y+self.height > mouse[1] > self.y
	
	def clicked(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		return self.x+self.width > mouse[0] > self.x and self.y+self.height > mouse[1] > self.y and click[0]==1