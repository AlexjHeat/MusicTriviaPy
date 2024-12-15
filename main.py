# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from controlwindow import ControlWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controlWindow = ControlWindow()

    sys.exit(app.exec())
