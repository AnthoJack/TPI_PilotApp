from tkinter import Frame, Entry, Label

#Classe représentant les paramètres à modifier
class Setting(Frame):
    
    def __init__(self, parent, newName, newDesc, robotSetting = False, appSetting = True):
        super().__init__(parent)
        self.name = newName #Nom du paramètre qui sera enregistré dans le fichier
        self.desc = Label(self, text = newDesc) #Nom du paramètre tel qu'il sera présenté à l'utilisateur
        self.robotSet = robotSetting #Définit s'il s'agit d'un paramètre à enregistrer sur le robot
        self.appSet = appSetting #Définit s'il s'agit d'un paramètre à enregistrer sur l'ordinateur
        self.modif = Entry(self, width = 45)

    def grid(self):
        super().grid(padx = 5, pady = 5)
        self.desc.grid(pady = 5)
        self.modif.grid(pady = 5, row = 1)

    #Retourne le paramètre de la façon dont il sera enregistré dans le fichier de configuration
    def apply(self):
        return self.name + ":" + self.modif.get()
