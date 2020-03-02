# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(970, 560)
        MainWindow.setMinimumSize(QtCore.QSize(970, 560))
        MainWindow.setMaximumSize(QtCore.QSize(970, 560))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 971, 561))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.NavArea = QtWidgets.QWidget(self.widget)
        self.NavArea.setGeometry(QtCore.QRect(9, 10, 951, 301))
        self.NavArea.setObjectName("NavArea")
        self.PrefixNavigator = QtWidgets.QTextBrowser(self.NavArea)
        self.PrefixNavigator.setGeometry(QtCore.QRect(0, 0, 951, 301))
        self.PrefixNavigator.setObjectName("PrefixNavigator")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(-10, 310, 1001, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Observable = QtWidgets.QLineEdit(self.widget)
        self.Observable.setGeometry(QtCore.QRect(20, 360, 351, 22))
        self.Observable.setObjectName("Observable")
        self.WorkspaceName = QtWidgets.QLineEdit(self.widget)
        self.WorkspaceName.setGeometry(QtCore.QRect(380, 360, 151, 22))
        self.WorkspaceName.setObjectName("WorkspaceName")
        self.Prefix = QtWidgets.QLineEdit(self.widget)
        self.Prefix.setGeometry(QtCore.QRect(540, 360, 61, 22))
        self.Prefix.setObjectName("Prefix")
        self.PrefixPath = QtWidgets.QLineEdit(self.widget)
        self.PrefixPath.setGeometry(QtCore.QRect(610, 360, 351, 22))
        self.PrefixPath.setText("")
        self.PrefixPath.setObjectName("PrefixPath")
        self.labelPathObserv = QtWidgets.QLabel(self.widget)
        self.labelPathObserv.setGeometry(QtCore.QRect(20, 340, 251, 16))
        self.labelPathObserv.setObjectName("labelPathObserv")
        self.labelWorkspace = QtWidgets.QLabel(self.widget)
        self.labelWorkspace.setGeometry(QtCore.QRect(380, 340, 141, 16))
        self.labelWorkspace.setObjectName("labelWorkspace")
        self.labelPrefName = QtWidgets.QLabel(self.widget)
        self.labelPrefName.setGeometry(QtCore.QRect(540, 340, 55, 16))
        self.labelPrefName.setObjectName("labelPrefName")
        self.LabelPrefPath = QtWidgets.QLabel(self.widget)
        self.LabelPrefPath.setGeometry(QtCore.QRect(610, 340, 211, 16))
        self.LabelPrefPath.setObjectName("LabelPrefPath")
        self.AddingButtun = QtWidgets.QPushButton(self.widget)
        self.AddingButtun.setGeometry(QtCore.QRect(20, 390, 941, 28))
        self.AddingButtun.setObjectName("AddingButtun")
        self.DeleteByPrefix = QtWidgets.QLineEdit(self.widget)
        self.DeleteByPrefix.setGeometry(QtCore.QRect(20, 490, 281, 22))
        self.DeleteByPrefix.setObjectName("DeleteByPrefix")
        self.labelDelete = QtWidgets.QLabel(self.widget)
        self.labelDelete.setGeometry(QtCore.QRect(20, 470, 141, 16))
        self.labelDelete.setObjectName("labelDelete")
        self.DeletingButton = QtWidgets.QPushButton(self.widget)
        self.DeletingButton.setGeometry(QtCore.QRect(310, 490, 93, 28))
        self.DeletingButton.setObjectName("DeletingButton")
        self.DbInit = QtWidgets.QPushButton(self.widget)
        self.DbInit.setGeometry(QtCore.QRect(790, 460, 161, 81))
        self.DbInit.setObjectName("DbInit")
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(-10, 430, 1001, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setGeometry(QtCore.QRect(760, 440, 16, 131))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Projanager"))
        self.PrefixNavigator.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">TextText</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.labelPathObserv.setText(_translate("MainWindow", "Путь до отслеживаемой папки"))
        self.labelWorkspace.setText(_translate("MainWindow", "Имя workspace"))
        self.labelPrefName.setText(_translate("MainWindow", "Префикс"))
        self.LabelPrefPath.setText(_translate("MainWindow", "Путь до папки префикса"))
        self.AddingButtun.setText(_translate("MainWindow", "Добавить префикс"))
        self.labelDelete.setText(_translate("MainWindow", "Удаляемый префикс"))
        self.DeletingButton.setText(_translate("MainWindow", "Удалить"))
        self.DbInit.setText(_translate("MainWindow", "Инициализировать \n"
" базу данных"))
