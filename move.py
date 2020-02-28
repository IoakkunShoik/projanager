import shutil
import os


def grub(prefix, path, workspace):
    fList = os.listdir(path)
    #moving:
    for f in fList:
        print(f[f.find("-")+1:])
        shutil.copyfile(path+"/"+f, "workspaces/"+workspace+"/"
        +prefix[f[:f.find("-")]]+"/"+f[f.find("-")+1:] )
    #testing:
    for f in fList:
        if os.path.isfile("workspaces/"+workspace+"/" +prefix[f[:f.find("-")]]+"/"+f[f.find("-")+1:]):
            if os.path.isfile(path+"/"+f):
                os.remove(path+"/"+f)
        else: grub(prefix, path, workspace)
        
    

def check(prefix, path, workspace):
    #creating workspace
    if not os.path.exists("workspaces/"+workspace):
        os.mkdir("workspaces/"+workspace)
    #creating all paths:
    for pref in prefix:
        mkTree = []
        if prefix[pref].find("/")!=-1:
            folderIerarchy = prefix[pref].split("/")
            for folder in folderIerarchy:
                if not mkTree : 
                    mkTree.append("workspaces/"+workspace+"/"+folder)
                    continue
                mkTree.append(mkTree[-1]+"/"+folder)
    #
        if prefix[pref].find("/")==-1:
            mkTree.append("workspaces/"+workspace+"/"+prefix[pref])

        for i in mkTree:
            if not os.path.exists(i):
                os.mkdir(i)
    
