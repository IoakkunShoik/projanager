import sys


def showParams():
    print(sys.argv[1:])

def paramsProc():
    try:
        for arg in range(9):
            if sys.argv[arg] == "-i": return [1]                                                                      #Initialize db
            if sys.argv[arg] == "-a": return [2, sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6]]     #Insert prefix
            if sys.argv[arg] == "-s": return [3]                                                                      #Show prefixes
            if sys.argv[arg] == "-h": return [4]                                                                      #Take help
            if sys.argv[arg] == "-m": return [5, sys.argv[arg+1]]                                                     #Move files
            if sys.argv[arg] == "-r": return [9, sys.argv[arg+1]]                                                     #Remove prefix
    except:
        return [4]