from tkinter import Tk, LabelFrame, Label, Button, PhotoImage, Canvas

#Classe basique permettant d'afficher dans une région de la fenêtre des labels organisés verticalement

class View(LabelFrame):

    def __init__(self, parent, width = 350, height = 350, column = 0, row = 0, text = "View", rowspan = 1, columnspan = 1):
        super().__init__(parent, width = width, height = height, bg = "#CCC", bd = 5, padx = 25, pady = 25, relief = "sunken", text = text)
        self.grid_propagate(0) #La vue ne modifie pas sa taille pour englober son contenu
        self.grid(column = column, row = row, padx = 10, pady = 10, rowspan = rowspan, columnspan = columnspan, sticky = "n")
        self.content = [] #La liste des widgets contenus dans cette vue

    def display(self): #Méthode pour l'affichage du contenu
        for item in self.content:
            item.grid()

#Type de vue permettant d'afficher une image et de la modifier en cours d'exécution

class ImageView(View):

    def __init__(self, parent, width = 850, height = 650, column = 0, row = 0, imageFolder = "app/images/", text = "Images", rowspan = 1, columnspan = 1):
        super().__init__(parent = parent, width = width, height = height, column = column, row = row, text = text, rowspan = rowspan, columnspan = columnspan)
        self.imageDir = imageFolder #Dossier dans lequel aller chercher les images
        self.img = 0 #Image affichée dans le canvas. Une référence à l'image doit être conservée autrement l'image est détruite par le ramasse-miette
        self.isImageSet = False #Définit si une image peut-être affichée ou s'il faut afficher les instructions
        self.content = {"default":Label(self, text = "Aucune image à afficher pour le moment. Cliquez sur le bouton caméra ou appuyez sur la barre espace pour prendre une photo et l'afficher ici"),
            "image":Canvas(self, width = 800, height = 600)} #Par défaut, la classe contient un label indiquant les instructions pour prendre une image et un canvas pour y dessiner les images

    #Modifie l'image à afficher
    
    def refreshImage(self, imagePath):
        self.isImageSet = True
        self.img = PhotoImage(file = self.imageDir + imagePath)
        self.content["image"].create_image(0, 0, anchor = "nw", image = self.img)
        self.display()
    
    def display(self):
        #Si aucune image n'est configurée, on affiche les instructions, sinon on affiche l'image
        if(self.isImageSet):
            self.content["default"].grid_remove()
            self.content["image"].grid()
        else:
            self.content["default"].grid()

#Vue acueillant des contrôles pour le robot et pouvant les afficher dans une grille en laissant vide les cases définies comme telles

class ControlsView(View):

    def __init__(self, parent, width = 350, height = 350, column = 0, row = 0, cCtrl = 3, rCtrl = 3, text = "Contrôles", rowspan = 1, columnspan = 1):
        super().__init__(parent = parent, width = width, height = height, column = column, row = row, text = text, rowspan = rowspan, columnspan = columnspan)
        self.columns = cCtrl #Nombre de colonnes pour l'affichage
        self.rows = rCtrl #Nombre de rangs pour l'affichage
        self.empty = [] #Liste des cases à laisser vide définies par leur index
    
    def display(self):
        buttonIndex = 0 #Prochain contrôle à afficher
        cellIndex = 0 #Indice de la case
        for y in range(self.rows):
            for x in range(self.columns):
                if cellIndex in self.empty:
                    cellIndex += 1
                else:
                    self.content[buttonIndex].grid(column = x, row = y, padx = 10, pady = 10)
                    cellIndex += 1
                    buttonIndex += 1

    
    def setConState(self, state): #Change la couleur de fond de la vue
        if(state):
            self.config(bg = "#070")
        else:
            self.config(bg = "#700")
