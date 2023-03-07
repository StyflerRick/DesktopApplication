import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QWidget, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Checkbox')
        self.lbl = QLabel('Você bebe?')
        self.ck = QCheckBox('Sim')
        self.lbl2 = QLabel()
        # self.ck.setCheckState(Qt.Checked)

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.ck)
        layout.addWidget(self.lbl2)
        
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.ck.stateChanged.connect(self.state)

    def state(self, s):
        if s == Qt.Checked:
            self.lbl2.setText('Preencha:')


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
