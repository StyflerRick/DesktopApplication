import sys
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QFrame, QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Janela')
        self.setFixedSize(QSize(600, 400))

        self.input = QLineEdit()
        self.lbl = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.lbl)

        container = QFrame()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.input.textChanged.connect(self.lbl.setText)

    def texto(self):
        pass


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
