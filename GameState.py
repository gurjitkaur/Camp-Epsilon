import StateMachine
import DataFile_Handler
import UserFile_Handler
import Tkinter
import GUI_Manager2
import soundHandler

from time import clock

##===================================================================
## GameState

Char = type ("Char", (object,), {})

class GameState(Char):
    def __init__(self):
        ## Initialize References
        self.StateMachine = StateMachine.StateMachine(self, self)
        self.DataFile = DataFile_Handler.DataFile_Handler("ACT1.txt")

        ## Game Data
        self.choices = []               # List of choices

        ## Set first state to Transition State
        self.StateMachine.setState("TransitionState")

        ## Initialize Tkinter and GUI_Manager
        self.tk = Tkinter.Tk()
        self.GUI_Manager = GUI_Manager2.GUI_Manager2(self.tk)
        self.gameInitialize()
        self.tk.mainloop()

    ## Execute command for State Machine
    def execute(self):
        self.StateMachine.execute()

    ## Initialize the game
    def gameInitialize(self):
        ## Click to start game
        def leftClick_Handler(event):
            ##Unbind the button, clear the message
            self.tk.unbind("<Button-1>")
            message.destroy()
            
            ## Display Start Menu
            self.display_StartMenu()

        ## Bind left click to call leftClick_Handler
        self.tk.bind("<Button-1>", leftClick_Handler)

        ## Place start message
        message = Tkinter.Message(self.tk, text = "Click anywhere to start")
        message.place(bordermode = Tkinter.OUTSIDE, height = self.GUI_Manager.mainFrameHeight, width = self.GUI_Manager.mainFrameWidth)

    def tester_prompt(self):
        print("TEST")

    def click_Handler(self, event):
        self.execute()

    ## Display State Menu
    def display_StartMenu(self):
        print("Start Menu")
        ## Initialize start menu frame
        self.startMenuFrame = Tkinter.Frame(self.GUI_Manager.main_frame)

        ## Setup Title
        title = Tkinter.Label(self.startMenuFrame)

        ## Create Buttons
        buttonNewGame = Tkinter.Button(self.startMenuFrame, command = lambda: self.display_NewGame_Menu())
        buttonContinue = Tkinter.Button(self.startMenuFrame, command = lambda: self.tester_prompt())
        buttonExit = Tkinter.Button(self.startMenuFrame, command = lambda: self.tk.quit())

        self.startMenuFrame.place(bordermode = Tkinter.OUTSIDE, height = self.GUI_Manager.mainFrameHeight, width = self.GUI_Manager.mainFrameWidth)
        
        ## Call GUI_Manager to display buttons
        self.GUI_Manager.startMenu(title, buttonNewGame, buttonContinue, buttonExit)

    ## Hide Start Menu
    def hide_StartMenu(self):
        self.startMenuFrame.place_forget()
    
    ## Display the new game menu
    def display_NewGame_Menu(self):
        print("New Game")
        ## Create Toplevel entry
        entry = Tkinter.Toplevel(self.GUI_Manager.main_frame)

        ## Create player prompt and entry box
        instruction = Tkinter.Label(entry)
        entryBox = Tkinter.Entry(entry)

        ## Confirm button
        buttonConfirm = Tkinter.Button(entry, command = lambda: self.createNewGame(entry, entryBox))

        ## Return button
        buttonReturn = Tkinter.Button(entry, command = lambda: self.tester_prompt())

        ## Call GUI_Manager to display NewGame Menu
        self.GUI_Manager.newGame(entry, instruction, entryBox, buttonConfirm, buttonReturn)

    ## Create a new game when new game option is chosen from start menu
    def createNewGame(self, entry, entryBox):
        ## Get name from entry
        name = entryBox.get()

        ## Call userfile handler to get name
        self.UserFile = UserFile_Handler.UserFile_Handler(name)

        ## Save file
        self.UserFile.saveFile()

        ## Clear the screen
        self.startMenuFrame.place_forget()
        entry.destroy()

        ## Display the gamescreen
        self.display_GameScreen()

        ## Execute State Machine
        self.execute()

    ## Display the gamescreen.
    def display_GameScreen(self):
        print("Game Screen")
        ## Call GUI_Manager to display screen
        self.GUI_Manager.gameScreen()

        ## TESTER: Click to progress game
        self.tk.bind("<Button-1>", self.click_Handler)

    ## DataFile_Handler call
    def callDataFile_Handler(self):
        line = self.DataFile.keyword_Handler()
        self.DataFile.updateLine()
        options = {
            ''      : lambda: None,
            "DSC"   : lambda: self.Keyword_DSC_Handler(line[1]),
            "NPC"   : lambda: self.Keyword_NPC_Handler(line[1]),
            "CHC"   : lambda: self.Keyword_CHC_Handler(self.choices, line[1], line[2]),
            "SFX"   : lambda: self.Keyword_SFX_Handler(line[1]),
            "MUS"   : lambda: self.Keyword_MUS_Handler(line[1]),
            "BKG"   : lambda: self.Keyword_BKG_Handler(line[1]),
            "LIK"   : lambda: self.Keyword_LIK_Handler(),
            "JMP"   : lambda: self.Keyword_JMP_Handler(),
            "FIN"   : lambda: self.Keyword_FIN_Handler(),
            "BRN"   : lambda: self.Keyword_BRN_Handler(),
            "ENC"   : lambda: self.Keyword_ENC_Handler(self.choices)
        }
        
        options[line[0]]()

        return line[0]

    ## DSC Keyword Handler: Call GUI_Manager to print text
    def Keyword_DSC_Handler(self, text):
        print("DSC")
        self.GUI_Manager.print_dialogue(text + '\n')

    ## NPC Keyword Handler: Call GUI_Manager to print text
    def Keyword_NPC_Handler(self, text):
        print("NPC")
        self.GUI_Manager.print_dialogue(text + '\n')

    ## CHC Keyword Handler: Store choice line number and string
    def Keyword_CHC_Handler(self, choices, line, text):
        print("CHC")
        choices.append(line)
        choices.append(text)

    ## ENC Keyword Handler: Call GUI_Manager to configure buttons.
    #                       Wait for user input
    #                       Set transition to wait state
    def Keyword_ENC_Handler(self, choices):
        print("ENC")
        ## Create Choice Buttons
        self.button1 = Tkinter.Button(self.GUI_Manager.user_frame, command = lambda: self.Choice1_Handler(choices[1]))
        self.button2 = Tkinter.Button(self.GUI_Manager.user_frame, command = lambda: self.Choice2_Handler(choices[3]))

        ## Call GUI_Manager to print choices onto buttons
        self.GUI_Manager.display_choice(self.button1, self.button2, choices[1], choices[3])

        ## TESTER: Unbind Left Click Story Progress
        self.tk.unbind("<Button-1>")

    ## Helper to CHC_Handler: Called when button1 is pressed
    #                         Call GUI_Manager to print choices
    #                         Call DataFile_Handler to jump to specific line
    #                         Call Choice clear
    def Choice1_Handler(self, choice):
        self.GUI_Manager.print_dialogue(choice + '\n')
        self.DataFile.setLineNumber(int(self.choices[0]))
        self.Choice_Clear()

    ## Helper to CHC_Handler: Called when button2 is pressed
    def Choice2_Handler(self, choice):
        self.GUI_Manager.print_dialogue(choice + '\n')
        self.DataFile.setLineNumber(int(self.choices[2]))
        self.Choice_Clear()
        
    ## Helper to ENC_Handler: Clear choices, clear buttons
    def Choice_Clear(self):
        ## Clear choices
        self.choices[:] = []

        ## Call GUI_Handler to hide buttons
        self.GUI_Manager.hide_choice(self.button1, self.button2)

        ## TESTER: Rebind left click
        self.tk.bind("<Button-1>", self.click_Handler)

    ## SFX Keyword Handler: Call Sound_Manager to play sound effect
    def Keyword_SFX_Handler(self, text):
        print("SFX")
        pass

    ## MUS Keyword Handler: Call Sound_Manager to loop music
    def Keyword_MUS_Handler(self, text):
        print("MUS")
        pass

    ## BKG Keyword Handler: Call GUI_Manager to display background
    def Keyword_BKG_Handler(self, text):
        print("BKG")
        pass

    ## LIK Keyword Handler: Call UserFile_Handler to update Likeability
    def Keyword_LIK_Handler(self, text):
        print("LIK")
        pass
    
    ## JMP Keyword Handler: Call DataFile_Handler to jump to specific line in file
    def Keyword_JMP_Handler(self):
        print("JMP")
        #self.DataFile.jumpToLine(self.Line[1])
        pass

    ## FIN Keyword Handler: Call UserFile_Handler to save
    ##                      Call DataFile_Handler to open new act
    def Keyword_FIN_Handler(self):
        print("FIN")
        pass

    ## BRN Keyword Handler: Call DataFile_Handler to update branch variable
    #                       0 = decrement
    #                       1 = increment
    def Keyword_BRN_Handler(self):
        print("BRN")
        pass




    #def UserFile_FIN_Handler(self):  #player name, data file, likeability
    #    DataFile.endAct(self.line[1])
    #    act = DataFile.GetAct()
    #    UserFile.updateUser([UserFile.getName(), DataFile.getAct(), UserFile.getLikeabilty()])
    #    UserFile.SaveFile()

if __name__ == '__main__':
    game = GameState()
    #for i in range(0, 20):
    #    startTime = clock()
    #    timeInterval = 0
    #    while(startTime + timeInterval > clock()):
    #        pass
    #    game.execute()
