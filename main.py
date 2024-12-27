# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from source.control import ControlWindow
import source.libraries.font_lib as fontlib

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fontlib.loadFonts()
    controlWindow = ControlWindow()

    sys.exit(app.exec())
