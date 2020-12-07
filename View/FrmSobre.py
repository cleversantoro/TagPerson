from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from View.UI.FrmSobre_UI import *

class Ui_Sobre(QMainWindow, Ui_FrmSobre):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    tela = Ui_Sobre()
    tela.show()
    app.exec()
