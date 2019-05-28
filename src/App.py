from tkinter import Tk, Button, Label
from View import View, ImageView, ControlsView
from Logger import Logger
from NetControls import NetControls
from NetCamera import NetCamera
from SettingSaver import SettingSaver
from Setting import Setting

#Classe controlleur gérant l'ensemble de l'application
class App:
    
    def __init__(self):
        self.window = Tk()
        self.previousLog = "" #Dernier log enregistré
        #Liste des quatres vues formant l'interface de l'application
        self.views = {"image": ImageView(self.window, width = 850, height = 650, rowspan = 2, columnspan = 2), 
            "controls": ControlsView(self.window, column = 2), 
            "settings": View(self.window, height = 450, column = 2, row = 1, text = "Paramètres", rowspan = 2),
            "log": View(self.window, height = 250, width = 850, column = 0, row = 2, text = "Logs", columnspan = 2)}
        #Mise en place des mécanismes pour faire avancer le robot
        self.views["controls"].content.append(Button(self.views["controls"], bitmap = "@img/ArrowUP.xbm", height = 70, width = 70)) #Ajout du bouton aux contrôles
        self.views["controls"].content[0].bind('<1>', self.pilotUp) #Liaison du clic de la souris avec l'action d'avancer
        self.views["controls"].content[0].bind('<ButtonRelease-1>', self.pilotIdle) #Liaison du relâchement du clic de la souris avec l'arrêt du robot
        self.views["controls"].content[0].bind_all('<KeyPress-Up>', self.pilotUp) #Liaison de l'enfoncement de la touche haut avec l'action d'avancer
        self.views["controls"].content[0].bind_all('<KeyRelease-Up>', self.pilotIdle) #liaison du relâchement de la touche haut avec l'arrêt du robot
        #Mise en place des mécanismes pour faire tourner le robot à gauche
        self.views["controls"].content.append(Button(self.views["controls"], bitmap = "@img/ArrowLEFT.xbm", height = 70, width = 70))
        self.views["controls"].content[1].bind('<1>', self.pilotLeft)
        self.views["controls"].content[1].bind('<ButtonRelease-1>', self.pilotIdle)
        self.views["controls"].content[1].bind_all('<KeyPress-Left>', self.pilotLeft)
        self.views["controls"].content[1].bind_all('<KeyRelease-Left>', self.pilotIdle)
        #Mise en place des mécanismes pour prendre une photo
        self.views["controls"].content.append(Button(self.views["controls"], bitmap = "@img/Camera.xbm", height = 70, width = 70))
        self.views["controls"].content[2].bind('<ButtonRelease-1>', self.camera)
        #Mise en place des mécanismes pour faire tourner le robot à droite
        self.views["controls"].content.append(Button(self.views["controls"], bitmap = "@img/ArrowRIGHT.xbm", height = 70, width = 70))
        self.views["controls"].content[3].bind('<1>', self.pilotRight)
        self.views["controls"].content[3].bind('<ButtonRelease-1>', self.pilotIdle)
        self.views["controls"].content[3].bind_all('<KeyPress-Right>', self.pilotRight)
        self.views["controls"].content[3].bind_all('<KeyRelease-Right>', self.pilotIdle)
        #Mise en place des mécanismes pour faire reculer le robot
        self.views["controls"].content.append(Button(self.views["controls"], bitmap = "@img/ArrowDOWN.xbm", height = 70, width = 70))
        self.views["controls"].content[4].bind('<1>', self.pilotDown)
        self.views["controls"].content[4].bind('<ButtonRelease-1>', self.pilotIdle)
        self.views["controls"].content[4].bind_all('<KeyPress-Down>', self.pilotDown)
        self.views["controls"].content[4].bind_all('<KeyRelease-Down>', self.pilotIdle)
        self.views["controls"].empty = [0, 2, 6, 8] #Les cellules dans les coins sont vides
        self.views["controls"].display()
        self.views["image"].display()
        self.views["settings"].content.append(Setting(self.views["settings"], "host", "Adresse hôte")) #Ajout du paramètre de l'adresse d'hôte à la vue des paramètres
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
        #Separation ordonnée des paramètres en nom et valeur
        for line in lines:
            setting = line.split(":")
            setName.append(setting[0])
            setVal.append(setting[1].strip("\n"))
        #Création des classes utiles
        self.history = Logger()
        self.robotCtrl = NetControls(setVal[setName.index("host")])
        self.robotCam = NetCamera(host = setVal[setName.index("host")], robotPath = setVal[setName.index("robotImageDir")], localPath = setVal[setName.index("appImageDir")])
        self.config = SettingSaver(host = setVal[setName.index("host")])
        self.window.title("PilotApp by Anthony Jaccard") #Modification du nom de la fenêtre
        self.window.mainloop() #Démarrage du programme
    
    #Méthode de callback pour faire avancer le robot
    def pilotUp(self, event): #l'argument event est donné par tkinter et est donc obligatoire
        self.robotCtrl.directionY = 1
        self.pilot()
        self.log("Piloting robot forward")
    
    #Méthode de callback pour faire reculer le robot
    def pilotDown(self, event):
        self.robotCtrl.directionY = -1
        self.pilot()
        self.log("Piloting robot backward")
    
    #Méthode de callback pour faire tourner le robot à gauche
    def pilotLeft(self, event):
        self.robotCtrl.directionX = -1
        self.pilot()
        self.log("Piloting robot left")

    #Méthode de callback pour faire tourner le robot à gauche
    def pilotRight(self, event):
        self.robotCtrl.directionX = 1
        self.pilot()
        self.log("Piloting robot right")
    
    #Méthode de callback pour faire s'arrêter le robot
    def pilotIdle(self, event):
        self.robotCtrl.directionX = 0
        self.robotCtrl.directionY = 0
        self.pilot()
        self.log("Robot stopped")
    
    #Méthode envoyant l'ordre au robot de se déplacer
    def pilot(self):
        conStatus = self.robotCtrl.pilot() #Envoi de l'ordre de déplacement
        self.views["controls"].setConState(conStatus == 0) #On modifie la couleur du fond de la vue en fonction de l'état de la connexion avec le robot
    
    #Méthode mettant à jour l'affichage de l'image
    def image(self, imageName):
        self.views["image"].refreshImage(imageName)
        self.log("New Image: " + imageName)
    
    #Méthode de callback qui prend une photo et la récupère
    def camera(self, event):
        if(self.robotCam.snap()): #Envoie l'ordre de prendre la photo
            self.history.log("Error: unable to take picture")
        else:
            imageNum = self.robotCam.getImage() #Récupère la photo
            if(imageNum == 0):
                print("ERROR")
                self.history.log("Error: unable to take picture")
            else:
                self.image("img%d.gif" % imageNum)

    #Méthode de callback 
    def apply(self):
        appSetContent = "" #Futur contenu du fichier de configuration de l'app
        robotSetContent = "" #Futur contenu du fichier de configuration du robot
        for setting in self.views["settings"].content[:-1]: #On récupère le paramètre sous forme de texte dans la variable correspondant au type de paramètre 
            if(setting.appSet):
                appSetContent += setting.apply() + "\n"
            if(setting.robotSet):
                robotSetContent += setting.apply() + "\n"
        self.log("Save app settings: " + appSetContent.replace("\n", ", "))
        self.log("Save robot settings: " + robotSetContent.replace("\n", ", "))
        self.log("New settings saved: relaunch app to apply them")
        self.config.appSet(appSetContent) #On enregistre la configuration dans le fichier de configuration de l'app
        self.config.robotSet(robotSetContent) #On envoie la configuration au robot
    
    #Méthode d'affichage et d'enregistrement des log
    def log(self, content):
        if(len(self.views["log"].content) >= 8): #Au maximum 8 log peuvent être affichés
            self.views["log"].content[0].grid_forget()
            self.views["log"].content.pop(0)
            self.views["log"].display()
        if(self.previousLog != content): #On n'enregistre de nouveau log que s'il est différent du log précédent
            self.views["log"].content.append(Label(self.views["log"], text = content,  width = 100, anchor = "nw", bg = "#CCC"))
            self.views["log"].display()
            self.history.log(content + "\n")
            self.previousLog = content
