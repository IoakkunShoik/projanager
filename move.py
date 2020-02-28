import shutil
import os
prefix = {"n":"new", "a":"add/sad", "b":"black/white/sa"}

def grub(prefix, path, workspace):
    fList = os.listdir(path)

    if not os.path.exists("workspaces/"+workspace):
        os.mkdir("workspaces/"+workspace)
    
    for pref in prefix:

        mkTree = []
        workString = "workspaces/"+workspace+"/"+prefix[pref][:prefix[pref].find("/")]
        
        if prefix[pref].find("/")!=-1:
            folderIerarchy = prefix[pref].split("/")
            for folder in folderIerarchy:
                if not mkTree : 
                    mkTree.append("workspaces/"+workspace+"/"+folder)
                    continue
                mkTree.append(mkTree[-1]+"/"+folder)
        

            
        if prefix[pref].find("/")==-1:
            mkTree.append("workspaces/"+workspace+"/"+prefix[pref])
        
        for i in mkTree:
            if not os.path.exists(i):
                os.mkdir(i)
    
    """
    for i in fList:
        shutil.copyfile(path+"/"+i, "workspaces/"+workspace+"/"+i)"""
