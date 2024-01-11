import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader

def start_run():
    print("hello")

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
w = loader.load("ui/mainwindow.ui", None)
w.Cam1StatusLight.setStyleSheet(f"background-color: lightgrey")
w.show()
app.exec()