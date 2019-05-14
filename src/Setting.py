from tkinter import Frame, Entry

class Setting(Frame):
    
    def __init__(self, newName, newDesc, newValue, description, robotSetting = False, appSetting = True):
        self.name = newName
        self.desc = newDesc
        self.robot = robotSetting
        self.value = newValue
        self.desc = description
        self.robotSet = robotSetting
        self.appSet = appSetting
        # how to set modif ?
    
    def apply(self):
        return self.name + ":" + self.value
