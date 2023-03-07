# Importação dos módulos necessários
import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QLabel)

# Definição da classe MainWindow que herda da classe QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Definição do título da janela principal
        self.setWindowTitle('Title Here')

        # Criação dos rótulos e caixas de texto para entrada de dados
        self.lbl_altura = QLabel('Altura')
        self.txt_altura = QLineEdit()
        self.lbl_comprimento = QLabel('Comprimento')
        self.txt_comprimento = QLineEdit()
        self.lbl_largura = QLabel('Largura')
        self.txt_largura = QLineEdit()

        # Criação do rótulo para exibição do resultado e botão de cálculo
        self.lbl_resultado = QLabel()
        self.btn_calcular = QPushButton('Calcular')

        # Criação do layout vertical e adição dos widgets
        layout = QVBoxLayout()
        layout.addWidget(self.lbl_altura)
        layout.addWidget(self.txt_altura)
        layout.addWidget(self.lbl_comprimento)
        layout.addWidget(self.txt_comprimento)
        layout.addWidget(self.lbl_largura)
        layout.addWidget(self.txt_largura)
        layout.addWidget(self.lbl_resultado)
        layout.addWidget(self.btn_calcular)

        # Criação do quadro e definição do layout como layout central
        container = QFrame()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Conexão do sinal clicked do botão de cálculo ao slot calcular_metro_cubico
        self.btn_calcular.clicked.connect(self.calcular_metro_cubico)

    # Definição do método para cálculo do volume
    def calcular_metro_cubico(self):
        resultado = str(
            float(self.txt_altura.text()) *
            float(self.txt_comprimento.text()) *
            float(self.txt_largura.text())
        )
        self.lbl_resultado.setText(resultado)


# Criação da instância da aplicação e da janela principal, e execução da aplicação
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
