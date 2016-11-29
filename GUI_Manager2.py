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

        ## Background frame
        self.bkg_frame = ttk.Frame(self.main_frame)

        ## Dialogue frame
        self.dialog_frame = ttk.Frame(self.main_frame)          #Set dialog-frame for gameplay
        self.dialog_text = Text(self.dialog_frame)
        self.dialog_scroll = Scrollbar(self.dialog_frame)
        self.dialog_yview = 1

        ## Dialogue frame config
        self.dialog_text.config(wrap = WORD)        
        
        ## User Frame
        self.user_frame = ttk.Frame(self.main_frame)                                                    #Set-user frame for gameplay, user's choices and options will go into this frame
        
        ## Main frame
        master.resizable(width = False, height = False)     #Make window not resizable 
        self.main_frame.pack()                              #Pack the main frame into place
        self.main_frame.config(height = self.mainFrameHeight, width = self.mainFrameWidth)  #Set the height and width of the main frame
        self.main_frame.config(relief = RIDGE)              #Style the border
        self.main_frame.config(padding = (15, 15))          #Add padding to main frame
        

    ##Display the start menu    
    def startMenu(self, title, buttonNewGame, buttonContinue, buttonExit):
        ## Font Setup
        buttonFont = tkFont.Font(size = 24)                 #Create custom font for buttons
        titleFont = tkFont.Font(size = 30)                  #Create custom font for buttons

        ## Title
        title.config(text = "Camp Epsilon", font = titleFont)
        title.place(bordermode = OUTSIDE, height = 90, width = 300, relx = 0.375, rely = .007)                           #set label in place and set dimensions

        ## New Game Button
        buttonNewGame.config(text = "New Game", font = buttonFont)        #created button for start screen 
        buttonNewGame.place(bordermode = OUTSIDE, height = 100, width = 250, relx = 0.40, rely = .20)                     #Set button in place, set dimensions

        ## Load Game Button
        buttonContinue.config(text = "Continue Game", font = buttonFont)     #create button for load screen
        buttonContinue.place(bordermode = OUTSIDE, height = 100, width = 250, relx = 0.40, rely = .45)                      #set button in place, set dimensions

        ## Exit Game Button
        buttonExit.config(text = "Exit Game", font = buttonFont)                                          #create button for game exit
        buttonExit.place(bordermode = OUTSIDE, height = 100, width = 250, relx = 0.40, rely = .70)                      #set button in place, set dimensions 

        #soundplayer.updateMusic(placeholder)               #play music on screen
    
    ## Display the game menu
    def gameScreen(self):
        ## Display Background frame
        self.bkg_frame.grid(row = 0, column = 0, rowspan = 2, sticky = 'nsew', padx = 10, pady = 10)    #Position the frame and add padding         
        self.bkg_frame.config(width = 450)                                                              #Set the width of the frame
        self.bkg_frame.config(relief = RIDGE)                                                           #Style the border

        ## Display Dialogue frame
        self.dialog_frame.grid(row = 0, column = 1, sticky = 'nsew', padx = 10, pady = 10)              #Position the frame and add padding
        self.dialog_frame.config(height = 270, width = 450)                                             #Set height and width of the frame
        self.dialog_frame.config(relief = RIDGE)                                                        #Style the border
        self.dialog_text.config(state = DISABLED)

        ## Display User frame
        self.user_frame.grid(row = 1, column = 1, sticky = 'nsew', padx = 10, pady = 10)                #Position the frame and add padding
        self.user_frame.config(height = 270, width = 450)                                               #Set height and width of the frame
        self.user_frame.config(relief = RIDGE)                                                          #Style the border

        self.main_frame.pack()

    #Method that creates popup window for file name entry. Changes start screen to game screen
    def newGame(self, entry, instruction, entryBox, buttonConfirm, buttonReturn):
        ## Set Font
        buttonFont = tkFont.Font(size = 15)                             #create custom font for buttons

        ## Entry Toplevel window
        entry.config(height = 250, width = 300)      #Create new window
        entry.title("Please enter your name:")                                #Set title of window. Text thats on top left of window
        entry.resizable(height = False, width = False)             #Make window not resizable

        ## Player prompt and entry box
        #instruction.config(text = "Enter name for save file.")              #Create text to instruct player to type name
        #instruction.place(x = 0,y = 50)                                     #Place label
        entryBox.place(x = 0,y = 50)                                      #place entry in frame

        ## Confirm button
        buttonConfirm.config(text = "Ok", font  = buttonFont)                   #create button for player
        buttonConfirm.place(x = 125,y = 135)                                    #Set buttons

        ## Return button
        buttonReturn.config(text = "Return to Menu", font  = buttonFont)    #create button for returning to start screen
        buttonReturn.place(x = 90, y = 185)                                 #place button to popup window

    def print_dialogue(self, message):
        ## Set Font
        DSCfont = tkFont.Font(size = 15)

        ## Print to dialogue frame by temporarily enabling then disabling text, update yview
        self.dialog_text.config(state = NORMAL)
        self.dialog_text.insert(END, message)
        self.dialog_yview += 2
        self.dialog_text.yview(self.dialog_yview)
        self.dialog_text.config(state = DISABLED)
        self.dialog_text.pack()

    def print_background(self):
        pass
        
    def display_choice(self, button1, button2, choice1, choice2):
        ## Font Setup
        buttonFont = tkFont.Font(size = 15)

        ## button1
        button1.config(text = choice1, font = buttonFont)
        button1.pack()

        ## button2
        button2.config(text = choice2, font = buttonFont)
        button2.pack()
    
    def hide_choice(self, button1, button2):
        button1.destroy()
        button2.destroy()