import StateMachine
import DataFile_Handler
import UserFile_Handler
import Tkinter
import GUI_Manager2

from time import clock

##===================================================================
## GameState

Char = type ("Char", (object,), {})

class GameState(Char):
    def __init__(self):
        ## Initialize References
        self.StateMachine = StateMachine.StateMachine(self, self)
        self.DataFile = DataFile_Handler.DataFile_Handler("ACT1.txt")
        self.line = ""

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
        ## Click to start game screen, unbind left click
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
        print("EXECUTE")
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

    def hide_StartMenu(self):
        self.startMenuFrame.place_forget()
    
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

    def display_GameScreen(self):
        print("Game Screen")
        self.GUI_Manager.gameScreen()
        self.tk.bind("<Button-1>", self.click_Handler)

    def callDataFile_Handler(self):
        line = self.DataFile.keyword_Handler()
        self.DataFile.updateLine()
        options = {
            ''      : lambda: None,
            "DSC"   : lambda: self.DataFile_DSC_Handler(line[1]),
            "NPC"   : lambda: self.DataFile_NPC_Handler(line[1]),
            "CHC"   : lambda: self.DataFile_CHC_Handler(line[1]),
            "SFX"   : lambda: self.DataFile_SFX_Handler(line[1]),
            "MUS"   : lambda: self.DataFile_MUS_Handler(line[1]),
            "BKG"   : lambda: self.DataFile_BKG_Handler(line[1]),
            "LIK"   : lambda: self.DataFile_LIK_Handler(),
            "JMP"   : lambda: self.DataFile_JMP_Handler(),
            "FIN"   : lambda: self.DataFile_FIN_Handler(),
            "BRN"   : lambda: self.DataFile_BRN_Handler(),
            "ENC"   : lambda: self.DataFile_ENC_Handler()
        }
        
        options[line[0]]()

    def DataFile_DSC_Handler(self, text):
        print("DSC")
        self.GUI_Manager.print_dialogue(text)

    def DataFile_NPC_Handler(self, text):
        print("NPC")
        self.GUI_Manager.print_dialogue(text)
        #self.GUI_Manager.printNPC(self.Line[1])

    def DataFile_CHC_Handler(self, text):
        #self.GUI_Manager.addChoices(self.Line[1], self.Line[2], self.Line[4], self.Line[5])
        pass

    def DataFile_SFX_Handler(self, text):
        pass

    def DataFile_MUS_Handler(self, text):
        pass

    def DataFile_BKG_Handler(self, text):
        pass

    def DataFile_LIK_Handler(self, text):
        pass
        
    def DataFile_JMP_Handler(self):
        #self.DataFile.jumpToLine(self.Line[1])
        pass

    def DataFile_FIN_Handler(self):
        pass

    def DataFile_BRN_Handler(self):
        pass

    def DataFile_ENC_Handler(self):
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
