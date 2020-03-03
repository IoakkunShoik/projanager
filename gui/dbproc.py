import sqlite3
def init():
    
    try:
        sql = sqlite3.connect("../dbs/db.db")
        

        cursor = sql.cursor()
        cursor.execute("""CREATE TABLE sys (id INTEGER PRIMARY KEY, wspath text, wsname text,
        wss text, prefvalue text, preffolder text)""")
    except:
        return "Database already exists"
    return "done"
    #   ["C:/Users/ioakk/Documents/projanager/test", "test", "workspaces", "a", "add/sad", "test"]

    #   wspath  - path to workspace                       "C:/Users/ioakk/Documents/projanager/test"
    #   wsname - name of workspace                        "test"
    #   wss  - workspaces name                            "workspaces"
    #   prefvalue  - contains prefix                      "a"
    #   preffolder  - contains folder of prefix           "add/sad"
    #   checkingfolder - target folder                    "test"
dbproc.init()
def insert(query):
    sql = sqlite3.connect("./dbs/db.db")
    cursor = sql.cursor()
    var = cursor.execute("SELECT * FROM sys WHERE wspath=? and wsname=? and wss=? and prefvalue=?", query[:4])
    for i in var:
        return "this prefix already exists"
    
    cursor.execute("INSERT INTO sys(wspath, wsname, wss, prefvalue, preffolder) VALUES (?,?,?,?,?)", query)
    sql.commit()
    return "done"

def remove(i):
    sql = sqlite3.connect("./dbs/db.db")
    cursor = sql.cursor()
    var = cursor.execute("DELETE FROM sys WHERE prefvalue=?", [i])
    sql.commit()
    return id

def show():
    sql = sqlite3.connect("./dbs/db.db")
    cursor = sql.cursor()
    var = cursor.execute("SELECT * FROM sys")
    result=[]
    for i in var:
        result.append(i)
    return result
#prefix = {"n":"new", "a":"add/sad", "b":"black/white/sa"}
def makePrefix(workspace):
    sql    = sqlite3.connect("./dbs/db.db")
    cursor = sql.cursor()
    output = cursor.execute("SELECT * FROM sys WHERE wsname=?", [workspace]).fetchall()
    prefix= {}
    try:
        for item in output:
            prefix[item[4]]=item[5]
            paths = [item[1], item[2], item[3]]
        result = (prefix, paths)
    except:
        result = ('', ["","",""])
    return result
