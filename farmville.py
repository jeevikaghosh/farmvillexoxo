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




introLoopExit = introLoop()


if introLoopExit==1:
	
	characterLoopExit= characterLoop()

	if characterLoopExit== "f":

		startGameLoopExit=startGameLoop("f")

		# if startGameLoopExit=="bug":

		# 	pestGameLoopExit=pestGameLoop()

		# 	if pestGameLoopExit=="ruined":

		# 		startGameLoopExit=startGameLoop("f")


	else:		

		startGameLoopExit=startGameLoop("m")




pygame.quit()
sys.exit()