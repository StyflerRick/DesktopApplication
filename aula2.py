import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QLabel)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Title Here')  # Define o titulo da aplicação

        self.lbl_altura = QLabel('Altura')
        self.txt_altura = QLineEdit()  # Caixinha da altura
        self.lbl_comprimento = QLabel('Comprimento')
        self.txt_comprimento = QLineEdit()  # Caixinha do comprimento
        self.lbl_largura = QLabel('Largura')
        self.txt_largura = QLineEdit()  # Caixinha da largura

        self.lbl_resultado = QLabel()  # Mostra o resultado
        self.btn_calcular = QPushButton('Calcular')  # Botao calcular

        # Adiciona os Widgets no sistema
        layout = QVBoxLayout()
        layout.addWidget(self.lbl_altura)
        layout.addWidget(self.txt_altura)
        layout.addWidget(self.lbl_comprimento)
        layout.addWidget(self.txt_comprimento)
        layout.addWidget(self.lbl_largura)
        layout.addWidget(self.txt_largura)
        layout.addWidget(self.lbl_resultado)
        layout.addWidget(self.btn_calcular)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.btn_calcular.clicked.connect(self.calcular_metro_cubico)

    def calcular_metro_cubico(self):
        resultado = str(
            float(self.txt_altura.text()) *
            float(self.txt_comprimento.text()) *
            float(self.txt_largura.text())
        )
        self.lbl_resultado.setText(resultado)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
