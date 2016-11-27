#Version 0.0.9
from Tkinter import *
import tkFont
import ttk
##from soundHandler import soundHandler



class GUI_Manager2:
    ##soundPlayer = soundHandler()    #object for soundHandler. used to play music and sound effects
    y = 50  #y coordinate to place text on canvas

    

    def __init__(self, master = None):
        ## References
        self.main_frame = ttk.Frame(master)                 #Set main frame, the other three smaller frames will go inside the main frame
        self.root = master                                  #Save tk object to loal var 
        self.mainFrameWidth = 1000
        self.mainFrameHeight = 600

        self.bkg_frame = ttk.Frame(self.main_frame)
        self.dialog_frame = ttk.Frame(self.main_frame)
        self.user_frame = ttk.Frame(self.main_frame)   

        ## Main frame
        master.resizable(width = False, height = False)     #Make window not resizable 
        self.main_frame.pack()                              #Pack the main frame into place
        self.main_frame.config(height = self.mainFrameHeight, width = self.mainFrameWidth)  #Set the height and width of the main frame
        self.main_frame.config(relief = RIDGE)              #Style the border
        self.main_frame.config(padding = (15, 15))          #Add padding to main frame
        
    ##Display the start menu    
    def startMenu(self):
        ## Font Setup
        buttonFont = tkFont.Font(size = 24)                 #Create custom font for buttons
        titleFont = tkFont.Font(size = 30)                  #Create custom font for buttons

        ## Setup Title
        title = Label(self.main_frame,text = "Camp Epsilon", font = titleFont)                                               #Create label for title
        title.place(bordermode = OUTSIDE, height = 90, width = 300, relx = 0.375, rely = .007)                           #set label in place and set dimensions

        ## New Game Button
        buttonStart = Button(self.main_frame, text = "New Game",command = lambda: self.startGame(),font = buttonFont)        #created button for start screen 
        buttonStart.place(bordermode = OUTSIDE, height = 100, width = 250, relx = 0.40, rely = .20)                     #Set button in place, set dimensions

        ## Load Game Button
        buttonCont = Button(self.main_frame, text = "Continue Game",command = lambda: self.loadGame(),font = buttonFont)     #create button for load screen
        buttonCont.place(bordermode = OUTSIDE, height = 100, width = 250, relx = 0.40, rely = .45)                      #set button in place, set dimensions

        ## Exit Game Button
        buttonExit = Button(self.main_frame, text = "Exit Game", font = buttonFont)                                          #create button for game exit
        buttonExit.place(bordermode = OUTSIDE, height = 100, width = 250, relx = 0.40, rely = .70)                      #set button in place, set dimensions 

        #soundplayer.updateMusic(placeholder)               #play music on screen
    
    ## Display the game menu
    def gameScreen(self):
        ## Background frame
                                                             #Set background-frame for gameplay
        self.bkg_frame.grid(row = 0, column = 0, rowspan = 2, sticky = 'nsew', padx = 10, pady = 10)    #Position the frame and add padding         
        self.bkg_frame.config(width = 450)                                                              #Set the width of the frame
        self.bkg_frame.config(relief = RIDGE)                                                           #Style the border

        ## Dialogue frame
                                                        #Set dialog-frame for gameplay
        self.dialog_frame.grid(row = 0, column = 1, sticky = 'nsew', padx = 10, pady = 10)              #Position the frame and add padding
        self.dialog_frame.config(height = 270, width = 450)                                             #Set height and width of the frame
        self.dialog_frame.config(relief = RIDGE)                                                        #Style the border
        
        ## User frame
                                                           #Set-user frame for gameplay, user's choices and options will go into this frame
        self.user_frame.grid(row = 1, column = 1, sticky = 'nsew', padx = 10, pady = 10)                #Position the frame and add padding
        self.user_frame.config(height = 270, width = 450)                                               #Set height and width of the frame
        self.user_frame.config(relief = RIDGE)                                                          #Style the border

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
        