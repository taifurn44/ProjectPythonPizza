# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pizza.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Login import Ui_Login
from Menu import Ui_Menu

class Ui_Pizza(object):
    def setupUi(self, Pizza):
        Pizza.setObjectName("Pizza")
        Pizza.setWindowModality(QtCore.Qt.NonModal)
        Pizza.setEnabled(True)
        Pizza.resize(440, 299)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Pizza.sizePolicy().hasHeightForWidth())
        Pizza.setSizePolicy(sizePolicy)
        Pizza.setMinimumSize(QtCore.QSize(1, 1))
        Pizza.setMaximumSize(QtCore.QSize(572, 416))
        Pizza.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pictures/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Pizza.setWindowIcon(icon)
        Pizza.setToolTip("")
        Pizza.setStyleSheet("")
        Pizza.setModal(False)
        self.label = QtWidgets.QLabel(Pizza)
        self.label.setGeometry(QtCore.QRect(0, 0, 441, 301))
        self.label.setMinimumSize(QtCore.QSize(441, 301))
        self.label.setMaximumSize(QtCore.QSize(441, 301))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Pictures/269 (1).jpg"))
        self.label.setObjectName("label")
        self.butMenu = QtWidgets.QPushButton(Pizza)
        self.butMenu.setGeometry(QtCore.QRect(120, 120, 201, 41))
        self.butMenu.setStyleSheet("border-radius: 10px;\n""background-color: rgb(255, 255, 255);\n""color: rgb(170, 85, 0);\n""")
        self.butMenu.setObjectName("butMenu")
        self.butManager = QtWidgets.QPushButton(Pizza)
        self.butManager.setGeometry(QtCore.QRect(120, 190, 201, 41))
        self.butManager.setStyleSheet("border-radius: 10px;\n""background-color: rgb(170, 85, 0);\n""color: white;")
        self.butManager.setObjectName("butManager")
        self.label_2 = QtWidgets.QLabel(Pizza)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 441, 61))
        self.label_2.setStyleSheet("background-color: rgba(144, 144, 144, 250);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Pizza)
        self.label_3.setGeometry(QtCore.QRect(60, 13, 341, 51))
        self.label_3.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n""color: rgb(85, 255, 255);")
        self.label_3.setObjectName("label_3")

        self.butManager.clicked.connect(self.openManager)
        self.butMenu.clicked.connect(self.openMenu)

        self.retranslateUi(Pizza)
        QtCore.QMetaObject.connectSlotsByName(Pizza)

        self.Pizza = Pizza

    def openMenu(self):
        self.windows = QtWidgets.QDialog()
        self.ui = Ui_Menu()
        self.ui.setupUi(self.windows,self.Pizza)
        self.windows.show()
        self.Pizza.close()

    def openManager(self):
        self.windows = QtWidgets.QDialog()
        self.ui = Ui_Login()
        self.ui.setupUi(self.windows,self.Pizza)
        self.windows.show()
        self.Pizza.close()

    def retranslateUi(self, Pizza):
        _translate = QtCore.QCoreApplication.translate
        Pizza.setWindowTitle(_translate("Pizza", "Pizza"))
        self.butMenu.setText(_translate("Pizza", "Menu"))
        self.butManager.setText(_translate("Pizza", "Manager"))
        self.label_3.setText(_translate("Pizza", "Pizza Ordering system"))
#import Pictures_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pizza = QtWidgets.QDialog()
    ui = Ui_Pizza()
    ui.setupUi(Pizza)
    Pizza.show()
    sys.exit(app.exec_())
