import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)

win = MainWindow()
win.setWindowTitle("SBC Run Control")
win.resize(1200,750)
win.show()

app.exec()