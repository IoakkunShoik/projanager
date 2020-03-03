import sys
import os
from PyQt5 import QtWidgets
from gui import mainwindow
import dbproc
import move

class Projanager(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def display(self, arg):
        j = self.Observable.text()
        self.PrefixNavigator.setHtml(j)
        return 0

    def insert(self, insertFunc):
        wspath = self.Observable.text()
        wsname  = self.WorkspaceName.text()
        wss  = self.Workspaces.text()
        prefvalue = self.Prefix.text()
        preffolder = self.PrefixPath.text()
        insertFunc([wspath, wsname, wss, prefvalue, preffolder])
        self.display("123")
        self.refresh()
        self.Observable.setText("")
        self.WorkspaceName.setText("")
        self.Workspaces.setText("")
        self.Prefix.setText("")
        self.PrefixPath.setText("")

    
    def refresh(self):
        showArr = dbproc.show()
        outputStr = "<style>td{border:1px solid black;}</style><table>"
        outputStr += "<tr><td><b>Path</b></td><td><b>Workspace</b></td><td><b>Workspaces path</b></td><td><b>prefix</b></td><td><b>Path to prefix</b></td></tr>"
        for i in showArr:
            outputStr+="<tr><td>"+i[1]+"</td><td>"+i[2]+"</td><td>"+i[3]+"</td><td>"+i[4]+"</td><td>"+i[5]+"</td></tr>"
        outputStr += "</table>"
        self.PrefixNavigator.setHtml(outputStr)

    def remove(self, removeFunc):
        txtPrf = self.DeleteByPrefix.text()
        removeFunc(txtPrf)
        self.refresh()

    def init(self, initFunc):
        initFunc()
        
    def move(self, mkPrefFunc, moveFunc):
        prefixResponse = mkPrefFunc(self.moveLine.text())
        moveFunc.check(prefixResponse[0], prefixResponse[1][0], prefixResponse[1][1], prefixResponse[1][2])
        moveFunc.grub(prefixResponse[0], prefixResponse[1][0], prefixResponse[1][1], prefixResponse[1][2])
def guiView():
    app = QtWidgets.QApplication(sys.argv)
    window = Projanager()
    window.show()
    window.refresh()
    window.DbInit.clicked.connect(lambda: window.init(dbproc.init))
    window.AddingButtun.clicked.connect(lambda: window.insert(dbproc.insert))
    window.DeletingButton.clicked.connect(lambda: window.remove(dbproc.remove))
    window.Move.clicked.connect(lambda: window.move(dbproc.makePrefix, move))
    app.exec_()
    #print(os.popen("dir").read())

if __name__ == '__main__':
    guiView()