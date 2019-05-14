from tkinter import Frame, Entry, Label, Checkbutton

class Setting(Frame):
    
    def __init__(self, parent, newName, newDesc, textInput = True, robotSetting = False, appSetting = True):
        super().__init__(parent)
        self.name = newName
        self.desc = Label(self, text = newDesc)
        self.robotSet = robotSetting
        self.appSet = appSetting
        self.modif = 0
        if(textInput):
            self.modif = Entry(self, width = 30)
        else:
            self.modif = Checkbutton(self)

    def grid(self):
        super().grid(padx = 25, pady = 10)
        self.desc.grid(padx = 10, pady = 10)
        self.modif.grid(padx = 10, pady = 10)

    def apply(self):
        return self.name + ":" + self.modif.get()
