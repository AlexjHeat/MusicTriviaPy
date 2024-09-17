# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QFileInfo
from PySide6.QtWidgets import QMessageBox, QFileDialog
from db import Session, Directory

class FileManager:
    def __init__(self, parent):
        self.parent = parent
        self.activeDir = ""

    def getFilePath(self, fileName:str):
        #check if current active file path exists
        if self.checkActiveDir(fileName):
            return self.activeDir + fileName

        #if not, check database for a filepath that contains the song
        elif self.checkInactiveDirs(fileName):
            return self.activeDir + fileName

        #If not, asks the user to select the folder containing the song and adds it to the database.
        elif self.getDir(fileName):
            return self.activeDir + fileName

        else:
            return None

    def checkActiveDir(self, fileName:str):
        if QFileInfo(self.activeDir + fileName).isFile():
            return True
        return False

    def checkInactiveDirs(self, fileName:str):
        session = Session()
        directories = session.query(Directory).all()
        for directory in directories:
            if QFileInfo(directory.dir + fileName).isFile():
                self.activeDir = directory.dir
                return True
        return False


    def getDir(self, fileName:str):
        warning_msg = QMessageBox.warning(
                        self.parent,
                        'File not found',
                        f'Please select the folder that {fileName} is in!',
                        QMessageBox.Ok | QMessageBox.Cancel)
        if warning_msg == QMessageBox.Ok:

            dir = QFileDialog().getExistingDirectory(self.parent, f'Please select the folder that {fileName} is in!') + "\\"
            session = Session()
            if QFileInfo(dir + fileName).isFile():
                directory = Directory(dir=dir)
                session.add(directory)
                session.commit()
                self.activeDir =
                return True
        return False
