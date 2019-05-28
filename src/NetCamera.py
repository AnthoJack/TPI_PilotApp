import subprocess

#Classe implémentant les méthodes de prise de vue à distance et de récupération des images
class NetCamera:
    
    def __init__(self, host = "pi@192.168.0.12", robotPath = "PilotAppTemp/images", localPath = "app/images"):
        self.host = host
        self.robotPath = robotPath
        self.localPath = localPath
        self.imageCount = 0 #Nombre d'image stockées durant l'éxecution du programme
    
    #Méthode de prise de vue à distance
    def snap(self):
        if(subprocess.run(["ssh", self.host, "python3", "~/PilotAppTemp/scripts/snap.py"]).returncode):
            print("ERROR: Unable to take picture")
            return 1
        else:
            return 0
    
    #Méthode de récupération des images
    def getImage(self):
        self.imageCount += 1
        command = "scp %s:%s/img.gif %s/img%d.gif" % (self.host, self.robotPath, self.localPath, self.imageCount)
        if(subprocess.run(command, capture_output = True).returncode):
            print("ERROR")
            return 0
        else:
            return self.imageCount
            