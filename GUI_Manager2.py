#Version 0.0.8
from Tkinter import *
import tkFont
##from soundHandler import soundHandler

masterWidth = 1000
masterHeight = 500

frameWidth = 500
frameHeight = 500

class GUI_Manager2:
    ##soundPlayer = soundHandler()    #object for soundHandler. used to play music and sound effects

    def __init__(self, master = None):
        ## Initialization
        self.frame = Frame(master)                          #Create a frame to hold stuff for startScreen
        self.root = master                                  #Save tk object to local var 
        
        ## Main Window Settings
        master.minsize(width = masterWidth, height = masterHeight)           #Set minimum size to main window
        master.resizable(width = False, height = False)     #Make window not resizable 

        ## Frame Settings
        self.frame.config(width = frameWidth, height = frameHeight)        #Set dimensions for frame

        ## Pack
        self.frame.pack()                                   #pack startscreen into window
        
    def startMenu(self):
        ## Font Setup
        buttonFont = tkFont.Font(size = 24)                 #Create custom font for buttons
        titleFont = tkFont.Font(size = 30)                  #Create custom font for buttons

        ## New Game Button
        buttonStart = Button(self.frame, text = "New Game",command = lambda: self.startGame(),font = buttonFont)        #created button for start screen 
        buttonStart.place(bordermode = OUTSIDE, height = 100, width = 250, relx = 0.30, rely = .20)                     #Set button in place, set dimensions

        ## Load Game Button
        buttonCont = Button(self.frame, text = "Continue Game",command = lambda: self.loadGame(),font = buttonFont)     #create button for load screen
        buttonCont.place(bordermode = OUTSIDE, height = 100, width = 250, relx = 0.30, rely = .45)                      #set button in place, set dimensions


        ## Exit Game Button
        buttonExit = Button(self.frame, text = "Exit Game", font = buttonFont)                                          #create button for game exit
        buttonExit.place(bordermode = OUTSIDE, height = 100, width = 250, relx = 0.30, rely = .70)                      #set button in place, set dimensions 

        ## Setup Title
        title = Label(self.frame,text = "Camp Epsilon", font = titleFont)                                               #Create label for title
        title.place(bordermode = OUTSIDE, height = 90, width = 300, relx = 0.20, rely = .007)                           #set label in place and set dimensions

        #soundplayer.updateMusic(placeholder)               #play music on screen
    