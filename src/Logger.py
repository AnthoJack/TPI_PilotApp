#Classe gérant l'enregistrement des log dans un fichier
class Logger:
    def __init__(self, logFile = "app/Robot.log"):
        self.logFile = logFile
        file = open(self.logFile, "w")
        file.write("")
        file.close()
    
    #Enregistre le log 
    def log(self, content):
        file = open(self.logFile, "a")
        file.write(content)
        file.close()