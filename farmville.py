import pygame
import sys
import time 
import random
from button import Button
from farmgrid import tile
from loops import *
from globalvariables import *
from pestgame import *





exitCode = intro_loop()


if exitCode==1:
	# pestGameLoop()
	startGameLoop()



pygame.quit()
sys.exit()