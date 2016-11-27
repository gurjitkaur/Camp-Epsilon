import StateMachine
import DataFile_Handler
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
        self.Line = ""

        ## Set States
        self.StateMachine.addState("StartState", StateMachine.StartState(self.StateMachine))
        self.StateMachine.addState("TransitionState", StateMachine.TransitionState(self.StateMachine))
        self.StateMachine.addState("ReadState", StateMachine.ReadState(self.StateMachine))
        self.StateMachine.addState("WaitState", StateMachine.WaitState(self.StateMachine))

        ## Set Transitions
        self.StateMachine.addTransition("toStartState", StateMachine.StateTransition("StartState"))
        self.StateMachine.addTransition("toTransitionState", StateMachine.StateTransition("TransitionState"))
        self.StateMachine.addTransition("toReadState", StateMachine.StateTransition("ReadState"))
        self.StateMachine.addTransition("toWaitState", StateMachine.StateTransition("WaitState"))

        ## Set first state to Transition State
        self.StateMachine.setState("StartState")

        ## Initialize Tkinter and GUI_Manager
        self.tk = Tkinter.Tk()
        self.GUI_Manager = GUI_Manager2.GUI_Manager2(self.tk)
        self.gameInitialize()
        #self.GUI_Manager.startMenu()
        self.tk.mainloop()

        ## Initialize the game
    def gameInitialize(self):
        ## Click to start game screen, unbind left click
        def leftClick_Handler(event):
            #self.tk.unbind("<Button-1>")
            #self.execute()
            print("LEFT")

        ## Bind left click to call leftClick_Handler
        self.tk.bind("<Button-1>", leftClick_Handler)

        ## Place start message
        message = Tkinter.Message(self.tk, text = "Click anywhere to start")
        message.place(bordermode = Tkinter.OUTSIDE, height = 100, width = 250, relx = 0.30, rely = .45)

    ## Execute command for State Machine
    def execute(self):
        self.StateMachine.execute()

    def Display_Start_Menu(self):
        #self.GUI_Manager.Display_Start_Menu()

        pass

    def callDataFile_Handler(self):
        self.Line = self.DataFile.keyword_Handler()
        #if(isinstance(self.Line, list)):
        #    self.Keyword = self.Line[0]
        #print(type(self.Line))
        self.DataFile.updateLine()
        print (self.Line)

    def DataFile_Empty_Handler(self):
        self.DataFile.updateLine()

    def DataFile_DSC_Handler(self):
        self.DataFile.updateLine()
        #self.GUI_Manager.printDSC(self.Line[1])

    def DataFile_NPC_Handler(self):
        self.DataFile.updateLine()
        #self.GUI_Manager.printNPC(self.Line[1])

    def DataFile_CHC_Handler(self):
        #self.GUI_Manager.addChoices(self.Line[1], self.Line[2], self.Line[4], self.Line[5])
        pass

    def DataFile_SFX_Handler(self):
        pass

    def DataFile_MUS_Handler(self):
        pass

    def DataFile_BKG_Handler(self):
        pass

    def DataFile_LIK_Handler(self):
        pass
        
    def DataFile_JMP_Handler(self):
        self.DataFile.jumpToLine(self.Line[1])

    def DataFile_FIN_Handler():
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
