# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teste.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 457)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tblCombate = QtWidgets.QTableWidget(self.centralwidget)
        self.tblCombate.setGeometry(QtCore.QRect(10, 10, 471, 391))
        self.tblCombate.setObjectName("tblCombate")
        self.tblCombate.setColumnCount(7)
        self.tblCombate.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tblCombate.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCombate.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCombate.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCombate.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCombate.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCombate.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCombate.setHorizontalHeaderItem(6, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tblCombate.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Descrião"))
        item = self.tblCombate.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nivel"))
        item = self.tblCombate.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "custo"))
        item = self.tblCombate.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ajuste"))
        item = self.tblCombate.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "total"))
        item = self.tblCombate.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "categoria"))
        item = self.tblCombate.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "icone"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
