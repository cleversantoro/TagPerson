from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *

from Controller.CombateCTR import CombateCTR as combate
from Controller.PersonagemCTR import PersonagemCTR as personagem

from resources.categoria import *

from Helpers.constantes import const
import os


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

        self.appEvents()

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

    def appEvents(self):
        self.person = personagem.get_persona(8)
        rows = personagem.get_persona_combat(self.person.id,1)        

        #self.tblCombate.setColumnHidden(0,True)
        self.tblCombate.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblCombate.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblCombate.verticalHeader().hide()

        header = self.tblCombate.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
        #self.tblCombate.setColumnWidth(2, 180);
        

        #item = QtGui.QTableWidgetItem(icon, "") # Second argument (required !) is text
        #self.tableWidget.setItem(0, 0, item)

        while (self.tblCombate.rowCount() > 0):
                self.tblCombate.removeRow(0)

        row = 0
        for item in rows:
            self.tblCombate.insertRow(row)
            #id = QTableWidgetItem(str(item[0]))
            descricao = QTableWidgetItem(str(item[1]))
            
            self.nivel = QtWidgets.QSpinBox()
            self.nivel.setValue(item[2])
            self.nivel.valueChanged.connect(self.teste)

            #nivel = QTableWidgetItem(niv,None)
            custo = QTableWidgetItem(str(item[3]))
            ajuste = QTableWidgetItem(str(item[4]))
            total = QTableWidgetItem(str(item[5]))
            categoria = QTableWidgetItem(str(item[7]))
            icon = QtGui.QIcon(QtGui.QPixmap(":/categoria/{}".format(item[8])))
            icone = QTableWidgetItem(icon,None)

            #self.tblCombate.setItem(row, 0, id)
            self.tblCombate.setItem(row, 0, descricao)
            self.tblCombate.setCellWidget(row, 1, self.nivel)
            self.tblCombate.setItem(row, 2, custo)
            self.tblCombate.setItem(row, 3, ajuste)
            self.tblCombate.setItem(row, 4, total)
            self.tblCombate.setItem(row, 5, categoria)
            self.tblCombate.setItem(row, 6, icone)
            row = row + 1
        
        #self.setTableWidthPersonagems()
    def teste(self):
        item = self.nivel.value()
        msg = QMessageBox()
        msg.setText(str(item))
        msg.exec();

    def setTableWidthPersonagems(self):
        width = self.tblCombate.verticalHeader().width()
        width += self.tblCombate.horizontalHeader().length()
        if self.tblCombate.verticalScrollBar().isVisible():
            width += self.tblCombate.verticalScrollBar().width()
        width += self.tblCombate.frameWidth() * 2
        self.tblCombate.setFixedWidth(width)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
