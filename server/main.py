
import sys
from gui import gui
from pprint import pprint
from tkinter import *
from server import MyServer
import time
import threading

newOutput = False
output = ""
myServer = MyServer(sys.argv[1], sys.argv[2])
my_gui = gui()

def applicationStart():
    global my_gui
    my_gui.startGui()

def checkNewOutput():
    global output
    global newOutput
    global myServer
    global my_gui

    #TODO have to add something here to update title or whatever in gui
    if(newOutput):
        myServer.setNewOutput(False)
        my_gui.updateMessage(output)
        newOutput = False

def serverStart():
    global output
    global newOutput
    global myServer
    
    myServer.run()
    output = myServer.getOutput()
    newOutput = myServer.getNewOutput()
    checkNewOutput()
    serverStart()

thread = threading.Thread(target = serverStart)
thread.daemon = True
thread.start()

if __name__ == "__main__":
    applicationStart()