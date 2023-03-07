# Importação dos módulos necessários
import sys
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QLabel)

# Definição da classe MainWindow que herda da classe QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QLabel')
        self.lbl = QLabel()
        self.lbl.setPixmap(QPixmap('img.png'))

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)

        self.setCentralWidget(self.lbl)


# Criação da instância da aplicação e da janela principal, e execução da aplicação
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
