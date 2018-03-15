import pygame
import sys
import time 
import random
from button import Button
from farmgrid import tile
from loops import *
from globalvariables import *


pygame.display.set_caption("Farmville")

exitCode = intro_loop()


if exitCode==1:
	startGameLoop()



pygame.quit()
sys.exit()