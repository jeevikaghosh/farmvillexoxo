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
import shelve

 



def introLoop():
	running = True
	logoX=dispWidth/5
	logoY=dispHeight/6-50
	startWidth = dispWidth/5
	startHeight = dispHeight/7
	startX=2*dispWidth/5
	StartY=4*dispHeight/5
	usernameY=2*dispHeight/5
	userButY=3*dispHeight/5-50
	userButX=dispWidth/5+50
	userWidth=dispWidth/2
	userHeight=dispHeight/10
	welcomeTextX=dispWidth/7
	
	# theme=pygame.mixer.Sound(path.join(soundDir,"farmtheme.ogg"))
	theme.play()
	theme.set_volume(0.1)
	# pygame.mixer.Sound(path.join(soundDir,"farmtheme.ogg")).set_volume(0.1)
	
	
	username=""

	while running: 
		# print(theme)
		# theme
		for event in pygame.event.get():
			if event.type== pygame.QUIT:
				return 0

			if event.type==pygame.KEYDOWN:
				print(str(event.key))
				if event.key in keyDict:
					print(True)

					username+=keyDict[event.key]
					print(username)

				if event.key==8:
					print (username,username[:-2] )
					username=username[:-1]

			gameDisp.fill(white)

			welcomeText = myfont.render("Welcome to" , 6, black)
			gameDisp.blit(welcomeText, (2*dispWidth/5-50, 20))
			
			usernameText = myfont.render("Type your username to begin:" , 6, black)
			gameDisp.blit(usernameText, (startWidth, usernameY))

			usernameButton = Button(green,userButX,userButY,userWidth,userHeight,gameDisp)
			startButton = Button(green,startX,StartY,startWidth,startHeight,gameDisp)
			startButton.addText("Start New Game",black)

			mouse = pygame.mouse.get_pos()

			
			if startButton.hover():
				highlightStartButton= Button(brightGreen,startX,StartY,startWidth,startHeight,gameDisp)
				highlightStartButton.addText("Start New Game", black)

			if usernameButton.hover():
				highlightUsernameButton= Button(brightGreen,userButX,userButY,userWidth,userHeight,gameDisp)
			
			gameDisp.blit(scaledLogo,(logoX,logoY))

			usernameText = myfont.render(username , 6, black)
			gameDisp.blit(usernameText, (userButX+20, userButY+10))

			if len(username)!=0 and path.exists("%s.txt"%username):
				loadButton= Button(red, userButX+100, userButY+70,startWidth,startHeight,gameDisp)
				loadButton.addText("Load Prev Game", black)
				if loadButton.hover():
					highlightLoadButton= Button(orangeRed,userButX+100, userButY+70,startWidth,startHeight,gameDisp)
					highlightLoadButton.addText("Load Prev Game", black)

				if loadButton.clicked():
					with open("%s.txt" %(username)) as file:
						mylist = [line.rstrip('\n') for line in file]
						character=mylist[0]
						file.close()
					theme.stop()
					return startGameLoop((character,username), True)
    				# running=False
				# invalidText = myfont.render("!!!Invalid Username!!!", 6, red)
				# gameDisp.blit(invalidText, (userButX+20, userButY+70))
			
			if startButton.clicked() and len(username)!=0:
				f= open("%s.txt"%username,"w+")
				f.close()
				return username

			pygame.display.update()


def characterLoop(username):
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
	print("char",username)
	
	while running: 

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 0

				
			gameDisp.fill(white)

			characterText = myfont.render("Choose your Character:" , 6, black)
			gameDisp.blit(characterText, (logoX, startHeight))

			maleCharButton= Button(blue,maleCharButX,charButY,charButWidth,CharButHeight,gameDisp)

			femCharButton=Button(pink,femCharButX,charButY,charButWidth,CharButHeight,gameDisp)

			

			mouse = pygame.mouse.get_pos()

		
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
				theme.stop()
				return ((character, username))
			if femButClicked:
				highlightmaleCharButton = Button(brightPink,femCharButX,charButY,charButWidth,CharButHeight,gameDisp)
				theme.stop()
				return ((character, username))

			
			gameDisp.blit(scaledFarmgirl,(femCharButX,charButY))
			gameDisp.blit(scaledFarmboy,(maleCharButX,charButY+margin))
		

			pygame.display.update()



def startGameLoop(specs, load=False):
	character, username= specs
	running = True

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
	print("game",username, character)
	
	written=[]

	soundOn=True

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


	cropButWidth = dispWidth/7
	cropButHeight = dispHeight/8
	cropButX=4.5*dispWidth/5
	cornY=dispHeight/5+dispHeight/20
	cabbageY=2*dispHeight/5+dispHeight/20
	tomatoY=3*dispHeight/5+dispHeight/20
	HouseX=dispWidth/3
	saveButX=4*dispWidth/5-40
	saveButY=dispHeight/15


	cornButton = Button(red,cropButX,cornY,cropButWidth,cropButHeight,gameDisp)
	
	cabbageButton = Button(red,cropButX,cabbageY,cropButWidth,cropButHeight,gameDisp)
	
	tomatoButton = Button(red,cropButX,tomatoY,cropButWidth,cropButHeight,gameDisp)
	
	background.play()

	cropButtons.append(cornButton)
	cropButtons.append(cabbageButton)
	cropButtons.append(tomatoButton)

	for i in range(margin,numOfTiles*tileSize,tileSize):
		for j in range(margin,numOfTiles*tileSize-tileSize,tileSize):
				newGrassTile = tile(tileSize, i+cameraX, j+cameraY, gameDisp, path.join(imageDir,"grasstile.jpg"))
				allGrassTiles.append(newGrassTile)

	
	if load:
		with open("%s.txt"%username) as file:
			mylist = [line.rstrip('\n') for line in file]
			money = int(mylist[1])
			if mylist[2]=="1":
				buyTree=True
			if mylist[2]=="2":
				buyTree=True
				buyTree2=True
			if mylist[3]=="1":
				buyBush=True
			if mylist[3]=="2":
				buyBush=True
				buyBush2=True
			if mylist[4]=="1":
				upgradeHouse=True
			if mylist[4]=="2":
				upgradeHouse=True
				upgradeFarmhouse=True

			loadGrassTiles=[]
			loadPloughTiles=[]
			for i in range(margin,numOfTiles*tileSize,tileSize):
				for j in range(margin,numOfTiles*tileSize-tileSize,tileSize):
					
					if ("x= %d y= %d" % (i , j)) in mylist[5]:
						newGrassTile = tile(tileSize, i+cameraX, j+cameraY, gameDisp, path.join(imageDir,"grasstile.jpg"))
						loadGrassTiles.append(newGrassTile)

			for i in range(margin,numOfTiles*tileSize,tileSize):
				for j in range(margin,numOfTiles*tileSize-tileSize,tileSize):
					
					if ("x= %d y= %d" % (i , j)) in mylist[6]:
						newPloughTile = tile(tileSize, i+cameraX, j+cameraY, gameDisp, path.join(imageDir,"soil2.png"))
						loadPloughTiles.append(newPloughTile)
			print(loadGrassTiles)
			allPloughTiles=loadPloughTiles
			allGrassTiles=loadGrassTiles

			
        	# character =  file [1]
        # file.close()

	while running: 

		
			screenButton=Button(backgroundGreen,0,0,dispWidth,dispHeight,gameDisp)

			if len(allGrassTiles)!=0:
				for singtile in allGrassTiles: 
					singtile.draw()

			if len(allPloughTiles)!=0:
				for singtile in allPloughTiles: 
					singtile.draw()

			if len(allFadedPloughTiles)!=0:
				for singtile in allFadedPloughTiles: 
					singtile.draw()

			if len(allHighlightedTiles)!=0:
				for singtile in allHighlightedTiles: 
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
			if money==0:
				return "Game Over"

				running=False

			
			if houseButton.clicked():
				if money>=100:
					if upgradeHouse:
						upgradeFarmhouse=True
					upgradeHouse=True
					
					money-=100
				else:
					noMoneyText = myfont2.render("Not enough coins", 6, red)
					gameDisp.blit(noMoneyText, (HouseX*2,0))


			if treeButton.clicked():
				
				if money>=50:
					if buyTree:
						buyTree2=True
					buyTree=True
					
					money-=50
				else:
					noMoneyText = myfont2.render("Not enough coins", 6, red)
					gameDisp.blit(noMoneyText, (HouseX/15,dispHeight/2+20))

			if bushButton.clicked():
				
				if money>=30:
					if buyBush:
						buyBush2=True
					buyBush=True
					
					money-=30

				else:
					noMoneyText = myfont2.render("Not enough coins", 6, red)
					gameDisp.blit(noMoneyText, (HouseX/2+20,dispHeight-50))

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

			# if farmerButton.hover():
				
				
			# else:
			# 	pygame.draw.rect(gameDisp,backgroundGreen,(HouseX/15,dispHeight/2-170,350,50))
			
			if soundButton.clicked():
					print("smxk")
					if not soundOn:
						background.play()
						soundOn=True
					elif soundOn:
						soundOn=False
						background.stop()
						
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

				written=[character, str(money), str(numOfTrees),  str(numOfBushes), str(houseUpgrades), str(allGrassTiles), str(allPloughTiles)]
				print(written)
				newFile = ""
				for elem in written:
					newFile += (elem + "\n")
# Writing
				with open("%s.txt" %(username), 'w') as file:
					file.write(newFile)
					file.close()

			# if visitButton.clicked():


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
			

			for cropButton in cropButtons:
				if cropButton.clicked():
					chosenCrop=cropButton
					print(chosenCrop)
					highlightButton=Button(orangeRed,cropButton.x,cropButton.y,cropButton.width,cropButton.height,gameDisp)


			# gameDisp.fill(backgroundGreen)

			if len(allBugTiles)!=0:
				for singtile in allBugTiles:
		

					if singtile.clicked():
						
						pestGameLoopExit=pestGameLoop()

					
						if pestGameLoopExit=="failed":
							print(singtile.currentImg)

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
			# gameDisp.fill(backgroundGreen)
			if len(allFadedPloughTiles)!=0:
				for singtile in allFadedPloughTiles:
					currentTime=pygame.time.get_ticks()
					# pr int("ct", currentTime, "st", singtile.startTime, "dif", currentTime-singtile.startTime )
					if (currentTime-singtile.startTime)>1000 and (currentTime-singtile.startTime)//1000%3==0:
						# print ("sxjsnj")
						allPloughTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"soil2.png"), time))
						singtile.clickedTile=True
						allFadedPloughTiles.remove(singtile)

			if len(allGrassTiles)!=0:
				for singtile in allGrassTiles:
					# if not singtile.clickedTile:
					if singtile.clicked():
						time=pygame.time.get_ticks()
						allFadedPloughTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"soilfaded.png"), time))
						singtile.clickedTile=True
						allGrassTiles.remove(singtile)
						print (pygame.time.get_ticks())
						print(allGrassTiles)
						print("clicked tile at " + str(singtile.x) + "," + str(singtile.y)+"clicked" +str(singtile.clickedTile))
						money-=20
				
				
					# if singtile.x+tileSize > mouse[0] > singtile.x and singtile.y+tileSize > mouse[1] > singtile.y:
					# 	print("laala")
					# 	highlightSingtile = tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"grasstilefaded.jpg"))
					# else:
					# 	unhighlightSingtile = tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"grasstile.jpg"))
					if singtile.hover():
						allHighlightedTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"grasstilefaded.jpg")))
						print(allHighlightedTiles)
					elif not singtile.hover():
						allHighlightedTiles=allHighlightedTiles[:-1]
			
				# # 	print("hovered tile at " + str(singtile.x) + ", " + str(singtile.y))



			if len(allPloughTiles)!=0:
				for singtile in allPloughTiles:
					# currentTime=pygame.time.get_ticks()
					# print("ct", currentTime, "st", singtile.startTime, "dif", currentTime-singtile.startTime )
					# if (currentTime-singtile.startTime)>1000 and (currentTime-singtile.startTime)//1000%3==0:
					# print ("sxjsnj")

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

						

			if len(allSeedTiles)!=0:
				for singtile in allSeedTiles:
					currentTime=pygame.time.get_ticks()
				# print("ct", currentTime, "st", singtile.startTime, "dif", currentTime-singtile.startTime )
					# if (currentTime-singtile.startTime)>1000 and (currentTime-singtile.startTime)//1000%3==0:
					# print ("sxjsnj")
					centerX  = singtile.x+int(singtile.size/2)
					centerY = singtile.y+int(singtile.size/2)
					radius = int(singtile.size/4)

					if (currentTime-singtile.startTime)>1000: 
						pygame.draw.circle(gameDisp, white, (centerX, centerY),radius)
						
					if (currentTime-singtile.startTime)>1000 and singtile.currentImg==path.join(imageDir,"cornseeds.jpg"): 	
						
						angle=int(((currentTime-singtile.startTime)//1000)/cornTime*360)
						points = [(centerX, centerY)]
						# angle = 
						# Get points on arc
						for i in range(-90,angle-90):
							x = centerX + int(radius*math.cos(i*math.pi/180))
							y = centerY+int(radius*math.sin(i*math.pi/180))
							points.append((x, y))
							# print ("n", i, "(x, y)", (x, y), "r", radius)
						points.append((centerX, centerY))
						
						# Draw pie segment
						if len(points) > 2:
							pygame.draw.polygon(gameDisp, green, points)

					if (currentTime-singtile.startTime)>1000 and singtile.currentImg==path.join(imageDir,"tomatoseeds.jpg"): 	
						
						angle=int(((currentTime-singtile.startTime)//1000)/tomatoTime*360)
						points = [(centerX, centerY)]
						# angle = 
						# Get points on arc
						for i in range(-90,angle-90):
							x = centerX + int(radius*math.cos(i*math.pi/180))
							y = centerY+int(radius*math.sin(i*math.pi/180))
							points.append((x, y))
							
						points.append((centerX, centerY))
						
						# Draw pie segment
						if len(points) > 2:
							pygame.draw.polygon(gameDisp, green, points)

					if (currentTime-singtile.startTime)>1000 and singtile.currentImg==path.join(imageDir,"cabbageseeds.jpg"): 	
						
						angle=int(((currentTime-singtile.startTime)//1000)/cabbageTime*360)
						points = [(centerX, centerY)]
						# angle = 
						# Get points on arc
						for i in range(-90,angle-90):
							x = centerX + int(radius*math.cos(i*math.pi/180))
							y = centerY+int(radius*math.sin(i*math.pi/180))
							points.append((x, y))
							
						points.append((centerX, centerY))
						
						# Draw pie segment
						if len(points) > 2:
							pygame.draw.polygon(gameDisp, green, points)



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
				

			if len(allCropTiles)!=0:
				for singtile in allCropTiles:

					if singtile.clicked():
						time=pygame.time.get_ticks()

						if singtile.currentImg==path.join(imageDir,"cornfield.jpg") and not singtile.bugs:
							money+=30
						if singtile.currentImg==path.join(imageDir,"tomatofield.jpg")and not singtile.bugs:
							money+=40
						if singtile.currentImg==path.join(imageDir,"cabbagefield.jpg")and not singtile.bugs:
							money+=50
						allFadedPloughTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"soilfaded.png"), time))
						allCropTiles.remove(singtile)

			# randomInd=random.randint(len(allCropTiles)-1)

			# randTile=allCropTiles[ranomInd]

			if len(allCropTiles)!=0:
				for singtile in allCropTiles:
					currentTime=pygame.time.get_ticks()
				# print("ct", currentTime, "st", singtile.startTime, "dif", currentTime-singtile.startTime )
					# if (currentTime-singtile.startTime)>1000 and (currentTime-singtile.startTime)//1000%3==0:
					# print ("sxjsnj")

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



						
			if len(allRottenTiles)!=0:
				for singtile in allRottenTiles:

					if singtile.clicked():
						time=pygame.time.get_ticks()
						money-=5
						print("clicked")
						allFadedPloughTiles.append(tile(tileSize, singtile.x, singtile.y, gameDisp, path.join(imageDir,"soilfaded.png"), time))
						allRottenTiles.remove(singtile)
			
			if not upgradeHouse:
				gameDisp.blit(scaledHouse2,(HouseX,0))
			if upgradeHouse and not upgradeFarmhouse:
				
				gameDisp.blit(scaledHouse,(HouseX,0))
			if  upgradeFarmhouse:
				print("sjxnjs")
				
				gameDisp.blit(scaledHouse3,(HouseX,0))
		

			

			if buyTree:
				gameDisp.blit(scaledTree1,(HouseX/15-dispHeight/20,4*dispHeight/5-dispHeight/10))
			if buyTree2:
				gameDisp.blit(scaledTree1,(HouseX/10,4*dispHeight/5))

			if buyBush:
				gameDisp.blit(scaledbush,(HouseX+houseSize,4*dispHeight/5+dispHeight/10))
			if buyBush2:
				gameDisp.blit(scaledbush,(HouseX*2,4*dispHeight/5+dispHeight/10))


			if soundOn:
				gameDisp.blit(scaledSoundOn,(cropButX, 5*dispHeight/6))
				
			if not soundOn:
		
				gameDisp.blit(scaledSoundOff,(cropButX, 5*dispHeight/6))

			if character=="f":
				gameDisp.blit(scaledFarmgirl2,(0+cameraX,cornY+30+cameraY))
		
			if character=="m":
				gameDisp.blit(scaledFarmboy2,(0+cameraX,cornY+30+cameraY))

			# for tile in allPloughTiles:

			
			gameDisp.blit(scaledSpeech,( HouseX/17+cameraX,dispHeight/2-250+cameraY))
			upgradeText = myfont2.render("Welcome %s!" %username, 6, black)
			upgradeText2 = myfont2.render(" Press H for help" , 6, black)
			upgradeText3 = myfont2.render("and I for information", 6, black)
			gameDisp.blit(upgradeText, (HouseX/4+cameraX,dispHeight/2-220+cameraY))
			gameDisp.blit(upgradeText2, (HouseX/5+cameraX,4*dispHeight/7-240+cameraY))
			gameDisp.blit(upgradeText3, (HouseX/6+cameraX,4*dispHeight/7-220+cameraY))

			gameDisp.blit(scaledTree2,(HouseX/10,3*dispHeight/5))
			# gameDisp.blit(scaledTree1,(HouseX/15-dispHeight/20,4*dispHeight/5-dispHeight/10))
			gameDisp.blit(scaledbush,(HouseX,4*dispHeight/5+dispHeight/10))
			# gameDisp.blit(scaledTree1,(HouseX/10,4*dispHeight/5))
			gameDisp.blit(scaledcorn,(cropButX,cornY))
			gameDisp.blit(scaledcabbage,(cropButX,cabbageY))
			gameDisp.blit(scaledtomato,(cropButX,tomatoY))
			gameDisp.blit(scaledCoins,(0,0))
			moneyText = myfont.render(" %d " % (money), 6, yellow)
			pygame.draw.rect(gameDisp,backgroundGreen,(70,0,100,50))
			gameDisp.blit(moneyText, (70, 20))
			
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
					# if event.key==pygame.K_h:
					# 	print("h")
					# 	gameDisp.blit(scaledInstructions, (0,0))

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
			



def pestGameLoop():

	running=True 
	cropsFailed=None
	gameState=None
	contX=2*dispWidth/5
	contY=3*dispHeight/5
	contWidth = dispWidth/3
	contHeight = dispHeight/8

	bugSprites=pygame.sprite.Group()
	playerSprite=pygame.sprite.GroupSingle()
	# allSprites=pygame.sprite.Group()
	spray = Spray()
	playerSprite.add(spray)
	# allSprites.add(spray)
	
	gameState=True
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
			if event.type==pygame.KEYDOWN:
				print(str(event.key))
				if event.key == pygame.K_SPACE:
					gameState=False
					


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
		gameDisp.fill(backgroundGreen)
		playerSprite.draw(gameDisp)
		bugSprites.draw(gameDisp)
		# allSprites.draw(gameDisp)
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



		if numOfHits>=10:
			gameDisp.fill(backgroundGreen)
			winText= myfont.render("Crops Saved!", 6, yellow)
			gameDisp.blit(winText, (200, 200))
			continueButton = Button(blue, contX, contY, contWidth,contHeight, gameDisp)
			continueButton.addText("Press Space to Continue", white)
			cropsFailed=False
			for bug in bugSprites:
				bug.kill()


		elif counter==0 and numOfHits<10:
			gameDisp.fill(backgroundGreen)
			loseText= myfont.render("Crops Failed!", 6, yellow)
			gameDisp.blit(loseText, (200, 200))
			continueButton = Button(blue, contX, contY, contWidth,contHeight, gameDisp)
			continueButton.addText("Press Space to Continue", white)
			cropsFailed=True
			for bug in bugSprites:
				bug.kill()
			
			
		
		if not gameState and cropsFailed:
			return "failed"
		if not gameState and not cropsFailed:
			return "saved"


		timerText = myfont.render("Timer: %d seconds" % (counter), 6, yellow)
		gameDisp.blit(timerText, (0, 20))
		scoreText = myfont.render("Score: %d" % (numOfHits), 6, yellow)
		gameDisp.blit(scoreText, (2*dispWidth/3, 20))
		#flip display
		pygame.display.flip()

		# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error



def gameOverLoop():
	running=True

	logoX=dispWidth/5
	logoY=dispHeight/6-50
	startWidth = dispWidth/5
	startHeight = dispHeight/7
	startX=2*dispWidth/5
	StartY=4*dispHeight/5
	usernameY=2*dispHeight/5
	userButY=3*dispHeight/5-50
	userButX=dispWidth/5+50
	userWidth=dispWidth/2
	userHeight=dispHeight/10
	welcomeTextX=dispWidth/7
	
	while running:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running= False
		
		gameDisp.fill(white)

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

		if restartButton.clicked():
			return "restart"

		if endButton.clicked():
			running=False

		pygame.display.flip()
