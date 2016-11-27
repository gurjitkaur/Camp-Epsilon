#Version 0.0.9
from Tkinter import *
import tkFont
import ttk
#from PIL import ImageTk, Image <-- Probably will not need this
from soundHandler import soundHandler
#from UserFile_Handler import UserFile_Handler

#Used for testing will delete this class
class Choice:
    answers = []
    results = []
    def setChoice(self,answer,result):
        self.answers.append(answer)
        self.results.append(result)

class GUI_Manager:
    #userFile = UserFile_Handler()  #object for userfile. used for getting save files and creating new saves
    soundPlayer = soundHandler()    #object for soundHandler. used to play music and sound effects
    
    y = 50  #y coordinate to place text on canvas
    def __init__(self,master = None):
        
        self.main_frame = ttk.Frame(master)                 #Set main frame, the other three smaller frames will go inside the main frame
        self.main_frame.pack()                              #Pack the main frame into place
        self.main_frame.config(height = 600, width = 1000)  #Set the height and width of the main frame
        self.main_frame.config(relief = RIDGE)              #Style the border
        self.main_frame.config(padding = (15, 15))          #Add padding to main frame

        self.bkg_frame = ttk.Frame(self.main_frame)                                                     #Set background-frame for gameplay
        self.bkg_frame.grid(row = 0, column = 0, rowspan = 2, sticky = 'nsew', padx = 10, pady = 10)    #Position the frame and add padding         
        self.bkg_frame.config(width = 450)                                                              #Set the width of the frame
        self.bkg_frame.config(relief = RIDGE)                                                           #Style the border

        self.dialog_frame = ttk.Frame(self.main_frame)                                                  #Set dialog-frame for gameplay
        self.dialog_frame.grid(row = 0, column = 1, sticky = 'nsew', padx = 10, pady = 10)              #Position the frame and add padding
        self.dialog_frame.config(height = 270, width = 450)                                             #Set height and width of the frame
        self.dialog_frame.config(relief = RIDGE)                                                        #Style the border
        
        self.user_frame = ttk.Frame(self.main_frame)                                                    #Set-user frame for gameplay, user's choices and options will go into this frame
        self.user_frame.grid(row = 1, column = 1, sticky = 'nsew', padx = 10, pady = 10)                #Position the frame and add padding
        self.user_frame.config(height = 270, width = 450)                                               #Set height and width of the frame
        self.user_frame.config(relief = RIDGE)                                                          #Style the border                    

        self.root = master                                  #Save tk object to loal var 
        master.resizable(width = False, height = False)     #Make window not resizable 


    #Method creates the startscreen for the game
    def startMenu(self):
        buttonFont = tkFont.Font(size = 24)                 #Create custom font for buttons
        titleFont = tkFont.Font(size = 30)                  #Create custom font for buttons
        buttonStart = Button(self.main_frame, text = "New Game",command = lambda: self.startGame(),font = buttonFont)  #created button for start screen 
        buttonStart.place(bordermode = OUTSIDE, height = 100, width = 250, relx = 0.30, rely = .20)                     #Set button in place, set dimensions
        buttonCont = Button(self.main_frame, text = "Continue Game",command = lambda: self.loadGame(),font = buttonFont)#create button for load screen
        buttonCont.place(bordermode = OUTSIDE, height = 100, width = 250, relx = 0.30, rely = .45)                      #set button in place, set dimensions
        buttonExit = Button(self.main_frame, text = "Exit Game", font = buttonFont)                                    #create button for game exit
        buttonExit.place(bordermode = OUTSIDE, height = 100, width = 250, relx = 0.30, rely = .70)                      #set button in place, set dimensions 
        title = Label(self.main_frame,text = "Camp Epsilon", font = titleFont)                                         #Create label for title
        title.place(bordermode = OUTSIDE, height = 90, width = 300, relx = 0.20, rely = .007)                           #set label in place and set dimensions
        #soundplayer.updateMusic(placeholder)               #play music on screen

    #Method that creates the load screen for the game. 
    def loadGame(self):
        self.main_frame.pack_forget()                      #Take away frame that holds starts screen stuff from window
        self.loadScreen = Frame(self.root,bg = "black")     #Create new frame that holds stuff for load screen
        self.loadScreen.config(height = 500, width = 500)   #Set dimensions
        self.loadScreen.pack(expand = True,fill = BOTH)     #pack screen into window
        titleFont = tkFont.Font(size = 30)
        buttonFont = tkFont.Font(size = 18)                 #Set font size
        title = Label(self.loadScreen,text = "Save File Menu",font = titleFont,bg = "black",fg = "red")
        title.place(height = 90,width = 300, relx = .35, rely = .007)
        files = []                                          #list that will hold butttons for save files
        counter = 0                                         #used in placing buttons
        ycoord = 100                                        #y coordinate to place buttons
        #saveFiles = userFile.getFileNames()                #Called to get save files 
        names = ["bill","mandy","edd","dora","jimmy"]       #Test list for names. Will delete later
        #names= []
        self.filename =""
        for name in names:                                  #For loop that goes through all file names 
            files.append(Button(self.loadScreen, text = name,font = buttonFont,command = lambda:(self.setfile(name))))#Testing. Will delete later.
            #files.append(Button(self.loadScreen, text = name,font = buttonFont,command = lambda: userFile.loadFile(name)))#Creates buttons that will tell userFile_Handler to load file
            files[counter].place(x = 450, y = ycoord)    #Place button in frame
            counter += 1 #update counter
            ycoord += 60 #update y coordinate
        if(len(files) == 0):
            warning = Label(self.loadScreen,text = "No Saves Availiable",font = titleFont,bg = "black",fg = "red")
            warning.place(height = 90,width  = 500,relx = .25, rely = .30)
        buttonReturn = Button(self.loadScreen, text = "Return to start", command = lambda: self.LoadToStart(),font = buttonFont)#Button to return to start screen
        buttonReturn.place(height = 100, width = 200, x= 400, y = 400)#place button and set dimensions
        buttonLoad = Button(self.loadScreen, text = "Load Game", command = lambda: self.userfile.loadFile(self.filename),font = buttonFont)#Button to load save file 
        buttonLoad.place(height = 100, width = 200, x= 700, y = 400)#place button and set dimensions
        buttonDelete = Button(self.loadScreen, text = "Delete Game", command = lambda: self.userfile.DeleteFile(self.filename),font = buttonFont)#Button to load save file 
        buttonDelete.place(height = 100, width = 200, x= 100, y = 400)#place button and set dimensions

    #Method used to get file name from to pass to user file
    def setfile(self,name):
        self.filename = name    #Set name to variable

    #Method that creates popup window for file name entry. Changes start screen to game screen
    def startGame(self):
        self.main_frame.pack_forget()                                  #Take away frame that holds starts screen stuff from window
        buttonFont = tkFont.Font(size = 15)                             #create custom font for buttons
        self.entry = Toplevel(self.root,height = 250, width = 300)      #Create new window
        self.entry.title("Enter a name")                                #Set title of window. Text thats on top left of window
        self.entry.resizable(height = False, width = False)             #Make window not resizable
        instruct = Label(self.entry,text = "Enter name for save file.") #Create text to instruct player to type name
        instruct.place(x = 0,y = 50)                                    #Place label
        field = Entry(self.entry)                                       #Create entry box for player
        field.place(x = 150,y = 50)                                     #place entry in frame
        confirm = Button(self.entry, text = "Ok", command = (lambda:self.start(field.get())), font  = buttonFont) #create button for player
        confirm.place(x = 125,y = 135)                                  #Set buttons
        buttonReturn = Button(self.entry, text = "Return to Menu", command = (lambda:self.GameToStart(0)), font  = buttonFont)#create button for returning to start screen
        buttonReturn.place(x = 90, y = 185)                             #place button to popup window
        self.gameScreen = Frame(self.root,bg = "black")                 #Create a frame to hold textbox, choice buttons?, and background?
        self.gameScreen.pack(fill = BOTH,expand = True)                 #Pack frame to window
        self.textbox = Frame(self.gameScreen)                           #Create frame that will hold text in the game
        self.textbox.config(height = 500, width = 500)                  #Set dimensions for frame
        self.textbox.pack()                                             #pack frame into gameScreen
        self.scroll = Scrollbar(self.textbox)                           #create scrollbar 
        self.scroll.pack(side = RIGHT, fill = Y)                        #pack scrollbar into window
        self.canvas = Canvas(self.textbox, scrollregion = (0,0,0,1000),height = 400, width = 400, bg = "white",yscrollcommand = self.scroll.set )#create canvas that will hold text. set scrollbar to scroll canvas vertically
        self.canvas.pack(side = LEFT)                                   #pack canvas left side of frame
        self.scroll.config( command = self.canvas.yview)                #set the scrollbar change the canvas
        logo = PhotoImage(file = 'python_logo.gif')
        option = Button(self.gameScreen, text = "Options", command = (lambda:self.optionMenu()), font  = buttonFont,width = 10, height = 5) #create button for options
        #option.config(image = logo, compound = LEFT)
        option.pack()                                                   #pack button into frame
        self.GUI_HandlerBKG("")                                         #Used to 
        a = "I'll come running like Indiana Jones to rescue you!"#Test stuff will delete
        b ="You'll have to find a way to get out of there "#Test stuff will delete
        #self.GUI_HandlerCHC(0,a,0,b)#Test stuff will delete
        
    def start(self,name):
        #files = userFile.getFileNames() #get name of save files
        room = True     #flag if theres room for save files
        dupe = False    #flag if theres already save file with current 
        files = ['billy','edd','mandy','matt'] #test list will delete later
        for names in files:     #for loop tht goes through names. 
            if(names == name):  #If variable name =s one them set flag to true
                dupe = True
                break           #break loop
        if(len(files) == 5):    #if length of list with names = 5 then set room flag to false
            room = False
        if(dupe):   #if the name entry is a already exists as save file. case matters.place warning label
            dupeWarning = Label(self.entry,text = "A file with this name already exists",justify = CENTER)
            dupeWarning.place(x = 50,y = 70)
        if(room == False):#if the max limit of files is reached place warning label.
            roomWarning = Label(self.entry,text = "Max number of save files reached. Please return to Start Menu and go to Load Game to delete a file.",wraplength = 205,justify = CENTER)
            roomWarning.place(x = 50,y = 90)
        if( room and dupe == False):#if both flags don't trip errors
            #self.userFile.saveFile(name)   #create save file
            self.entry.destroy()    #destroy window

    #method for when choice buttons are clicked
    def buttonClick(self,lineNumber):
        #dataFile.CurrentLine = lineNumber  #update currentline
        self.buttonFrame.destroy()         #destroy frame that holds choice buttons

    def optionMenu(self):
        buttonFont = tkFont.Font(size = 15)
        self.options = Toplevel(self.root,height = 250, width = 300)
        self.options.title("Option Menu")
        toggleMUS = Button(self.options, text = "Toggle Music", command = (lambda:self.soundPlayer.toggleMusic()), font  = buttonFont)
        toggleMUS.pack()
        toggleSE = Button(self.options, text = "Toggle Sound Effects", command = (lambda:self.soundPlayer.toggleSFX()), font  = buttonFont)
        toggleSE.pack()
        closeOptions = Button(self.options, text = "Return to Game", command = (lambda:self.options.destroy()), font  = buttonFont)
        closeOptions.pack()
        startMenu = Button(self.options, text = "Return to Menu", command = (lambda:self.GameToStart(1)), font  = buttonFont)
        startMenu.pack()

    #Method to switch load screen to start screen
    def LoadToStart(self):
        self.loadScreen.destroy()   #Destroys loadscreen frame.
        self.main_frame.pack()     #put start screen back into window.

    #Method to move new game to start screen
    def GameToStart(self,window):
        if (window == 0):
            self.entry.destroy()    #destroy window used to get save file name
        else:
            self.options.destroy()  #destroy game option menu
        self.gameScreen.destroy()  #destroy frame holding text box
        self.main_frame.pack() #pack start screen into main window
    

    #method that handles description keyword lines
    #Current bug: Text maybe shown incorrect. Examples: Text maybe overlapped with other text(Max line limit is 2 in size 15 font).
    #Current format for create_text(X coordinate(I think the coordinate is middle of text),Ycoordinate, font color, font, max width of text in pixels,text is centered so that left side is (x,y))
    def GUI_HandlerDSC(self,description):
        DSCfont = tkFont.Font(size = 15)    #create custom font
        self.canvas.create_text(0,self.y,fill = "blue",text = description, font = DSCfont,width = 400,anchor = W)#create text to put onto canvas
        self.y += 50    #update y coordinate for adding text to canvas.

    #method handles npc keyword lines
    #Has same bugs as description does. Create_text format is same too.
    def GUI_HandlerNPC(self,dialouge):
        NPCfont = tkFont.Font(size = 15)
        self.canvas.create_text(0,self.y,fill = "green", text = dialouge, font = NPCfont,width = 400,anchor = W)
        self.y += 50

    #method handles choice keywords lines
    def GUI_HandlerCHC(self,choice):
        CHCfont = tkFont.Font(size = 13)            #Create custom font for choices
        self.buttonFrame = Frame(self.gameScreen)   #Create frame for buttons
        self.buttonFrame.pack(side = BOTTOM)        #place frame on bottom of gamescreen
        buttons = []
        for x in range(0,len(choice.answers)):
            buttons.append(Button(self.buttonFrame,text = choice.answers[x], font = CHCfont,wraplength = 240,command = (lambda: self.buttonClick(choice.results[x]))))

        buttons[0].grid(row = 0, column = 0)        #Place buttons 
        buttons[1].grid(row = 0, column = 1)

    #method for backgrounds
    #Maybe do background frames for left and right of textbox
    #Would require the use of two files for each frame tho.
    def GUI_HandlerBKG(self,background):
        self.bkg_canvas = Canvas(bkg_frame, width = 450, height = 500)      #Set canvas for background
        self.bkg_canvas.pack(expand = YES, fill = BOTH, side = LEFT)        #Pack canvas     
        self.bkg = PhotoImage(file = background)                            #Set background file
        self.bkg_canvas.create_image(0,0, image = self.bkg, anchor = NW)    #Place background on the canvas

    #Method for music keyword lines
    def GUI_HandlerMUS(self,music):
        soundPlayer.updateMusic(music) #Tells soundPlayer to play music

    #Method for sound effect keywords
    def GUI_HandlerSFX(self,sound):
        soundPlayer.playSound(sound)    #Tells soundPlayer to play the sound effect
