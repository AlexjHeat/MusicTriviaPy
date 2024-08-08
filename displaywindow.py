# This Python file uses the following encoding: utf-8
from PySide6 import QtUiTools
from PySide6.QtCore import QUrl, QFileInfo
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QMessageBox, QVBoxLayout

SONG_FOLDER = "D:\\QtProjects\\MusicTriviaPy\\Songs\\"

class DisplayWindow:
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = QtUiTools.QUiLoader().load("displaywindow.ui")
        self.ui.show()

        self.mediaPlayer = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.mediaPlayer.setAudioOutput(self.audioOutput)

        #self.videoWidget = QVideoWidget()
        #QMessageBox.warning(self.parent, 'Warning', str(type(self.ui.videoWidget)))

        #self.video = QVideoWidget(self.ui.videoScreen)
        #self.mediaPlayer.setVideoOutput(self.video)

        #self.video = QVideoWidget(self.ui.videoScreen)

        #self.videoWidget.show()

    def play(self, song):
        fileString = SONG_FOLDER + song.fileName
        if not QFileInfo(fileString).exists():
            QMessageBox.warning(self.parent, 'Warning', fileString + " not found!")
            return False
        #if not self.checkFileName(song.fileName):
        #    return False
        self.mediaPlayer.setSource(QUrl.fromLocalFile(fileString))


        #TESTING
        #test = QVBoxLayout(self.ui.videoScreen)
        self.videoWidget = QVideoWidget()
        #test.addWidget(self.videoWidget)
        self.ui.main_layout.addWidget(self.videoWidget)
        #self.videoWidget = QVideoWidget(self.ui.videoScreen)
        #self.videoWidget.resize(500, 500)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.play()

'''
    #Verifies that the current active directiory contains the fileName. If not, tries to find a valid directory in the database.
    def setValidDirectory(self, fileName:str):
        if QFileInfo(self.activeDir + fileName).isFile():
            return True

        session = Session()
        filePaths = session.query(FilePath).filter(FilePath).all()
        for filePath in filePaths:
            file = QFileInfo(filePath + fileName)
            if file.isFile():
                self.activeDir = filePath
                return True
        return False

    #Checks if a valid directory already exists in the database. If not, it will ask the user for one
    def checkFileName(self, fileName:str):
        if self.setValidDirectory(fileName):
                return True
        else:
            warning_msg = QMessageBox.warning(
                            self.parent,
                            'File not found',
                            f'Please select the folder that {fileName} is in!',
                            QMessageBox.Ok | QMessageBox.Cancel)
            if warning_msg == QMessageBox.Ok:
                dir = QFileDialog().getExistingDirectory(self.parent, f'Please select the folder that {fileName} is in!')
                print(dir)
                #add dir to database
                #self.activeDir = dir
                return True
            return False
'''




