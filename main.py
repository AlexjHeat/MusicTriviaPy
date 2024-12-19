# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from controlwindow import ControlWindow
from db import createTables
import fontlib

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #createTables()
    #fontlib.loadFonts()
    controlWindow = ControlWindow()

    sys.exit(app.exec())
