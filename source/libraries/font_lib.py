# This Python file uses the following encoding: utf-8

from PySide6.QtGui import  QFontDatabase, QFontInfo, QFont
from config import FONT_PATH
import os

def getFont(name: str, size: int, default:str = None) -> QFont:
    font = QFont(name, size)
    if QFontInfo(font).family() != name and default:
        font = QFont(default, size)
    return font

def loadFonts():
    files = os.listdir(FONT_PATH)
    for file in files:
        if os.path.isfile(f'{FONT_PATH}/{file}'):
            QFontDatabase.addApplicationFont(f"{FONT_PATH}/{file}")
