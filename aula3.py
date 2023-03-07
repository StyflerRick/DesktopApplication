# Importação dos módulos necessários
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QLabel)

# Definição da classe MainWindow que herda da classe QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QLabel')
        self.setFixedSize(QSize(600, 400))
        self.lbl = QLabel('Meu teste')
        font = self.lbl.font()
        font.setPointSize(35)
        self.lbl.setFont(font)
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(self.lbl)


# Criação da instância da aplicação e da janela principal, e execução da aplicação
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
