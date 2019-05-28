import subprocess

#Classe implémentant les méthode pour l'enregistrement de la configuration de l'application et du robot
class SettingSaver:

    def __init__(self, host = "pi@192.168.0.12", robotFile = "~/PilotAppTemp/robot.conf", appFile = "app/app.conf"):
        self.host = host
        self.robotFile = robotFile
        self.appFile = appFile
    
    #Méthode d'enregistrement de la configuration de l'app
    def appSet(self, content):
        robotConf = open(self.appFile, "w")
        robotConf.write(content)
        robotConf.close()
    
    #Méthode d'enregistrement
    def robotSet(self, content):
        subprocess.run(["ssh", self.host, "echo", "'" + content + "'", ">", self.robotFile])
