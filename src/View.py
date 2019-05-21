from tkinter import Tk, LabelFrame, Label, Button, PhotoImage, Canvas

class View(LabelFrame):

    def __init__(self, parent, width = 350, height = 350, column = 0, row = 0, text = "View", rowspan = 1, columnspan = 1):
        super().__init__(parent, width = width, height = height, bg = "#CCC", bd = 5, padx = 25, pady = 25, relief = "sunken", text = text)
        self.grid_propagate(0)
        self.grid(column = column, row = row, padx = 10, pady = 10, rowspan = rowspan, columnspan = columnspan, sticky = "n")
        self.content = []

    def display(self):
        for item in self.content:
            item.grid()

class ImageView(View):

    def __init__(self, parent, width = 850, height = 650, column = 0, row = 0, imageFolder = "~/PilotAppTemp/images", text = "Images", rowspan = 1, columnspan = 1):
        super().__init__(parent = parent, width = width, height = height, column = column, row = row, text = text, rowspan = rowspan, columnspan = columnspan)
        self.imageDir = imageFolder
        self.isImageSet = False
        self.content = {"default":Label(self, text = "Aucune image à afficher pour le moment. Cliquez sur le bouton caméra ou appuyez sur la barre espace pour prendre une photo et l'afficher ici"),
            "image":Canvas(self)}

    def refreshImage(self, imagePath):
        self.isImageSet = True
        self.content["image"].create_image(0, 0, anchor = "nw", image = PhotoImage(file = self.imageDir + imagePath))
        self.display()
    
    def display(self):
        if(self.isImageSet):
            self.content["image"].grid()
        else:
            self.content["default"].grid()

class ControlsView(View):

    def __init__(self, parent, width = 350, height = 350, column = 0, row = 0, cCtrl = 3, rCtrl = 3, text = "Contrôles", rowspan = 1, columnspan = 1):
        super().__init__(parent = parent, width = width, height = height, column = column, row = row, text = text, rowspan = rowspan, columnspan = columnspan)
        self.columns = cCtrl
        self.rows = rCtrl
        self.empty = []
    
    def display(self):
        buttonIndex = 0
        cellIndex = 0
        for y in range(self.rows):
            for x in range(self.columns):
                if cellIndex in self.empty:
                    cellIndex += 1
                else:
                    self.content[buttonIndex].grid(column = x, row = y, padx = 10, pady = 10)
                    cellIndex += 1
                    buttonIndex += 1

    
    def setConState(self, state):
        if(state):
            self.config(bg = "#070")
        else:
            self.config(bg = "#700")
