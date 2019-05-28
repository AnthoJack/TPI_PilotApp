from picamera import PiCamera
from time import sleep

conf = open("robot.conf").readlines()
setName = []
setVal = []
for line in conf[:-1]:
    splitLine = line.split(":")
    setName.append(splitLine[0])
    setVal.append(splitLine[1].strip("\n"))
camera = PiCamera()
resW = int(setVal[setName.index("imageResolution")].split("x")[0])
resH = int(setVal[setName.index("imageResolution")].split("x")[1])
camera.rotation = 180
camera.resolution = (resW, resH)
camera.start_preview()
sleep(2)
camera.capture(setVal[setName.index("robotImageDir")] + "/img.gif", format = "gif")
camera.stop_preview()
