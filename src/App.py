from tkinter import Tk, Button, Label
from View import View, ImageView, ControlsView
from Logger import Logger
from NetControls import NetControls
from NetCamera import NetCamera
from SettingSaver import SettingSaver
from Setting import Setting

class App:
    
    def __init__(self):
        self.window = Tk()
        self.previousLog = ""
        self.views = {"image": ImageView(self.window, width = 850, height = 650, rowspan = 2, columnspan = 2), 
            "controls": ControlsView(self.window, column = 2), 
            "settings": View(self.window, height = 450, column = 2, row = 1, text = "Paramètres", rowspan = 2),
            "log": View(self.window, height = 250, width = 850, column = 0, row = 2, text = "Logs", columnspan = 2)}
        self.views["controls"].content.append(Button(self.views["controls"], bitmap = "@img/ArrowUP.xbm", height = 70, width = 70))
        self.views["controls"].content[0].bind('<1>', self.pilotUp)
        self.views["controls"].content[0].bind('<ButtonRelease-1>', self.pilotIdle)
        self.views["controls"].content[0].bind_all('<KeyPress-Up>', self.pilotUp)
        self.views["controls"].content[0].bind_all('<KeyRelease-Up>', self.pilotIdle)
        self.views["controls"].content.append(Button(self.views["controls"], bitmap = "@img/ArrowLEFT.xbm", height = 70, width = 70))
        self.views["controls"].content[1].bind('<1>', self.pilotLeft)
        self.views["controls"].content[1].bind('<ButtonRelease-1>', self.pilotIdle)
        self.views["controls"].content[1].bind_all('<KeyPress-Left>', self.pilotLeft)
        self.views["controls"].content[1].bind_all('<KeyRelease-Left>', self.pilotIdle)
        self.views["controls"].content.append(Button(self.views["controls"], bitmap = "@img/Camera.xbm", height = 70, width = 70))
        #self.views["controls"].content[2].bind('<ButtonRelease-1>', self.camera)
        self.views["controls"].content.append(Button(self.views["controls"], bitmap = "@img/ArrowRIGHT.xbm", height = 70, width = 70))
        self.views["controls"].content[3].bind('<1>', self.pilotRight)
        self.views["controls"].content[3].bind('<ButtonRelease-1>', self.pilotIdle)
        self.views["controls"].content[3].bind_all('<KeyPress-Right>', self.pilotRight)
        self.views["controls"].content[3].bind_all('<KeyRelease-Right>', self.pilotIdle)
        self.views["controls"].content.append(Button(self.views["controls"], bitmap = "@img/ArrowDOWN.xbm", height = 70, width = 70))
        self.views["controls"].content[4].bind('<1>', self.pilotDown)
        self.views["controls"].content[4].bind('<ButtonRelease-1>', self.pilotIdle)
        self.views["controls"].content[4].bind_all('<KeyPress-Down>', self.pilotDown)
        self.views["controls"].content[4].bind_all('<KeyRelease-Down>', self.pilotIdle)
        self.views["controls"].empty = [0, 2, 6, 8]
        self.views["controls"].display()
        self.views["image"].display()
        self.views["settings"].content.append(Setting(self.views["settings"], "host", "Adresse hôte"))
        self.views["settings"].content.append(Setting(self.views["settings"], "appImageDir", "Répertoire images App"))
        self.views["settings"].content.append(Setting(self.views["settings"], "robotImageDir", "Répertoire images robot", robotSetting = True))
        self.views["settings"].content.append(Setting(self.views["settings"], "imageResolution", "Resolution image (WxH)", robotSetting = True, appSetting = False))
        self.views["settings"].content.append(Button(self.views["settings"], text = "Appliquer", command = self.apply))
        self.views["settings"].display()
        self.views["log"].content.append(Label(self.views["log"], width = 100, text = "App load", anchor = "nw", bg = "#CCC"))
        self.views["log"].display()
        #auto configuration
        conf = open("app/app.conf")
        lines = conf.readlines()
        setName = []
        setVal = []
        for line in lines:
            setting = line.split(":")
            setName.append(setting[0])
            setVal.append(setting[1].strip("\n"))
        self.history = Logger()
        self.robotCtrl = NetControls(setVal[setName.index("host")])
        self.robotCam = NetCamera(host = setVal[setName.index("host")], robotPath = setVal[setName.index("robotImageDir")], localPath = setVal[setName.index("appImageDir")])
        self.config = SettingSaver(host = setVal[setName.index("host")])
        self.window.title("PilotApp by Anthony Jaccard")
        self.window.mainloop()
    
    def pilotUp(self, event): #event given by tkinter thus mandatory
        self.robotCtrl.directionY = 1
        self.pilot()
        self.log("Piloting robot forward")
    
    def pilotDown(self, event):
        self.robotCtrl.directionY = -1
        self.pilot()
        self.log("Piloting robot backward")
    
    def pilotLeft(self, event):
        self.robotCtrl.directionX = -1
        self.pilot()
        self.log("Piloting robot left")

    def pilotRight(self, event):
        self.robotCtrl.directionX = 1
        self.pilot()
        self.log("Piloting robot right")
    
    def pilotIdle(self, event):
        self.robotCtrl.directionX = 0
        self.robotCtrl.directionY = 0
        self.pilot()
        self.log("Robot stopped")
    
    def pilot(self):
        conStatus = self.robotCtrl.pilot()
        self.views["controls"].setConState(conStatus == 0)
    
    def image(self, imageName):
        self.views["image"].refreshImage(imageName)
        self.log("New Image: " + imageName)
    
    def camera(self, event):
        imageNum = self.robotCam.snap()
        if(imageNum < 0):
            self.history.log("Error: unable to take picture")
        else:
            self.image("img" + imageNum + ".png")

    
    def apply(self):
        appSetContent = ""
        robotSetContent = ""
        for setting in self.views["settings"].content[:-1]:
            if(setting.appSet):
                appSetContent += setting.apply() + "\n"
            if(setting.robotSet):
                robotSetContent += setting.apply() + "\n"
        self.log("Save app settings: " + appSetContent.replace("\n", ", "))
        self.log("Save robot settings: " + robotSetContent.replace("\n", ", "))
        self.log("New settings saved: relaunch app to apply them")
        self.config.appSet(appSetContent)
        self.config.robotSet(robotSetContent)
    
    def log(self, content):
        if(len(self.views["log"].content) >= 8):
            self.views["log"].content[0].grid_forget()
            self.views["log"].content.pop(0)
            self.views["log"].display()
        if(self.previousLog != content):
            self.views["log"].content.append(Label(self.views["log"], text = content,  width = 100, anchor = "nw", bg = "#CCC"))
            self.views["log"].display()
            self.history.log(content + "\n")
            self.previousLog = content
