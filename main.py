#glob
import shutil
import os
import getpass
#loc
import dbproc
import move

prefix = {"n":"new", "a":"add/sad", "b":"black/white/sa"}
def main():
    move.check(prefix, "C:/Users/ioakk/Documents/projanager/test", "test")
    move.grub(prefix, "C:/Users/ioakk/Documents/projanager/test", "test")

if __name__ == "__main__":
    main()