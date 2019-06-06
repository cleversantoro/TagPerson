#from PyQt5.QtSql import QSqlDatabase
import os  
import sqlite3

class ConexaoSQL:
    DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'tagperson.db')
    def db_connect(db_path=DEFAULT_PATH):  
        con = sqlite3.connect(db_path)
        #con.text_factory = lambda x: str(x, "latin1")
        return con

    def close_db(self):
        if self.conn:
            self.conn.close()
            #print("Conexão fechada.")
