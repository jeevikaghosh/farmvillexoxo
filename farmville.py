import pygame
import sys
import time 
import random

pygame.init()
pygame.font.init()
dispWidth=650
dispHeight=450

white=(255,255,255)
brightGreen=(0,255,0)
green = (50,205,50)
black = (0,0,0)

gameDisp=pygame.display.set_mode((dispWidth,dispHeight))
pygame.display.set_caption("Farmville")


def game_loop():
	print("game_loop started")

# def text_objects(text, font):
#     textSurface = font.render(text, True, black)
#     return textSurface, textSurface.get_rect()


# def button(msg,x,y,w,h,ic,ac,action=None):
#     mouse = pygame.mouse.get_pos()
#     click = pygame.mouse.get_pressed()
#     print(click)
#     if x+w > mouse[0] > x and y+h > mouse[1] > y:
#         pygame.draw.rect(gameDisp, ac,(x,y,w,h))

#         if click[0] == 1 and action != None:
#             action()         
#     else:
#         pygame.draw.rect(gameDisp, ic,(x,y,w,h))

#     # smallText = pygame.font.SysFont("comicsansms",20)
#     # textSurf, textRect = text_objects(msg, smallText)
#     # textRect.center = ( (x+(w/2)), (y+(h/2)) )
#     # gameDisp.blit(textSurf, textRect)


class Button:

	def __init__(self,color,x,y,h,w,screen):
		self.color = color
		self.x = x
		self.y = y
		self.height = h
		self.width = w
		self.screen = screen
		pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.width,self.height))

	def addText(self,text,color):
		self.font = pygame.font.SysFont('Arial', 25)
		locx = (self.x+(self.width/2))
		locy = (self.y+(self.height/2))
		textSurface = self.font.render(text, True, color)

		textRect = textSurface.get_rect()
		textRect.center = (locx, locy)
		self.screen.blit(textSurface,textRect)

	def clicked(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		return self.x+self.width > mouse[0] > self.x and self.y+self.height > mouse[1] > self.y and click[0]==1


running = True

startGame = False

while running: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
		gameDisp.fill(white)

		startButton = Button(green,100,100,100,100,gameDisp)


		startButton.addText("Start>",black)

		if startButton.clicked():
			running = False
			startGame = True


		pygame.display.update()


print("escaped running loop")


while startGame:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			startGame = False

		gameDisp.fill(white)

		newText = pygame.font.SysFont('Arial', 50).render("Welcome in game", True, black)

		gameDisp.blit(newText, (100,100))

		pygame.display.update()



pygame.quit()
sys.exit()