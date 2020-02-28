import sqlite3
def init(dbname):  
    sql = sqlite3.connect("./dbs/"+dbname)
    cursor = sql.cursor()
    cursor.execute("CREATE TABLE sys (id INTEGER PRIMARY KEY, wsname text, wspath text)")
    
def workspace(name):
    res = {"name": "test", "dirs":["images", "renders", "txt"], "prefx": ["i", "r", "t"]}
    return res