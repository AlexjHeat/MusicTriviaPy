# This Python file uses the following encoding: utf-8
from PySide6 import QtWidgets
from PySide6.QtCore import QDate
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QSpinBox, QDialogButtonBox, QDateEdit
from source.db import Record

class RecordDialog(QtWidgets.QDialog):
    def __init__(self, song, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.song = song
        self.setWindowTitle("Record")
        self.setupUI()

    def setupUI(self):
        #Song

        #Date
        self.dateEdit = QDateEdit()
        self.dateEdit.setDate(QDate.currentDate())

        #Stats
        statsLayout = QHBoxLayout()
        self.correctLineEdit = QSpinBox(self)
        self.totalLineEdit = QSpinBox(self)
        self.totalLineEdit.setValue(1)
        statsLayout.addWidget(QLabel("Correct", self))
        statsLayout.addWidget(self.correctLineEdit)
        statsLayout.addWidget(QLabel("/ Total", self))
        statsLayout.addWidget(self.totalLineEdit)

        #Button Box
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        #Layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(QLabel(str(self.song), self))
        mainLayout.addWidget(self.dateEdit)
        mainLayout.addLayout(statsLayout)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)


    def getRecord(self):
        return Record(  date = self.dateEdit.date().toPython(),
                        total = self.totalLineEdit.value(),
                        correct = self.correctLineEdit.value(),
                        song_id = self.song.id
                        )
