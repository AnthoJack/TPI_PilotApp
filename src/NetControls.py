import subprocess

class NetControls:

    def __init__(self, host):
        self.host = host
        self.directionY = 0
        self.directionX = 0
        self.previousAction = ""

    def pilot(self):
        command = ""
        if(self.directionY > 0):
            if(self.directionX > 0):
                command = "'fTurnR'"
            elif (self.directionX < 0):
                command = "fTurnL"
            else:
                command = "'fRun'"
        elif(self.directionY < 0):
            if(self.directionX > 0):
                command = "'bTurnR'"
            elif (self.directionX < 0):
                command = "'bTurnL'"
            else:
                command = "'bRun'"
        else:
            if(self.directionX > 0):
                command = "'rTurn'"
            elif (self.directionX < 0):
                command = "'lTurn'"
            else:
                command = "'idle'"
        if(command != self.previousAction):
            ssh = subprocess.run(["ssh", self.host, "/bin/bash", "-ilc", command], shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            self.previousAction = command
            return ssh.returncode
        return 0
        