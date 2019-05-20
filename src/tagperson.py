import sys,sqlite3,time
from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem


qtCreatorFile = "tagperson.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class TagPerson(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):

        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #self.btnTeste.clicked.connect(self.ExibiMensagem)
        #self.tblPersonagens.setModel(self.PopularTabela)
        self.PopularTabela()
        self.tblPersonagens.doubleClicked.connect(self.on_click)
        self.dAgilidade.valueChanged.connect(self.spinBox.setValue)
        self.dAgilidade.valueChanged.connect(self.verticalSlider.setValue)
        self.dAgilidade.valueChanged.connect(self.lcdNumber.display)

        self.spinBox.valueChanged.connect(self.dAgilidade.setValue)
        self.verticalSlider.valueChanged.connect(self.dAgilidade.setValue)

    def ExibiMensagem(self):
        QMessageBox.about(self, "Mensagem", "Botão Clicado")

    def PopularTabela(self):
        self.conn=sqlite3.connect("user.db")
        self.c=self.conn.cursor()
        query = "SELECT id, name, xp FROM persona"
        self.c.execute(query)
        rows = self.c.fetchall()
        for row in rows:
            rowPosition = self.tblPersonagens.rowCount()
            self.tblPersonagens.insertRow(rowPosition)
            for col in row:
                self.tblPersonagens.setItem(rowPosition, row.index(col), QTableWidgetItem(str(col)))
        self.c.close()
        self.conn.close()
    
    def on_click(self):
        #print("\n")
        for currentQTableWidgetItem in self.tblPersonagens.selectedItems():
            #valor = (currentQTableWidgetItem.row().str() , currentQTableWidgetItem.column().str(), currentQTableWidgetItem.text().str()).format(0,1,2)
            QMessageBox.about(self, "Mensagem", currentQTableWidgetItem.text())
            #print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    def table_appender(widget, *args):
        def set_columns(len, pos):
            if pos == len-1:
                widget.setItem(widget.rowCount()-1, pos, QTableWidgetItem(args[pos]))
            else:
                widget.setItem(widget.rowCount()-1, pos, QTableWidgetItem(args[pos]))
                set_columns(len, pos+1)
        widget.insertRow(widget.rowCount())
        set_columns(widget.columnCount(), 0)
        3
            

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TagPerson()
    window.show()
    sys.exit(app.exec_())