import pygame
import sys
import time 
import random
from button import Button
from farmgrid import tile
from loops import *
from globalvariables import *
from pestgame import *
import timer
from os import path 


#starts the games loops in order of progression
introLoopExit = introLoop()

characterLoopExit= characterLoop(introLoopExit)

startGameLoopExit=startGameLoop(characterLoopExit)

if startGameLoopExit=="Game Over":

	pygame.quit()
	sys.exit()


elif startGameLoopExit=="restart":

	introLoopExit = introLoop()

	characterLoopExit= characterLoop(introLoopExit)

	startGameLoopExit=startGameLoop(characterLoopExit)



pygame.quit()
sys.exit()