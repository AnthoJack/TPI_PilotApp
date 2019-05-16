from tkinter import Tk, Button
from View import View, ImageView, ControlsView
from Logger import Logger
from NetControls import NetControls
from NetCamera import NetCamera
from SettingSaver import SettingSaver
from Setting import Setting

class App:
    
    def __init__(self):
        self.window = Tk()
        self.views = {"image": ImageView(self.window, width = 850, height = 850), 
            "controls": ControlsView(self.window, column = 1), 
            "settings": View(self.window, height = 450, column = 1, row = 1, text = "Paramètres")}
        self.views["controls"].content.append(Button(self.views["controls"], bitmap = "@img/ArrowUP.xbm", height = 60, width = 60))
        self.views["controls"].content[0].bind('<1>', self.pilotUp)
        self.views["controls"].content[0].bind('<ButtonRelease-1>', self.pilotIdle)
        self.views["controls"].content.append(Button(self.views["controls"], bitmap = "@img/ArrowLEFT.xbm", height = 60, width = 60))
        self.views["controls"].content[1].bind('<1>', self.pilotLeft)
        self.views["controls"].content[1].bind('<ButtonRelease-1>', self.pilotIdle)
        self.views["controls"].content.append(Button(self.views["controls"], bitmap = "@img/Camera.xbm", height = 60, width = 60))
        self.views["controls"].content[2].bind('<ButtonRelease-1>', self.camera)
        self.views["controls"].content.append(Button(self.views["controls"], bitmap = "@img/ArrowRIGHT.xbm", height = 60, width = 60))
        self.views["controls"].content[3].bind('<1>', self.pilotRight)
        self.views["controls"].content[3].bind('<ButtonRelease-1>', self.pilotIdle)
        self.views["controls"].content.append(Button(self.views["controls"], bitmap = "@img/ArrowDOWN.xbm", height = 60, width = 60))
        self.views["controls"].content[4].bind('<1>', self.pilotDown)
        self.views["controls"].content[4].bind('<ButtonRelease-1>', self.pilotIdle)
        self.views["controls"].empty = [0, 2, 6, 8]
        self.views["controls"].display()
        self.views["image"].display()
        self.views["settings"].content.append(Setting(self.views["settings"], "saveImages", "Sauver images", False))
        self.views["settings"].content.append(Setting(self.views["settings"], "imageDir", "Répertoire images"))
        self.views["settings"].content.append(Setting(self.views["settings"], "imageResolution", "Resolution image", robotSetting = True, appSetting = False))
        self.views["settings"].content.append(Button(self.views["settings"], text = "Appliquer"))
        self.views["settings"].display()
        # get config from file
        self.history = Logger()
        self.robotCtrl = NetControls()
        self.robotCam = NetCamera()
        self.config = SettingSaver()
        self.window.title("PilotApp by Anthony Jaccard")
        self.window.mainloop()
    
    def pilotUp(self, event):
        self.robotCtrl.directionY = 1
        self.robotCtrl.pilot()
    
    def pilotDown(self, event):
        self.robotCtrl.directionY = -1
        self.robotCtrl.pilot()
    
    def pilotLeft(self, event):
        self.robotCtrl.directionX = -1
        self.robotCtrl.pilot()

    def pilotRight(self, event):
        self.robotCtrl.directionX = 1
        self.robotCtrl.pilot()
    
    def pilotIdle(self, event):
        self.robotCtrl.directionX = 0
        self.robotCtrl.directionY = 0
        self.robotCtrl.pilot()
    
    def image(self, event):
        pass
    
    def camera(self, event):
        pass
    
    def apply(self, event):
        pass