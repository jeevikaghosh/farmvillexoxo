
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
import socket
import threading
import os

def getfilename():
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

            # if len(username)!=0 and path.exists("%s.txt"%username):
            #     loadButton= Button(red, userButX+100, userButY+70,startWidth,startHeight,gameDisp)
            #     loadButton.addText("Load Prev Game", black)
            #     if loadButton.hover():
            #         highlightLoadButton= Button(orangeRed,userButX+100, userButY+70,startWidth,startHeight,gameDisp)
            #         highlightLoadButton.addText("Load Prev Game", black)

            #     if loadButton.clicked():
            #         with open("%s.txt" %(username)) as file:
            #             mylist = [line.rstrip('\n') for line in file]
            #             character=mylist[0]
            #             file.close()
            #         theme.stop()
            #         return startGameLoop((character,username), True)
                    # running=False
                # invalidText = myfont.render("!!!Invalid Username!!!", 6, red)
                # gameDisp.blit(invalidText, (userButX+20, userButY+70))
            
            if startButton.clicked() and len(username)!=0:
                f= open("%s.txt"%username,"w+")
                f.close()
                return username

            pygame.display.update()


def RetrFile(name, sock):
    filename = sock.recv(1024)
    if os.path.isfile(filename):
        sock.send("EXISTS " + str(os.path.getsize(filename)))
        userResponse = sock.recv(1024)
        if userResponse[:2] == 'OK':
            with open(filename, 'rb') as f:
                bytesToSend = f.read(1024)
                sock.send(bytesToSend)
                while bytesToSend != "":
                    bytesToSend = f.read(1024)
                    sock.send(bytesToSend)
    else:
        sock.send("ERR ")

    sock.close()

def Main():
    host = '127.0.0.1'
    port = 5000


    s = socket.socket()
    s.bind((host,port))

    s.listen(5)

    print "Server Started."
    while True:
        c, addr = s.accept()
        print "client connedted ip:<" + str(addr) + ">"
        t = threading.Thread(target=RetrFile, args=("RetrThread", c))
        t.start()
         
    s.close()

if __name__ == '__main__':
    Main()


import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    filename = raw_input("Filename? -> ")
    if filename != 'q':
        s.send(filename)
        data = s.recv(1024)
        if data[:6] == 'EXISTS':
            filesize = long(data[6:])
            message = raw_input("File exists, " + str(filesize) +"Bytes, download? (Y/N)? -> ")
            if message == 'Y':
                s.send("OK")
                f = open('new_'+filename, 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print "{0:.2f}".format((totalRecv/float(filesize))*100)+ "% Done"
                print "Download Complete!"
                f.close()
        else:
            print "File Does Not Exist!"

    s.close()
    

if __name__ == '__main__':
    Main()





