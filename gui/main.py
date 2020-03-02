import sys
from PyQt5 import QtWidgets
import mainwindow

class Projanager(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)
        self.DbInit.released.connect(self.a)

    def a(self):
        self.PrefixNavigator.setHtml("asdasdasdasdsdsdas")
        return 0

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Projanager()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()