import pygame
import sys
import time 
import random
from button import Button
from farmgrid import tile
from globalvariables import *
from pestgame import *



def intro_loop():
	running = True
	logoX=dispWidth/5
	startWidth = dispWidth/6
	startHeight = dispHeight/8
	startX=2*dispWidth/5
	StartY=4*dispHeight/5
	charButY=dispHeight/4
	charButWidth=dispWidth/3
	CharButHeight=dispHeight/2
	maleCharButX=dispWidth/12
	femCharButX=3*dispWidth/5-dispWidth/25
	margin=dispHeight/30
	femButClicked=False
	maleButClicked=False

	while running: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 0
				
			gameDisp.fill(white)

			maleCharButton= Button(blue,maleCharButX,charButY,charButWidth,CharButHeight,gameDisp)

			femCharButton=Button(pink,femCharButX,charButY,charButWidth,CharButHeight,gameDisp)

			startButton = Button(green,startX,StartY,startWidth,startHeight,gameDisp)
			startButton.addText("Start Game",black)

			mouse = pygame.mouse.get_pos()

			if startButton.x+startButton.width > mouse[0] > startButton.x and startButton.y+startButton.height > mouse[1] > startButton.y:
				highlightStartButton = Button(brightGreen,startX,StartY,startWidth,startHeight,gameDisp)
				highlightStartButton.addText("Start Game",black)

			if maleCharButton.x+maleCharButton.width > mouse[0] > maleCharButton.x and maleCharButton.y+maleCharButton.height > mouse[1] > maleCharButton.y:
				highlightmaleCharButton = Button(brightBlue,maleCharButX,charButY,charButWidth,CharButHeight,gameDisp)

			if femCharButton.x+femCharButton.width > mouse[0] > femCharButton.x and femCharButton.y+femCharButton.height > mouse[1] > femCharButton.y:
				highlightmaleCharButton = Button(brightPink,femCharButX,charButY,charButWidth,CharButHeight,gameDisp)
				
			if 	femCharButton.clicked():
				femButClicked=True
				character="f"

			if 	maleCharButton.clicked():
				maleButClicked=True
				character="m"

			if maleButClicked:
				highlightmaleCharButton = Button(brightBlue,maleCharButX,charButY,charButWidth,CharButHeight,gameDisp)

			if femButClicked:
				highlightmaleCharButton = Button(brightPink,femCharButX,charButY,charButWidth,CharButHeight,gameDisp)



			
			gameDisp.blit(scaledFarmgirl,(femCharButX,charButY))
			gameDisp.blit(scaledFarmboy,(maleCharButX,charButY+margin))
			gameDisp.blit(scaledLogo,(logoX,0))


			if startButton.clicked():
				return 1


			pygame.display.update()


def startGameLoop():
	running = True
	# self.currentImg = currentImg
	# img=pygame.image.load(self.currentImg)
	# scaleImage=pygame.transform.scale(img,(size,size))
	# self.surface= pygame.Surface((size,size))
	# self.surface.blit(scaleImage, (0,0))
	# self.screen=screen
	# self.screen.blit(self.surface,(self.x,self.y))
	# self.clickedTile=False
	cameraDir=None
	cameraX=0
	cameraY=0

	numOfTiles=5
	margin=int(dispWidth/5) 
	tileSize=int(dispWidth/6)

	gameDisp.fill(backgroundGreen)

	allGrassTiles = []

	allHighlightedTiles = []

	allFadedPloughTiles = []

	allPloughTiles = []

	allSeedTiles = []

	allCropTiles = []

	cropButtons= []

	cropButWidth = dispWidth/7
	cropButHeight = dispHeight/8
	cropButX=4.5*dispWidth/5
	cornY=dispHeight/5+dispHeight/20
	cabbageY=2*dispHeight/5+dispHeight/20
	tomatoY=3*dispHeight/5+dispHeight/20

	HouseX=dispWidth/3



	# scaleHouse=pygame.transform.scale(house,(houseSize,houseSize))
	# 
	# housesurface.blit(scaleHouse, (0,0))

	cornButton = Button(red,cropButX,cornY,cropButWidth,cropButHeight,gameDisp)
	
	cabbageButton = Button(red,cropButX,cabbageY,cropButWidth,cropButHeight,gameDisp)
	
	tomatoButton = Button(red,cropButX,tomatoY,cropButWidth,cropButHeight,gameDisp)
	

	cropButtons.append(cornButton)
	cropButtons.append(cabbageButton)
	cropButtons.append(tomatoButton)

	for i in range(margin,numOfTiles*tileSize,tileSize):
		for j in range(margin,numOfTiles*tileSize-tileSize,tileSize):
				newGrassTile = tile(tileSize, i+cameraX, j+cameraY, gameDisp, "grasstile.jpg")
				allGrassTiles.append(newGrassTile)


		
	gameDisp.blit(scaledHouse,(HouseX,0))
	gameDisp.blit(scaledTree2,(HouseX/10,3*dispHeight/5))
	gameDisp.blit(scaledTree1,(HouseX/15-dispHeight/20,4*dispHeight/5-dispHeight/10))
	gameDisp.blit(scaledbush,(HouseX,4*dispHeight/5+dispHeight/10))
	gameDisp.blit(scaledTree1,(HouseX/10,4*dispHeight/5))


	
	if character=="f":
		print("yes f")
		gameDisp.blit(scaledFarmgirl2,(0,tomatoY))
	if character=="m":
		gameDisp.blit(scaledFarmboy2,(0,tomatoY))
		print("yes m")


	while running: 
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running=False

				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_UP:
						cameraDir='n'
					elif event.key==pygame.K_DOWN:
						cameraDir='s'
					elif event.key==pygame.K_RIGHT:
						cameraDir='e'
					elif event.key==pygame.K_LEFT:
						cameraDir='w'
				elif event.type==pygame.KEYUP:
					cameraDir=None

			if cameraDir=='n':
				cameraY-=5
			elif cameraDir=='s':
				cameraY+=5
			elif cameraDir=='e':
				cameraX+=5
			elif cameraDir=='w':
				cameraX-=5


			mouse = pygame.mouse.get_pos()
			if cornButton.hover():
			# if cornButton.x+cornButton.width > mouse[0] > cornButton.x and cornButton.y+cornButton.height > mouse[1] > cornButton.y:
				highlightcornButton = Button(orangeRed,cropButX,cornY,cropButWidth,cropButHeight,gameDisp)
			else:
				cornButton=Button(red,cropButX,cornY,cropButWidth,cropButHeight,gameDisp)
			if cabbageButton.hover():
					highlightcornButton = Button(orangeRed,cropButX,cabbageY,cropButWidth,cropButHeight,gameDisp)
			else:
				cabbageButton=Button(red,cropButX,cabbageY,cropButWidth,cropButHeight,gameDisp)
			if tomatoButton.hover():
					highlightcornButton = Button(orangeRed,cropButX,tomatoY,cropButWidth,cropButHeight,gameDisp)
			else:
				tomatoButton=Button(red,cropButX,tomatoY,cropButWidth,cropButHeight,gameDisp)
			

			for cropButton in cropButtons:
				if cropButton.clicked():
					chosenCrop=cropButton
					print(chosenCrop)
					highlightButton=Button(orangeRed,cropButton.x,cropButton.y,cropButton.width,cropButton.height,gameDisp)


			if len(allGrassTiles)!=0:
				for singtile in allGrassTiles:
					# if not singtile.clickedTile:
					if singtile.clicked():
						time=pygame.time.get_ticks()
						allFadedPloughTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, "soilfaded.png", time))
						singtile.clickedTile=True
						allGrassTiles.remove(singtile)
						print (pygame.time.get_ticks())
						print(allGrassTiles)
						print("clicked tile at " + str(singtile.x) + "," + str(singtile.y)+"clicked" +str(singtile.clickedTile))
				
				
				
					if singtile.x+tileSize > mouse[0] > singtile.x and singtile.y+tileSize > mouse[1] > singtile.y:
						# print("laala")
						highlightSingtile = tile(tileSize, singtile.x, singtile.y, gameDisp, "grasstilefaded.jpg")
					else:
						unhighlightSingtile = tile(tileSize, singtile.x, singtile.y, gameDisp, "grasstile.jpg")
				# # if singtile.hover():
				# # 	# allHighlightedTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, "grasstilefaded.jpg"))

			
				# # 	print("hovered tile at " + str(singtile.x) + ", " + str(singtile.y))

			if len(allFadedPloughTiles)!=0:
				for singtile in allFadedPloughTiles:
					currentTime=pygame.time.get_ticks()
					# print("ct", currentTime, "st", singtile.startTime, "dif", currentTime-singtile.startTime )
					if (currentTime-singtile.startTime)>1000 and (currentTime-singtile.startTime)//1000%3==0:
						# print ("sxjsnj")
						allPloughTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, "soil2.png", time))
						singtile.clickedTile=True
						allFadedPloughTiles.remove(singtile)

			if len(allPloughTiles)!=0:
				for singtile in allPloughTiles:
					# currentTime=pygame.time.get_ticks()
				# print("ct", currentTime, "st", singtile.startTime, "dif", currentTime-singtile.startTime )
					# if (currentTime-singtile.startTime)>1000 and (currentTime-singtile.startTime)//1000%3==0:
					# print ("sxjsnj")

					if singtile.clicked():
						print("clicked")
						time=pygame.time.get_ticks()
						if chosenCrop.y==cornY:
							allSeedTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, "cornseeds.jpg", time))
							allPloughTiles.remove(singtile)
						if chosenCrop.y==tomatoY:
							allSeedTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, "tomatoseeds.jpg", time))
							allPloughTiles.remove(singtile)
						if chosenCrop.y==cabbageY:
							allSeedTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, "cabbageseeds.jpg", time))
							allPloughTiles.remove(singtile)
						

			if len(allSeedTiles)!=0:
				for singtile in allSeedTiles:
					currentTime=pygame.time.get_ticks()
				# print("ct", currentTime, "st", singtile.startTime, "dif", currentTime-singtile.startTime )
					# if (currentTime-singtile.startTime)>1000 and (currentTime-singtile.startTime)//1000%3==0:
					# print ("sxjsnj")

					if (currentTime-singtile.startTime)>1000 and (currentTime-singtile.startTime)//1000%3==0:
						
						
						if singtile.currentImg=="cornseeds.jpg":
							allCropTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, "cornfield.jpg", time))
							allSeedTiles.remove(singtile)
						if singtile.currentImg=="tomatoseeds.jpg":
							allCropTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, "tomatofield.jpg", time))
							allSeedTiles.remove(singtile)
						if singtile.currentImg=="cabbageseeds.jpg":
							allCropTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, "cabbagefield.jpg", time))
							allSeedTiles.remove(singtile)
						

						
			gameDisp.blit(scaledcorn,(cropButX,cornY))
			gameDisp.blit(scaledcabbage,(cropButX,cabbageY))
			gameDisp.blit(scaledtomato,(cropButX,tomatoY))
			pygame.display.update()



def pestGameLoop():

	running=True 
	bugSprites=pygame.sprite.Group()
	playerSprite=pygame.sprite.GroupSingle()
	# allSprites=pygame.sprite.Group()
	spray = Spray()
	playerSprite.add(spray)
	# allSprites.add(spray)
	myfont = pygame.font.SysFont("monospace", 15)
	numOfHits=0
	counter=15
	print(bugSprites)
	pygame.time.set_timer(pygame.USEREVENT, 1000)
	for i in range(4):
		topbug=Bugs(scaledBug, "top")
		bugSprites.add(topbug)
		# allSprites.add(topbug)
		bottombug=Bugs(scaledBug, "bottom")
		bugSprites.add(bottombug)
		# allSprites.add(bottombug)
		leftbug=Bugs(scaledBug, "left")
		bugSprites.add(leftbug)
		# allSprites.add(leftbug)
		rightbug=Bugs(scaledBug, "right")
		bugSprites.add(rightbug)
		# allSprites.add(rightbug)

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running= False
			if event.type==pygame.USEREVENT:
				counter-=1
				if counter<0:
					counter=0


		hits = pygame.sprite.spritecollide(spray, bugSprites, True)
		
		for hit in hits:
			numOfHits+=1
			print(numOfHits)
		time=pygame.time.get_ticks()
		#update
		# allSprites.update()
		playerSprite.update()
		bugSprites.update()
		#draw
		gameDisp.fill(green)
		playerSprite.draw(gameDisp)
		bugSprites.draw(gameDisp)
		# allSprites.draw(gameDisp)
		for bug in bugSprites:
			
			if ((spray.rect.centerx-bug.rect.centerx)**2+(spray.rect.centery-bug.rect.centery)**2)**0.5<200:

				print(((spray.rect.centerx-bug.rect.centerx)**2+(spray.rect.centery-bug.rect.centery)**2)**0.5)

				if bug.direction=="top":
					print("top")
					bug.speedY=-8
				if bug.direction=="bottom":
					print("bottom")
					bug.speedY=+8
				if bug.direction=="left":
					print("left")
					bug.speedY=-8
				if bug.direction=="right":
					print("right")
					bug.speedY=+8


		# 
		# counter=counter-(time-//1000

		if numOfHits==16:
			winText= myfont.render("Crops Saved!", 6, yellow)
			gameDisp.blit(winText, (200, 200))


		elif counter==0 and numOfHits!=16:
			loseText= myfont.render("Crops Failed!", 6, yellow)
			gameDisp.blit(loseText, (200, 200))
		


		# render text
		timerText = myfont.render("Timer: %d seconds" % (counter), 6, yellow)
		gameDisp.blit(timerText, (100, 100))
		#flip display
		pygame.display.flip()

		# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error










