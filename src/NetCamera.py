import subprocess

class NetCamera:
    
    def __init__(self, host = "anthojack@192.168.1.116", robotPath = "/PilotAppTemp/Images/", localPath = "app/images/"):
        self.host = host
        self.robotPath = robotPath
        self.localPath = localPath
        self.imageCount = 0
    
    def snap(self):
        if(subprocess.run(["ssh", self.host, "py", "~/PilotAppTemp/scripts/snap.py"]).returncode):
            print("ERROR: Unable to take picture")
            return -1
        else:
            if(self.getImage()):
                print("ERROR")
                return -1
            else:
                return self.imageCount
    
    def getImage(self):
        self.imageCount += 1
        if(subprocess.run(["scp", self.host + ":" + self.robotPath + "img.png", self.localPath + "img" + self.imageCount + ".png"])):
            return 0
        else:
            print("ERROR")
            return 1