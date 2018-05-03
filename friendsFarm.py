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

def friendsFarmIntro(savedFriends):

	running=True

	click1=False
	click2=False
	click3=False
	click4=False
	click5=False
	click6=False
	
	theme.play()

	
	friendUsername=""

	while running: 

		#gets the friends username from user input
		
		for event in pygame.event.get():
			if event.type== pygame.QUIT:
				return 0

			if event.type==pygame.KEYDOWN:
				print(str(event.key))
				if event.key in keyDict:
					print(True)

					friendUsername+=keyDict[event.key]
					print(username)

				if event.key==8:
					print (username,username[:-2] )
					friendUsername=friendUsername[:-1]

			gameDisp.fill(white)
			gameDisp.blit(scaledfarmtheme,(0,0))

			backButton = Button(red, cropButX-100, 5*dispHeight/6, cropButWidth,cropButHeight, gameDisp)
		
			#returns to the farm			
			if backButton.clicked():
				theme.stop()
				background.play()
				return savedFriends

			
			if backButton.hover():
				highlightsaveButton = Button(orangeRed,cropButX-100, 5*dispHeight/6, cropButWidth,cropButHeight,gameDisp)
				highlightsaveButton.addText("Back", white)
			else:
				backButton=Button(red,cropButX-100, 5*dispHeight/6, cropButWidth,cropButHeight,gameDisp)
				backButton.addText("Back", white)

			welcomeText = myfont.render("Type your friend's name to visit their Farm:" , 6, black)
			gameDisp.blit(welcomeText, (welcomeTextX-100, 15))
			
		
			friendUsernameButton = Button(green,userButX,userButY-240,userWidth,userHeight,gameDisp)
		
			mouse = pygame.mouse.get_pos()

			#displays the add farm on the possible farms that could be added in the roster
			if not click1:
				friendBut1=Button(green,friendX1,friendY1,startWidth,startHeight,gameDisp)
				friendBut1.addText("+", black)
			if not click2:
				friendBut2=Button(green,friendX2,friendY1,startWidth,startHeight,gameDisp)
				friendBut2.addText("+", black)
			if not click3:
				friendBut3=Button(green,friendX3,friendY1,startWidth,startHeight,gameDisp)
				friendBut3.addText("+", black)
			if not click4:
				friendBut4=Button(green,friendX1,friendY2,startWidth,startHeight,gameDisp)
				friendBut4.addText("+", black)
			if not click5:
				friendBut5=Button(green,friendX2,friendY2,startWidth,startHeight,gameDisp)
				friendBut5.addText("+", black)
			if not click6:
				friendBut6=Button(green,friendX3,friendY2,startWidth,startHeight,gameDisp)
				friendBut6.addText("+", black)


			#displaying the texts in when the mouse is hovered on the roster
			if friendBut1.hover() and not click1:
				highlightFriend1But=Button(brightGreen,friendX1,friendY1,startWidth,startHeight,gameDisp)
				highlightFriend1But.addText("Add Farm", black)
			if friendBut2.hover() and not click2:
				highlightFriend1But=Button(brightGreen,friendX2,friendY1,startWidth,startHeight,gameDisp)
				highlightFriend1But.addText("Add Farm", black)
			if friendBut3.hover() and not click3:
				highlightFriend1But=Button(brightGreen,friendX3,friendY1,startWidth,startHeight,gameDisp)
				highlightFriend1But.addText("Add Farm", black)
			if friendBut4.hover() and not click4:
				highlightFriend1But=Button(brightGreen,friendX1,friendY2,startWidth,startHeight,gameDisp)
				highlightFriend1But.addText("Add Farm", black)
			if friendBut5.hover() and not click5:
				highlightFriend1But=Button(brightGreen,friendX2,friendY2,startWidth,startHeight,gameDisp)
				highlightFriend1But.addText("Add Farm", black)
			if friendBut6.hover() and not click6:
				highlightFriend1But=Button(brightGreen,friendX3,friendY2,startWidth,startHeight,gameDisp)
				highlightFriend1But.addText("Add Farm", black)

			#username bar and username text

			if friendUsernameButton.hover():
				highlightUsernameButton= Button(brightGreen,userButX,userButY-240,userWidth,userHeight,gameDisp)
			
			usernameText = myfont.render(friendUsername , 6, black)
			gameDisp.blit(usernameText, (userButX+20, userButY+10-240))

			#makes sure the user name exists, and adds the username to the dict of saved friends 
			if len(friendUsername)!=0 and path.exists("%s.txt"%friendUsername):
				if friendBut1.clicked():
					highlightFriend1But=Button(brightGreen,friendX1,friendY1,startWidth,startHeight,gameDisp)
					highlightFriend1But.addText("%s"%friendUsername, black)
					click1=True
					savedFriends[1]="%s"%friendUsername
					theme.stop()
				if friendBut2.clicked():
					highlightFriend1But=Button(brightGreen,friendX2,friendY1,startWidth,startHeight,gameDisp)
					highlightFriend1But.addText("%s"%friendUsername, black)
					click2=True
					savedFriends[2]="%s"%friendUsername
					theme.stop()
				if friendBut3.clicked():
					highlightFriend1But=Button(brightGreen,friendX3,friendY1,startWidth,startHeight,gameDisp)
					highlightFriend1But.addText("%s"%friendUsername, black)
					click3=True
					savedFriends[3]="%s"%friendUsername
					theme.stop()
				if friendBut4.clicked():
					highlightFriend1But=Button(brightGreen,friendX1,friendY2,startWidth,startHeight,gameDisp)
					highlightFriend1But.addText("%s"%friendUsername, black)
					click4=True
					savedFriends[4]="%s"%friendUsername
					theme.stop()
				if friendBut5.clicked():
					highlightFriend1But=Button(brightGreen,friendX2,friendY2,startWidth,startHeight,gameDisp)
					highlightFriend1But.addText("%s"%friendUsername, black)
					click5=True
					savedFriends[5]="%s"%friendUsername
					theme.stop()
				if friendBut6.clicked():
					highlightFriend1But=Button(brightGreen,friendX3,friendY2,startWidth,startHeight,gameDisp)
					highlightFriend1But.addText("%s"%friendUsername, black)
					click6=True
					savedFriends[6]="%s"%friendUsername
					theme.stop()
				
				
				usernameText = myfont.render("Friend exists" , 6, black)
				gameDisp.blit(usernameText, (startWidth+100, usernameY-100))

				#drawing the load button and the features of it
				loadButton= Button(red, startX,StartY,startWidth,startHeight,gameDisp)
				loadButton.addText("Load their Farm", black)
				if loadButton.hover():
					highlightLoadButton= Button(orangeRed, startX,StartY,startWidth,startHeight,gameDisp)
					highlightLoadButton.addText("Load their Farm", black)

				if loadButton.clicked():
					with open("%s.txt" %(friendUsername)) as file:
						mylist = [line.rstrip('\n') for line in file]
						character=mylist[0]
						file.close()
					theme.stop()
					startFriendGameLoop((character,friendUsername), True)
    		

			elif len(friendUsername)!=0:
				usernameText = myfont.render("Friend Does not exists" , 6, red)
				gameDisp.blit(usernameText, (startWidth, usernameY-100))

			#when you return to the visit farm feature you can revisit the friends easily by clicking the button
			#and these functions make that possible for all six places in the roster
			for key in savedFriends:
				if key==1 and savedFriends[1]!=0:
					friendBut1=Button(green,friendX1,friendY1,startWidth,startHeight,gameDisp)
					friendBut1.addText("%s"%savedFriends[1], black)
					if friendBut1.clicked():
						with open("%s.txt" %(savedFriends[1])) as file:
							mylist = [line.rstrip('\n') for line in file]
							character=mylist[0]
							file.close()
							theme.stop()
							startFriendGameLoop((character,savedFriends[1]), True)
					
				if key==2 and savedFriends[2]!=0:
					friendBut1=Button(green,friendX2,friendY1,startWidth,startHeight,gameDisp)
					friendBut1.addText("%s"%savedFriends[2], black)
					if friendBut2.clicked():
						with open("%s.txt" %(savedFriends[2])) as file:
							mylist = [line.rstrip('\n') for line in file]
							character=mylist[0]
							file.close()
							theme.stop()
							startFriendGameLoop((character,savedFriends[2]), True)

				if key==3 and savedFriends[3]!=0:
					friendBut1=Button(green,friendX3,friendY1,startWidth,startHeight,gameDisp)
					friendBut1.addText("%s"%savedFriends[3], black)
					if friendBut3.clicked():
						with open("%s.txt" %(savedFriends[3])) as file:
							mylist = [line.rstrip('\n') for line in file]
							character=mylist[0]
							file.close()
							theme.stop()
							startFriendGameLoop((character,savedFriends[3]), True)

				if key==4 and savedFriends[4]!=0:
					friendBut1=Button(green,friendX1,friendY2,startWidth,startHeight,gameDisp)
					friendBut1.addText("%s"%savedFriends[4], black)
					if friendBut4.clicked():
						with open("%s.txt" %(savedFriends[4])) as file:
							mylist = [line.rstrip('\n') for line in file]
							character=mylist[0]
							file.close()
							theme.stop()
							startFriendGameLoop((character,savedFriends[4]), True)

				if key==5 and savedFriends[5]!=0:
					friendBut1=Button(green,friendX2,friendY2,startWidth,startHeight,gameDisp)
					friendBut1.addText("%s"%savedFriends[5], black)
					if friendBut5.clicked():
						with open("%s.txt" %(savedFriends[5])) as file:
							mylist = [line.rstrip('\n') for line in file]
							character=mylist[0]
							file.close()
							theme.stop()
							startFriendGameLoop((character,savedFriends[5]), True)


				if key==6 and savedFriends[6]!=0:
					friendBut1=Button(green,friendX3,friendY2,startWidth,startHeight,gameDisp)
					friendBut1.addText("%s"%savedFriends[6], black)
					if friendBut6.clicked():
						with open("%s.txt" %(savedFriends[6])) as file:
							mylist = [line.rstrip('\n') for line in file]
							character=mylist[0]
							file.close()
							theme.stop()
							startFriendGameLoop((character,savedFriends[6]), True)

				
			pygame.display.update()


#this game loop is just a simplified version of the startGameLoop i.e. without the 
#ability to make changes to the other farms

def startFriendGameLoop(specs, load=False):
	character, username= specs
	working = True

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

	allPloughTiles = []


	background.play()

	

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

	while working: 

		
			screenButton=Button(backgroundGreen,0,0,dispWidth,dispHeight,gameDisp)

			if len(allGrassTiles)!=0:
				for singtile in allGrassTiles: 
					singtile.draw()

			if len(allPloughTiles)!=0:
				for singtile in allPloughTiles: 
					singtile.draw()

			

			backButton = Button(red, saveButX, saveButY, cropButWidth,cropButHeight, gameDisp)
			soundButton = Button(backgroundGreen, cropButX, 5*dispHeight/6, cropButWidth,cropButHeight, gameDisp)
			
			
			
			if soundButton.clicked():
					
					if not soundOn:
						background.play()
						soundOn=True
					elif soundOn:
						soundOn=False
						background.stop()
						
			if backButton.clicked():
				background.stop()
				working=False
				

			
			if backButton.hover():
				highlightsaveButton = Button(orangeRed,saveButX, saveButY, cropButWidth,cropButHeight,gameDisp)
				highlightsaveButton.addText("Back", white)
			else:
				backButton=Button(red,saveButX, saveButY, cropButWidth,cropButHeight,gameDisp)
				backButton.addText("Back", white)

			
			if soundButton.hover():
				highlightsaveButton = Button(green,cropButX, 5*dispHeight/6, cropButWidth,cropButHeight,gameDisp)
			else:
				soundButton=Button(backgroundGreen,cropButX, 5*dispHeight/6, cropButWidth,cropButHeight,gameDisp)

			
			if not upgradeHouse:
				gameDisp.blit(scaledHouse2,(HouseX,0))
			if upgradeHouse and not upgradeFarmhouse:
				
				gameDisp.blit(scaledHouse,(HouseX,0))
			if  upgradeFarmhouse:
				print("sjxnjs")
				
				gameDisp.blit(scaledHouse3,(HouseX,0))
		
			
			gameDisp.blit(scaledTree2,(HouseX/10,3*dispHeight/5))
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

			

			
			gameDisp.blit(scaledSpeech,( HouseX/17+cameraX,dispHeight/2-250+cameraY))
			upgradeText = myfont2.render("Welcome to ", 6, black)
			upgradeText2 = myfont2.render("%s's Farm!" %username, 6, black)
			
			gameDisp.blit(upgradeText, (HouseX/4+cameraX,4*dispHeight/7-250+cameraY))
			gameDisp.blit(upgradeText2, (HouseX/4+cameraX-10,4*dispHeight/7-230+cameraY))
			gameDisp.blit(scaledbush,(HouseX,4*dispHeight/5+dispHeight/10))
			
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
			

