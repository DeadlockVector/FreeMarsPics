import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QComboBox,
    QMainWindow,
    QApplication,
    QVBoxLayout,
    QWidget
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("The Martian Chronicles")
        self.setFixedSize(QSize(896, 896))

        layout = QVBoxLayout()
        #rover_list = QComboBox()
        layout.addWidget(QComboBox())
        widget = QWidget()

        widget.setLayout(layout)

        self.setCentralWidget(widget)

app = QApplication([])
window = MainWindow()
window.show()

app.exec()
