import shutil
import os


def grub(prefix, path, workspace, wkspsfold):
    fList = os.listdir(path)
    
    #moving:
    for f in fList:
        if not os.path.exists(wkspsfold+ "/"+workspace+"/" +prefix[f[f.find("!")+1:f.find("-")]]+"/"+f[f.find("-")+1:]) or f.find('!')!=-1:
           
            print(wkspsfold+ "/"+workspace+"/" +prefix[f[f.find("!")+1:f.find("-")]]+"/"+f[f.find("-")+1:])

            shutil.copyfile(path+"/"+f, wkspsfold+"/"+workspace+"/"
            +prefix[f[f.find("!")+1:f.find("-")]]+"/"+f[f.find("-")+1:] )
    #testing and removing:
    for f in fList:
        if os.path.isfile(wkspsfold+ "/"+workspace+"/" +prefix[f[:f.find("-")]]+"/"+f[f.find("-")+1:]):
            if os.path.isfile(path+"/"+f):
                os.remove(path+"/"+f)
        else: grub(prefix, path, workspace, wkspsfold)
        
    

def check(prefix, path, workspace, wkspsfold):
    #creating workspace
    if not os.path.exists(wkspsfold):
        os.mkdir(wkspsfold)
    if not os.path.exists(wkspsfold+"/"+workspace):
        os.mkdir(wkspsfold+"/"+workspace)
    #creating all paths:
    for pref in prefix:
        mkTree = []
        if prefix[pref].find("/")!=-1:
            folderIerarchy = prefix[pref].split("/")
            for folder in folderIerarchy:
                if not mkTree : 
                    mkTree.append(wkspsfold+"/"+workspace+"/"+folder)
                    continue
                mkTree.append(mkTree[-1]+"/"+folder)
    #
        if prefix[pref].find("/")==-1:
            mkTree.append(wkspsfold+"/"+workspace+"/"+prefix[pref])

        for i in mkTree:
            if not os.path.exists(i):
                os.mkdir(i)
    
