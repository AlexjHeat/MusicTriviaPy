# This Python file uses the following encoding: utf-8
from PySide6 import QtUiTools

class DisplayWindow:
    def __init__(self):
        super().__init__()
        self.ui = QtUiTools.QUiLoader().load("displaywindow.ui")
        self.ui.show()
