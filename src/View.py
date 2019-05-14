from tkinter import Tk, LabelFrame, Label, Button, PhotoImage, Canvas

class View(LabelFrame):

    def __init__(self, parent, width = 350, height = 350, column = 0, row = 0, rowspan = 1, text = "View"):
        super().__init__(parent, width = width, height = height, bg = "#CCC", bd = 5, padx = 25, pady = 25, relief = "sunken", text = text)
        self.grid_propagate(0)
        self.grid(column = column, row = row, padx = 10, pady = 10, rowspan = rowspan)
        self.content = []

    def display(self):
        for item in self.content:
            item.grid()

class ImageView(View):

    def __init__(self, parent, width = 850, height = 850, column = 0, row = 0, imageFolder = "C:\\RobotTemp\\images\\", text = "Images"):
        super().__init__(parent = parent, width = width, height = height, column = column, row = row, rowspan = 2, text = text)
        self.imageDir = imageFolder
        self.content = {"default":Label(self, width = 100, text = "Aucune image à afficher pour le moment. Instructions"),
            "image":Canvas(self)}

    def refreshImage(self, imagePath):
        self.content["image"].create_image(0, 0, anchor = "nw", image = PhotoImage(file = self.imageDir + imagePath))
        self.display()
    
    def display(self):
        self.content["default"].grid()

class ControlsView(View):

    def __init__(self, parent, width = 350, height = 350, column = 0, row = 0, cCtrl = 3, rCtrl = 3, text = "Contrôles"):
        super().__init__(parent = parent, width = width, height = height, column = column, row = row, text = text)
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
