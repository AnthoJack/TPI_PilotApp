import subprocess

class SettingSaver:

    def __init__(self, host = "pi@192.168.0.12", robotFile = "~/PilotAppTemp/robot.conf", appFile = "app/app.conf"):
        self.host = host
        self.robotFile = robotFile
        self.appFile = appFile
    
    def appSet(self, content):
        robotConf = open(self.appFile, "w")
        robotConf.write(content)
        robotConf.close()
    
    def robotSet(self, content):
        subprocess.run(["ssh", self.host, "echo", "'" + content + "'", ">", self.robotFile])
