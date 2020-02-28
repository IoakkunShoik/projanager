#glob
import shutil
import os
import getpass
#loc
import dbproc
import move


def main():
    print(move.prefix)
    move.grub(move.prefix, "C:/Users/ioakk/Documents/projanager/test/", "test")

if __name__ == "__main__":
    main()