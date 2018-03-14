import pygame
import time 
import random

pygame.init()

dispWidth=650
dispHeight=450

white=(255,255,255)
gameDisp=pygame.display.set_mode((dispWidth,dispHeight))

pygame.display.set_caption("Farmville")
clock=pygame.time.Clock()

crashed= False

while not crashed: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				crashed=True
		
		gameDisp.fill(white)

		pygame.display.update()
		clock.tick(60)

pygame.quit()






