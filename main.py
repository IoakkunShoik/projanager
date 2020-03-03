#glob
import shutil
import os
import getpass
#loc

import move
from gui import gui
from view import *
import dbproc

prefix = {"n":"new", "a":"add/sad", "b":"black/white/sa"}
def main():

    #query = ["C:/Users/ioakk/Documents/projanager/test", "test", "workspaces", "n", "new"]
    
    action = paramsProc()
    if   action==None:  action=[4]

    if   action[0]==1:  print(dbproc.init())
    elif action[0]==2:  print(dbproc.insert(action[1:]))
    elif action[0]==3:  print(dbproc.show())
    elif action[0]==4:  print("   -i - init database\n   -a - insert into database prefix\n   -s - show your database\n   -m - move files")

    elif action[0]==5:  
        prefixResponse = dbproc.makePrefix(action[1])
        move.check  (prefixResponse[0], prefixResponse[1][0], prefixResponse[1][1], prefixResponse[1][2])
        move.grub   (prefixResponse[0], prefixResponse[1][0], prefixResponse[1][1], prefixResponse[1][2])
    elif action[0]==9:  print(dbproc.remove(action[1]))

    gui.guiView()

if __name__ == "__main__":
    main()
