from tkinter import Frame, Entry, Label, Checkbutton

class Setting(Frame):
    
    def __init__(self, parent, newName, newDesc, robotSetting = False, appSetting = True):
        super().__init__(parent)
        self.name = newName
        self.desc = Label(self, text = newDesc)
        self.robotSet = robotSetting
        self.appSet = appSetting
        self.modif = 0
        self.modif = Entry(self, width = 45)

    def grid(self):
        super().grid(padx = 5, pady = 5)
        self.desc.grid(pady = 5)
        self.modif.grid(pady = 5, row = 1)

    def apply(self):
        return self.name + ":" + self.modif.get()
