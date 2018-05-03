import pygame
import sys
import time 
import random
import math
from button import Button
from farmgrid import tile
from globalvariables import *
from pestgame import *
from os import path 
from friendsFarm import *



def introLoop():

	running = True

	
	#starting the sound
	soundOn=True
	theme.play()
	theme.set_volume(0.1)
	
	
	username=""

	while running: 
		
		for event in pygame.event.get():
			if event.type== pygame.QUIT:
				return 0
			#user input for username
			if event.type==pygame.KEYDOWN:
				if event.key in keyDict:
				
					username+=keyDict[event.key]
					
				if event.key==8:
					
					username=username[:-1]

		#creating the background
		gameDisp.fill(white)
		gameDisp.blit(scaledfarmtheme,(0,0))

		#creating the sound button
		soundButton = Button(green, cropButX, 5*dispHeight/6, cropButWidth,cropButHeight, gameDisp)
		if soundButton.clicked():
				
				if not soundOn:
					theme.play()
					soundOn=True
				elif soundOn:
					soundOn=False
					theme.stop()

		if soundButton.hover():
			highlightsaveButton = Button(brightGreen,cropButX, 5*dispHeight/6, cropButWidth,cropButHeight,gameDisp)
		else:
			soundButton=Button(green,cropButX, 5*dispHeight/6, cropButWidth,cropButHeight,gameDisp)

		if soundOn:
			gameDisp.blit(scaledSoundOn,(cropButX, 5*dispHeight/6))
		if not soundOn:
			gameDisp.blit(scaledSoundOff,(cropButX, 5*dispHeight/6))

		#displaying the texts on the screen
		welcomeText = myfont.render("Welcome to" , 6, black)
		gameDisp.blit(welcomeText, (2*dispWidth/5-50, 20))
		
		usernameText = myfont.render("Type your username to begin:" , 6, black)
		gameDisp.blit(usernameText, (startWidth, usernameY))

		usernameButton = Button(green,userButX,userButY,userWidth,userHeight,gameDisp)
		startButton = Button(green,startX,StartY,startWidth,startHeight,gameDisp)
		startButton.addText("Start New Game",black)

		mouse = pygame.mouse.get_pos()

		#creating the start button
		if startButton.hover():
			highlightStartButton= Button(brightGreen,startX,StartY,startWidth,startHeight,gameDisp)
			highlightStartButton.addText("Start New Game", black)

		if usernameButton.hover():
			highlightUsernameButton= Button(brightGreen,userButX,userButY,userWidth,userHeight,gameDisp)
		
		gameDisp.blit(scaledLogo,(logoX,logoY))

		usernameText = myfont.render(username , 6, black)
		gameDisp.blit(usernameText, (userButX+20, userButY+10))

		#checking if the file exits in the directory to load it
		if len(username)!=0 and path.exists("%s.txt"%username):
			loadButton= Button(red, userButX+100, userButY+70,startWidth,startHeight,gameDisp)
			loadButton.addText("Load Prev Game", black)
			if loadButton.hover():
				highlightLoadButton= Button(orangeRed,userButX+100, userButY+70,startWidth,startHeight,gameDisp)
				highlightLoadButton.addText("Load Prev Game", black)

			#if the load button clicked then opening the file
			if loadButton.clicked():
				theme.stop()
				try:
					with open("%s.txt" %(username)) as file:
						mylist = [line.rstrip('\n') for line in file]
						character=mylist[0]
						file.close()
					
					startGameLoop((character,username), True)
				except:
					invalidText = myfont.render("!!!Invalid Username!!!", 6, red)
					gameDisp.blit(invalidText, (userButX+20, userButY+70))

				return (username)

		#if start button clicked, a new file is created with the username 	
		if startButton.clicked() and len(username)!=0:
			f= open("%s.txt"%username,"w+")
			f.close()
			return (username)

		pygame.display.update()


def characterLoop(username):
	
	running = True

	#setting variables for clicked buttons 
	femButClicked=False
	maleButClicked=False
	soundOn=True
	
	#if the character is already saved in the file then the character loop is ended
	try:
		with open("%s.txt" %(username)) as file:
			mylist = [line.rstrip('\n') for line in file]
			character=mylist[0]
			file.close()
		theme.stop()
		running=False
	except:
		running=True

		
	
	while running: 

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 0

		#making the background, texts and buttons
		gameDisp.fill(white)
		gameDisp.blit(scaledfarmtheme,(0,0))

		characterText = myfont.render("Choose your Character:" , 6, black)
		gameDisp.blit(characterText, (logoX, startHeight))

		maleCharButton= Button(blue,maleCharButX,charButY,charButWidth,CharButHeight,gameDisp)

		femCharButton=Button(pink,femCharButX,charButY,charButWidth,CharButHeight,gameDisp)

		soundButton = Button(green, cropButX, 5*dispHeight/6, cropButWidth,cropButHeight, gameDisp)

		#manipulating the sound
		if soundButton.clicked():
				
				if not soundOn:
					theme.play()
					soundOn=True
				elif soundOn:
					soundOn=False
					theme.stop()

		if soundButton.hover():
			highlightsaveButton = Button(brightGreen,cropButX, 5*dispHeight/6, cropButWidth,cropButHeight,gameDisp)
		else:
			soundButton=Button(green,cropButX, 5*dispHeight/6, cropButWidth,cropButHeight,gameDisp)

		if soundOn:
			gameDisp.blit(scaledSoundOn,(cropButX, 5*dispHeight/6))
			
		if not soundOn:
			gameDisp.blit(scaledSoundOff,(cropButX, 5*dispHeight/6))

		#getting the mouse position to check the hover
		mouse = pygame.mouse.get_pos()

		if maleCharButton.hover():
			highlightmaleCharButton = Button(brightBlue,maleCharButX,charButY,charButWidth,CharButHeight,gameDisp)

		if femCharButton.hover():
			highlightmaleCharButton = Button(brightPink,femCharButX,charButY,charButWidth,CharButHeight,gameDisp)
			
		
		#checking if the female or male button is clicked and changing the variables accordingly
		if 	femCharButton.clicked():
			femButClicked=True
			theme.stop()
			character="f"

		if 	maleCharButton.clicked():
			maleButClicked=True
			theme.stop()
			character="m"

		if maleButClicked:
			highlightmaleCharButton = Button(brightBlue,maleCharButX,charButY,charButWidth,CharButHeight,gameDisp)
			theme.stop()
			return ((character, username))
		if femButClicked:
			highlightmaleCharButton = Button(brightPink,femCharButX,charButY,charButWidth,CharButHeight,gameDisp)
			theme.stop()
			return ((character, username))

		#drawing the characters on the screen 
		gameDisp.blit(scaledFarmgirl,(femCharButX,charButY))
		gameDisp.blit(scaledFarmboy,(maleCharButX,charButY+margin))
	

		pygame.display.update()



def startGameLoop(specs, load=False):
	character, username= specs
	
	running = True

	#defining some variables required 
	cameraDir=None
	cameraX=0
	cameraY=0

	numOfTiles=5
	margin=int(dispWidth/5) 
	tileSize=int(dispWidth/6)

	money=100
	upgradeHouse=False
	upgradeFarmhouse=False
	buyTree=False
	buyTree2=False
	buyBush=False
	buyBush2=False

	coinsForTree=None
	coinsForBush=None
	coinsForHouse=None

	soundOn=True
	background.play()
	
	
	written=[]

	gameDisp.fill(backgroundGreen)

	allGrassTiles = []

	allHighlightedTiles = []

	allFadedPloughTiles = []

	allPloughTiles = []

	allSeedTiles = []

	allCropTiles = []

	allRottenTiles = []

	allBugTiles = []

	cropButtons= []

	savedFriends={1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

	#making the crop button list

	cornButton = Button(red,cropButX,cornY,cropButWidth,cropButHeight,gameDisp)
	
	cabbageButton = Button(red,cropButX,cabbageY,cropButWidth,cropButHeight,gameDisp)
	
	tomatoButton = Button(red,cropButX,tomatoY,cropButWidth,cropButHeight,gameDisp)

	cropButtons.append(cornButton)
	cropButtons.append(cabbageButton)
	cropButtons.append(tomatoButton)

	#making the grasstiles list

	for i in range(margin,numOfTiles*tileSize,tileSize):
		for j in range(margin,numOfTiles*tileSize-tileSize,tileSize):
				newGrassTile = tile(tileSize, i+cameraX, j+cameraY, gameDisp, path.join(imageDir,"grasstile.jpg"))
				allGrassTiles.append(newGrassTile)

	#if the load variable is pressed then the saved farm is loaded by reading into the file
	if load:
		with open("%s.txt"%username) as file:
			textlist = [line.rstrip('\n') for line in file]
			

			money = int(textlist[1])
			if textlist[2]=="1":
				buyTree=True
			if textlist[2]=="2":
				buyTree=True
				buyTree2=True
			if textlist[3]=="1":
				buyBush=True
			if textlist[3]=="2":
				buyBush=True
				buyBush2=True
			if textlist[4]=="1":
				upgradeHouse=True
			if textlist[4]=="2":
				upgradeHouse=True
				upgradeFarmhouse=True


			loadGrassTiles=[]
			loadPloughTiles=[]
			for i in range(margin,numOfTiles*tileSize,tileSize):
				for j in range(margin,numOfTiles*tileSize-tileSize,tileSize):
					
					if ("x= %d y= %d" % (i , j)) in textlist[5]:
						newGrassTile = tile(tileSize, i+cameraX, j+cameraY, gameDisp, path.join(imageDir,"grasstile.jpg"))
						loadGrassTiles.append(newGrassTile)

			for i in range(margin,numOfTiles*tileSize,tileSize):
				for j in range(margin,numOfTiles*tileSize-tileSize,tileSize):
					
					if ("x= %d y= %d" % (i , j)) in textlist[6]:
						newPloughTile = tile(tileSize, i+cameraX, j+cameraY, gameDisp, path.join(imageDir,"soil2.png"))
						loadPloughTiles.append(newPloughTile)
			
			allPloughTiles=loadPloughTiles
			allGrassTiles=loadGrassTiles

			for i in range(1, 7):
				if (str(i)+": 0") not in textlist[7]:
					
					index1=textlist[7].find(str(i))+textlist[7][textlist[7].find(str(i)):].find("'")
					
					index2=index1+1+textlist[7][(index1+1):].find("'")

					savedFriends[i]=textlist[7][index1+1:index2]
     

	while running: 

			#a new screen is drawn to prevent image lagging
			screenButton=Button(backgroundGreen,0,0,dispWidth,dispHeight,gameDisp)

			#new tiles are drawn from all the tile lists 
			if len(allGrassTiles)!=0:
				for singtile in allGrassTiles: 
					singtile.draw()

			if len(allHighlightedTiles)!=0:
				for singtile in allHighlightedTiles: 
					singtile.draw()

			if len(allPloughTiles)!=0:
				for singtile in allPloughTiles: 
					singtile.draw()

			if len(allFadedPloughTiles)!=0:
				for singtile in allFadedPloughTiles: 
					singtile.draw()

			
			if len(allSeedTiles)!=0:
				for singtile in allSeedTiles: 
					singtile.draw()

			if len(allCropTiles)!=0:
				for singtile in allCropTiles: 
					singtile.draw()

			if len(allRottenTiles)!=0:
				for singtile in allRottenTiles: 
					singtile.draw()

			if len(allBugTiles)!=0:
				for singtile in allBugTiles: 
					singtile.draw()

			#the buttons for various tasks are created with their texts
			saveButton = Button(blue, saveButX, saveButY, 2*cropButWidth/3,cropButHeight, gameDisp)
			visitButton = Button(blue, saveButX+2*cropButWidth/3+30, saveButY, 2*cropButWidth/3,cropButHeight, gameDisp)
			soundButton = Button(backgroundGreen, cropButX, 5*dispHeight/6, cropButWidth,cropButHeight, gameDisp)
			saveButton.addText("Save", white)
			visitButton.addText("Visit", white)
			houseButton = Button(backgroundGreen,HouseX,0,houseSize*2,houseSize,gameDisp)
			treeButton = Button(backgroundGreen,0,2*dispHeight/3-50,houseSize,houseSize,gameDisp)
			bushButton = Button(backgroundGreen,HouseX,7*dispHeight/8,houseSize,houseSize,gameDisp)
			farmerButton=Button(backgroundGreen,0,dispHeight/3,houseSize,houseSize-60,gameDisp)

			
			mouse = pygame.mouse.get_pos()

			#keeping track of what utilities can be bought with certain number of coins
			if money>=100:
				coinsForHouse=True
			elif money<100:
				coinsForHouse=False
			if money>=50:
				coinsForTree=True
			elif money<50:
				coinsForTree=False
			if money>=30:
				coinsForBush=True
			elif money<30:
				coinsForBush=False
			#if the money falls below 0 then the game is over
			if money<=0:
				gameoverLoopExit=gameOverLoop()
				return gameoverLoopExit
				running=False
			
			#buying a new house
			if houseButton.clicked():
				if money>=100:
					if upgradeHouse:
						upgradeFarmhouse=True
					upgradeHouse=True
					
					money-=100
				else:
					noMoneyText = myfont2.render("Not enough coins", 6, red)
					gameDisp.blit(noMoneyText, (HouseX*2,0))

			#buying a new tree
			if treeButton.clicked():
				if money>=50:
					if buyTree:
						buyTree2=True
					buyTree=True
					
					money-=50
				else:
					noMoneyText = myfont2.render("Not enough coins", 6, red)
					gameDisp.blit(noMoneyText, (HouseX/15,dispHeight/2+20))

			#buying a new bush
			if bushButton.clicked():
				if money>=30:
					if buyBush:
						buyBush2=True
					buyBush=True
					
					money-=30

				else:
					noMoneyText = myfont2.render("Not enough coins", 6, red)
					gameDisp.blit(noMoneyText, (HouseX/2+20,dispHeight-50))

			
			#drawing the upgrade texts for the houses, trees and bushes 
			if houseButton.hover():
				if (not upgradeHouse or not upgradeFarmhouse) and coinsForHouse:
					upgradeText = myfont2.render("Upgrade House for 100 coins", 6, black)
					gameDisp.blit(upgradeText, (HouseX*2,0))
			else:
				pygame.draw.rect(gameDisp,backgroundGreen,(HouseX*2,0,400,30))


			if bushButton.hover():
				if (not buyBush or not buyBush2) and coinsForBush:
					upgradeText = myfont2.render("Buy another Bush", 6, black)
					upgradeText2 = myfont2.render("for 30 coins", 6, black)
					gameDisp.blit(upgradeText, (HouseX/2+20,dispHeight-50))
					gameDisp.blit(upgradeText2, (HouseX/2+20,dispHeight-30))
				
			else:
				pygame.draw.rect(gameDisp,backgroundGreen,(HouseX/2+20,dispHeight-50,120,300))

			if treeButton.hover():
				if (not buyTree or not buyTree2) and coinsForTree:
					upgradeText = myfont2.render("Buy another Tree", 6, black)
					upgradeText2 = myfont2.render("for 50 coins", 6, black)
					gameDisp.blit(upgradeText, (HouseX/15,dispHeight/2+20))
					gameDisp.blit(upgradeText2, (HouseX/15,4*dispHeight/7))
			else:
				pygame.draw.rect(gameDisp,backgroundGreen,(HouseX/15,dispHeight/2,130,300))

		
			#manipulating the sound 
			if soundButton.clicked():
					if not soundOn:
						background.play()
						soundOn=True
					elif soundOn:
						soundOn=False
						background.stop()

			#saving the game with variables 
			if saveButton.clicked():
				numOfTrees=0
				numOfBushes=0
				houseUpgrades=0
				if buyTree and not buyTree2:
					numOfTrees=1
				if buyTree and buyTree2:
					numOfTrees=2

				if buyBush and not buyBush2:
					numOfBushes=1
				if buyBush and buyBush2:
					numOfBushes=2

				if upgradeHouse and not upgradeFarmhouse:
					houseUpgrades=1
				if upgradeHouse and upgradeFarmhouse:
					houseUpgrades=2

				written=[character, str(money), str(numOfTrees),  str(numOfBushes), str(houseUpgrades), str(allGrassTiles), str(allPloughTiles), str(savedFriends)]
				
				newFile = ""
				for elem in written:
					newFile += (elem + "\n")

				with open("%s.txt" %(username), 'w') as file:
					file.write(newFile)
					file.close()

			#opening the visit farm feature
			if visitButton.clicked():

				friendFarmLoopExit=friendsFarmIntro(savedFriends)
				savedFriends= friendFarmLoopExit
				background.stop()

			#highlighting the buttons if the mouse hovers over it
			if saveButton.hover():
				highlightsaveButton = Button(brightBlue,saveButX, saveButY, 2*cropButWidth/3,cropButHeight,gameDisp)
				highlightsaveButton.addText("Save", white)
			else:
				saveButton=Button(blue,saveButX, saveButY, 2*cropButWidth/3,cropButHeight,gameDisp)
				saveButton.addText("Save", white)

			if visitButton.hover():
				highlightvisitButton = Button(brightBlue,saveButX+2*cropButWidth/3+30, saveButY, 2*cropButWidth/3,cropButHeight,gameDisp)
				highlightvisitButton.addText("Visit", white)
			else:
				visitButton=Button(blue,saveButX+2*cropButWidth/3+30, saveButY, 2*cropButWidth/3,cropButHeight,gameDisp)
				visitButton.addText("Visit", white)
			
			if soundButton.hover():
				highlightsaveButton = Button(green,cropButX, 5*dispHeight/6, cropButWidth,cropButHeight,gameDisp)
			else:
				soundButton=Button(backgroundGreen,cropButX, 5*dispHeight/6, cropButWidth,cropButHeight,gameDisp)

			if cornButton.hover():
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
			
			#choosing the crop to plant
			for cropButton in cropButtons:
				if cropButton.clicked():
					chosenCrop=cropButton
					print(chosenCrop)
					highlightButton=Button(orangeRed,cropButton.x,cropButton.y,cropButton.width,cropButton.height,gameDisp)


			#if there is a bugtile 
			if len(allBugTiles)!=0:
				for singtile in allBugTiles:
					
					#starting the bug game loop
					if singtile.clicked():
						
						pestGameLoopExit=pestGameLoop()

						#if you lose the bug game then the rotten tiles are replaced with the bug tiles
						if pestGameLoopExit=="failed":
							
							if singtile.currentImg==path.join(imageDir,"bugscornfield.png"):
								allRottenTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"rottencornfield.png"), time))
								allBugTiles.remove(singtile)
								print("rotcorn")
							if singtile.currentImg==path.join(imageDir,"bugstomatofield.png"):
								allRottenTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"rottentomatofield.png"), time))
								allBugTiles.remove(singtile)
								print("rottom")
							if singtile.currentImg==path.join(imageDir,"bugscabbagefield.png"):
								allRottenTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"rottencabbagefield.png"), time))
								allBugTiles.remove(singtile)
								print("rotcab")
						#if you win then the bug tiles are replaced with crop tiles
						if pestGameLoopExit=="saved":
							if singtile.currentImg==path.join(imageDir,"bugscornfield.png"):
								allCropTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"cornfield.jpg"), time))
								allBugTiles.remove(singtile)
								print("corn")
							if singtile.currentImg==path.join(imageDir,"bugstomatofield.png"):
								allCropTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"tomatofield.jpg"), time))
								allBugTiles.remove(singtile)
								print("tom")
							if singtile.currentImg==path.join(imageDir,"bugscabbagefield.png"):
								print("cab")
								allCropTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"cabbagefield.jpg"), time))
								allBugTiles.remove(singtile)

			# creating the ploughed tiles if the grass tile is clicked
			if len(allFadedPloughTiles)!=0:
				for singtile in allFadedPloughTiles:
					currentTime=pygame.time.get_ticks()
					
					if (currentTime-singtile.startTime)>1000 and (currentTime-singtile.startTime)//1000%3==0:
						
						allPloughTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"soil2.png"), time))
						singtile.clickedTile=True
						allFadedPloughTiles.remove(singtile)

			# creating the faded plough tiles if the grass tile is clicked
			if len(allGrassTiles)!=0:
				for singtile in allGrassTiles:
					
					if singtile.clicked():
						time=pygame.time.get_ticks()
						allFadedPloughTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"soilfaded.png"), time))
						singtile.clickedTile=True
						allGrassTiles.remove(singtile)
						money-=20
				
				
					if singtile.hover():
						allHighlightedTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"grasstilefaded.jpg")))
						
					elif not singtile.hover():
						singtile.draw()
						if len(allHighlightedTiles)>5:
							allHighlightedTiles=[]

			
			#planting the crops on the selected patch 
			if len(allPloughTiles)!=0:
				for singtile in allPloughTiles:

					if singtile.clicked():
						print("clicked")
						time=pygame.time.get_ticks()
						try:
							if chosenCrop.y==cornY:
								allSeedTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"cornseeds.jpg"), time))
								money-=10
								allPloughTiles.remove(singtile)
							if chosenCrop.y==tomatoY:
								allSeedTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"tomatoseeds.jpg"), time))
								money-=15
								allPloughTiles.remove(singtile)
							if chosenCrop.y==cabbageY:
								allSeedTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"cabbageseeds.jpg"), time))
								money-=20
								allPloughTiles.remove(singtile)
						except:
							noCropText = myfont2.render("No crop Chosen!" , 6, red)
							gameDisp.blit(noCropText, (cropButX-50,cornY-30))

						
			#when you stat
			if len(allSeedTiles)!=0:
				for singtile in allSeedTiles:
					currentTime=pygame.time.get_ticks()
				
					centerX  = singtile.x+int(singtile.size/2)
					centerY = singtile.y+int(singtile.size/2)
					radius = int(singtile.size/4)

					if (currentTime-singtile.startTime)>1000: 
						pygame.draw.circle(gameDisp, white, (centerX, centerY),radius)
						
					if (currentTime-singtile.startTime)>1000 and singtile.currentImg==path.join(imageDir,"cornseeds.jpg"): 	
						
						angle=int(((currentTime-singtile.startTime)//1000)/cornTime*360)
						points = [(centerX, centerY)]
						#gets the points on arc
						for i in range(-90,angle-90):
							x = centerX + int(radius*math.cos(i*math.pi/180))
							y = centerY + int(radius*math.sin(i*math.pi/180))
							points.append((x, y))
							
						points.append((centerX, centerY))
						
						#draws the slice
						if len(points) > 2:
							pygame.draw.polygon(gameDisp, green, points)

					if (currentTime-singtile.startTime)>1000 and singtile.currentImg==path.join(imageDir,"tomatoseeds.jpg"): 	
						
						angle=int(((currentTime-singtile.startTime)//1000)/tomatoTime*360)
						points = [(centerX, centerY)]
						
						#gets the points on arc
						for i in range(-90,angle-90):
							x = centerX + int(radius*math.cos(i*math.pi/180))
							y = centerY+int(radius*math.sin(i*math.pi/180))
							points.append((x, y))
							
						points.append((centerX, centerY))
						
						#draws the slice
						if len(points) > 2:
							pygame.draw.polygon(gameDisp, green, points)

					if (currentTime-singtile.startTime)>1000 and singtile.currentImg==path.join(imageDir,"cabbageseeds.jpg"): 	
						
						angle=int(((currentTime-singtile.startTime)//1000)/cabbageTime*360)
						points = [(centerX, centerY)]
						
						#gets the points on arc
						for i in range(-90,angle-90):
							x = centerX + int(radius*math.cos(i*math.pi/180))
							y = centerY+int(radius*math.sin(i*math.pi/180))
							points.append((x, y))
							
						points.append((centerX, centerY))
						
						#draws the slice
						if len(points) > 2:
							pygame.draw.polygon(gameDisp, green, points)


					#removes the timer when the time to harvest is reached 
					if (currentTime-singtile.startTime)>10000 and (currentTime-singtile.startTime)//1000%cornTime==0:
						
						if singtile.currentImg==path.join(imageDir,"cornseeds.jpg"):
							allCropTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"cornfield.jpg"), time))
							allSeedTiles.remove(singtile)

					if (currentTime-singtile.startTime)>10000 and (currentTime-singtile.startTime)//1000%tomatoTime==0:

						if singtile.currentImg==path.join(imageDir,"tomatoseeds.jpg"):
							allCropTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"tomatofield.jpg"), time))
							allSeedTiles.remove(singtile)

					if (currentTime-singtile.startTime)>10000 and (currentTime-singtile.startTime)//1000%cabbageTime==0:
						
						if singtile.currentImg==path.join(imageDir,"cabbageseeds.jpg"):
							allCropTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"cabbagefield.jpg"), time))
							allSeedTiles.remove(singtile)
				
			#when the crop is clicked the money is added
			if len(allCropTiles)!=0:
				for singtile in allCropTiles:

					if singtile.clicked():
						time=pygame.time.get_ticks()

						if singtile.currentImg==path.join(imageDir,"cornfield.jpg") and not singtile.bugs:
							money+=30
						if singtile.currentImg==path.join(imageDir,"tomatofield.jpg")and not singtile.bugs:
							money+=45
						if singtile.currentImg==path.join(imageDir,"cabbagefield.jpg")and not singtile.bugs:
							money+=60
						allFadedPloughTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"soilfaded.png"), time))
						allCropTiles.remove(singtile)

			
			#if the crop tile is clicked
			if len(allCropTiles)!=0:
				for singtile in allCropTiles:
					currentTime=pygame.time.get_ticks()
				
					#randomly generated bugs
					randInt=random.randint(0,100)
					if randInt==5:
						singtile.bugs=True
						if singtile.currentImg==path.join(imageDir,"cornfield.jpg"):
							allBugTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"bugscornfield.png"), time))
							allCropTiles.remove(singtile)
						if singtile.currentImg==path.join(imageDir,"tomatofield.jpg"):
							allBugTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"bugstomatofield.png"), time))
							allCropTiles.remove(singtile)
						if singtile.currentImg==path.join(imageDir,"cabbagefield.jpg"):
							allBugTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"bugscabbagefield.png"), time))
							allCropTiles.remove(singtile)


					#if the crop is not harvested within a time period then the crop rots
					elif (currentTime-singtile.startTime)>1000 and (currentTime-singtile.startTime)//1000%30==0 and not singtile.bugs:
						
						
						if singtile.currentImg==path.join(imageDir,"cornfield.jpg"):
							allRottenTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"rottencornfield.png"), time))
							allCropTiles.remove(singtile)
						if singtile.currentImg==path.join(imageDir,"tomatofield.jpg"):
							allRottenTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"rottentomatofield.png"), time))
							allCropTiles.remove(singtile)
						if singtile.currentImg==path.join(imageDir,"cabbagefield.jpg"):
							allRottenTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"rottencabbagefield.png"), time))
							allCropTiles.remove(singtile)


			#removing the rotten patch of land
			if len(allRottenTiles)!=0:
				for singtile in allRottenTiles:

					if singtile.clicked():
						time=pygame.time.get_ticks()
						money-=5
					
						allFadedPloughTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"soilfaded.png"), time))
						allRottenTiles.remove(singtile)
			#drawing the level house that you have bought
			if not upgradeHouse:
				gameDisp.blit(scaledHouse2,(HouseX,0))
			
			if upgradeHouse and not upgradeFarmhouse:
				gameDisp.blit(scaledHouse,(HouseX,0))
			
			if  upgradeFarmhouse:
				gameDisp.blit(scaledHouse3,(HouseX,0))
		

			#drawing the trees you have bought
			gameDisp.blit(scaledTree2,(HouseX/10,3*dispHeight/5))
			if buyTree:
				gameDisp.blit(scaledTree1,(HouseX/15-dispHeight/20,4*dispHeight/5-dispHeight/10))
			if buyTree2:
				gameDisp.blit(scaledTree1,(HouseX/10,4*dispHeight/5))
			#drawing the bushes you have bought
			if buyBush:
				gameDisp.blit(scaledbush,(HouseX+houseSize,4*dispHeight/5+dispHeight/10))
			if buyBush2:
				gameDisp.blit(scaledbush,(HouseX*2,4*dispHeight/5+dispHeight/10))

			#controlling the sound with images

			if soundOn:
				gameDisp.blit(scaledSoundOn,(cropButX, 5*dispHeight/6))
				
			if not soundOn:
		
				gameDisp.blit(scaledSoundOff,(cropButX, 5*dispHeight/6))

			if character=="f":
				gameDisp.blit(scaledFarmgirl2,(0+cameraX,cornY+30+cameraY))
		
			if character=="m":
				gameDisp.blit(scaledFarmboy2,(0+cameraX,cornY+30+cameraY))

			

			#drawing the texts and other aspects of the farm
			gameDisp.blit(scaledSpeech,( HouseX/17+cameraX,dispHeight/2-250+cameraY))
			upgradeText = myfont2.render("Welcome %s!" %username, 6, black)
			upgradeText2 = myfont2.render(" Press H for help" , 6, black)
			upgradeText3 = myfont2.render("and I for information", 6, black)
			gameDisp.blit(upgradeText, (HouseX/4+cameraX,dispHeight/2-220+cameraY))
			gameDisp.blit(upgradeText2, (HouseX/5+cameraX,4*dispHeight/7-240+cameraY))
			gameDisp.blit(upgradeText3, (HouseX/6+cameraX,4*dispHeight/7-220+cameraY))

		
			gameDisp.blit(scaledbush,(HouseX,4*dispHeight/5+dispHeight/10))
			gameDisp.blit(scaledcorn,(cropButX,cornY))
			gameDisp.blit(scaledcabbage,(cropButX,cabbageY))
			gameDisp.blit(scaledtomato,(cropButX,tomatoY))
			gameDisp.blit(scaledCoins,(0,0))
			moneyText = myfont.render(" %d " % (money), 6, yellow)
			pygame.draw.rect(gameDisp,backgroundGreen,(70,0,100,50))
			gameDisp.blit(moneyText, (70, 20))
			
			#moving the character around the farm through the camera variable
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

			if pygame.key.get_pressed()[pygame.K_h]:
						gameDisp.blit(scaledInstructions, (0,0))
			if pygame.key.get_pressed()[pygame.K_i]:
						gameDisp.blit(scaledInformation, (0,0))

			if cameraDir=='n':
				cameraY-=20
			elif cameraDir=='s':
				cameraY+=20
			elif cameraDir=='e':
				cameraX+=20
			elif cameraDir=='w':
				cameraX-=20

			pygame.display.update()

			pygame.display.flip()
			

#framework inspired by: https://github.com/kidscancode/pygame_tutorials/blob/master/pygame%20template.py

def pestGameLoop():

	running=True 
	cropsFailed=None
	gameState=None
	

	bugSprites=pygame.sprite.Group()
	playerSprite=pygame.sprite.GroupSingle()

	spray = Spray()
	playerSprite.add(spray)

	
	gameState=True
	numOfHits=0
	counter=15

	pygame.time.set_timer(pygame.USEREVENT, 1000)

	#making bugs enter from random locations
	for i in range(4):
		topbug=Bugs(scaledBug, "top")
		bugSprites.add(topbug)
		
		bottombug=Bugs(scaledBug, "bottom")
		bugSprites.add(bottombug)
		
		leftbug=Bugs(scaledBug, "left")
		bugSprites.add(leftbug)
		
		rightbug=Bugs(scaledBug, "right")
		bugSprites.add(rightbug)
		
	#getting the movement of the spray
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running= False
			if event.type==pygame.USEREVENT:
				counter-=1
				if counter<0:
					counter=0
			if event.type==pygame.KEYDOWN:
				
				if event.key == pygame.K_SPACE:
					gameState=False
					

		#tracking if collisions were made
		hits = pygame.sprite.spritecollide(spray, bugSprites, True)
		
		for hit in hits:
			numOfHits+=1
			
		time=pygame.time.get_ticks()
		
		#updating the groups 
		playerSprite.update()
		bugSprites.update()
		#drawing all the groups
		gameDisp.fill(backgroundGreen)
		playerSprite.draw(gameDisp)
		bugSprites.draw(gameDisp)
		
		
		#AI for bug movement 
		for bug in bugSprites:
			
			if ((spray.rect.centerx-bug.rect.centerx)**2+(spray.rect.centery-bug.rect.centery)**2)**0.5<200:

				print(((spray.rect.centerx-bug.rect.centerx)**2+(spray.rect.centery-bug.rect.centery)**2)**0.5)

				if bug.direction=="top":
					
					bug.speedY=-8
				if bug.direction=="bottom":
					
					bug.speedY=+8
				if bug.direction=="left":
					
					bug.speedY=-8
				if bug.direction=="right":
					
					bug.speedY=+8


		#checking if the player wins
		if numOfHits>=10:
			gameDisp.fill(backgroundGreen)
			winText= myfont.render("Crops Saved!", 6, yellow)
			gameDisp.blit(winText, (270, 200))
			continueButton = Button(blue, contX, contY, contWidth,contHeight, gameDisp)
			continueButton.addText("Press Space to Continue", white)
			cropsFailed=False
			for bug in bugSprites:
				bug.kill()

		#checking if the player loses
		elif counter==0 and numOfHits<10:
			gameDisp.fill(backgroundGreen)
			loseText= myfont.render("Crops Failed!", 6, yellow)
			gameDisp.blit(loseText, (270, 200))
			continueButton = Button(blue, contX, contY, contWidth,contHeight, gameDisp)
			continueButton.addText("Press Space to Continue", white)
			cropsFailed=True
			for bug in bugSprites:
				bug.kill()
			
			
		#ending the gameloop
		if not gameState and cropsFailed:
			return "failed"
		if not gameState and not cropsFailed:
			return "saved"


		#putting the texts on the screen
		timerText = myfont.render("Timer: %d seconds" % (counter), 6, yellow)
		gameDisp.blit(timerText, (0, 20))
		scoreText = myfont.render("Score: %d" % (numOfHits), 6, yellow)
		gameDisp.blit(scoreText, (2*dispWidth/3, 20))
		
		pygame.display.flip()

		


def gameOverLoop():
	running=True

	while running:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running= False
		
		#creates the images and texts that appear
		gameDisp.fill(white)
		gameDisp.blit(scaledfarmtheme,(0,0))

		gameDisp.blit(scaledLogo,(logoX,logoY))
		welcomeText = myfont.render("Game Over!!!" , 6, black)
		gameDisp.blit(welcomeText, (2*dispWidth/5-50, dispHeight/2))
		endButton = Button(green,startX-150,StartY,startWidth,startHeight,gameDisp)
		endButton.addText("Quit Game", black)
		restartButton = Button(green,startX+150,StartY,startWidth,startHeight,gameDisp)
		restartButton.addText("Restart", black)

		if restartButton.hover():
				highlightrestartButton = Button(brightGreen,startX+150,StartY,startWidth,startHeight,gameDisp)
				highlightrestartButton.addText("Restart", black)
		else:
			restartButton=Button(green,startX+150,StartY,startWidth,startHeight,gameDisp)
			restartButton.addText("Restart", black)

		if endButton.hover():
				highlightendButton = Button(brightGreen,startX-150,StartY,startWidth,startHeight,gameDisp)
				highlightendButton.addText("Quit Game", black)
		else:
			endButton=Button(green,startX-150,StartY,startWidth,startHeight,gameDisp)
			endButton.addText("Quit Game", black)
		#returns the choice that the player makes 
		if restartButton.clicked():
			return "restart"

		if endButton.clicked():
			return "Game Over"

		pygame.display.flip()
