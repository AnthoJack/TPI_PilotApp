from tkinter import Tk, Button
from View import View, ImageView, ControlsView
from Logger import Logger
from NetControls import NetControls
from NetCamera import NetCamera
from SettingSaver import SettingSaver

class App:
    
    def __init__(self):
        self.window = Tk()
        self.views = {"image": ImageView(self.window, width = 850, height = 850), 
            "controls": ControlsView(self.window, column = 1), 
            "settings": View(self.window, height = 450, column = 1, row = 1, text = "Paramètres")}
        self.views["controls"].content.append(Button(self.views["controls"], text = "UP"))
        self.views["controls"].content.append(Button(self.views["controls"], text = "LEFT"))
        self.views["controls"].content.append(Button(self.views["controls"], text = "CAMERA"))
        self.views["controls"].content.append(Button(self.views["controls"], text = "RIGHT"))
        self.views["controls"].content.append(Button(self.views["controls"], text = "DOWN"))
        self.views["controls"].empty = [0, 2, 6, 8]
        self.views["controls"].display()
        # get config from file
        self.history = Logger()
        self.robotCtrl = NetControls()
        self.robotCam = NetCamera()
        self.config = SettingSaver()
        self.window.title("PilotApp by Anthony Jaccard")
        self.window.mainloop()
    
    def pilot(self, type):
        pass
    
    def image(self, path):
        pass
    
    def camera(self):
        pass
    
    def apply(self):
        pass