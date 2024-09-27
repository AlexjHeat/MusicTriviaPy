# This Python file uses the following encoding: utf-8
from PySide6 import QtWidgets
from PySide6.QtCore import QDir
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QDialogButtonBox, QToolButton, QFileDialog
from db import Category

class CategoryDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Category")
        self.setupUI()

    def setupUI(self):
        #Name Field
        nameLayout = QHBoxLayout()
        nameLabel = QLabel("Name", self)
        self.nameEdit = QLineEdit(self)
        nameLayout.addWidget(nameLabel)
        nameLayout.addSpacing(28)
        nameLayout.addWidget(self.nameEdit)

        #Folder Field
        folderLayout = QHBoxLayout()
        folderLabel = QLabel("Folder", self)
        self.folderEdit = QLineEdit(self)
        folderDialogButton = QToolButton(self)
        folderDialogButton.released.connect(self.getFolder)
        folderLayout.addWidget(folderLabel)
        folderLayout.addWidget(self.folderEdit)
        folderLayout.addWidget(folderDialogButton)

        #Background Color Hex
        backgroundColorLayout = QHBoxLayout()
        backgroundColorLabel = QLabel("Background Color Hex", self)
        self.backgroundColorEdit = QLineEdit(self)
        backgroundColorLayout.addWidget(backgroundColorLabel)
        backgroundColorLayout.addWidget(self.backgroundColorEdit)

        #Clock Color Hex
        clockColorLayout = QHBoxLayout()
        clockLabel = QLabel("Clock Color Hex", self)
        self.clockColorEdit = QLineEdit(self)
        clockColorLayout.addWidget(clockLabel)
        clockColorLayout.addWidget(self.clockColorEdit)

        #LCD Color Hex
        lcdColorLayout = QHBoxLayout()
        lcdLabel = QLabel("LCD Color Hex", self)
        self.lcdColorEdit = QLineEdit(self)
        self.lcdColorEdit.setText("FFFFFF")
        lcdColorLayout.addWidget(lcdLabel)
        lcdColorLayout.addWidget(self.lcdColorEdit)

        #Description Field
        descriptionLayout = QHBoxLayout()
        descriptionLabel = QLabel("Description", self)
        self.descriptionEdit = QTextEdit(self)
        descriptionLayout.addWidget(descriptionLabel)
        descriptionLayout.addWidget(self.descriptionEdit)


        #Button Box
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        #Set layout
        layout = QVBoxLayout()
        layout.addLayout(nameLayout)
        layout.addLayout(folderLayout)
        layout.addLayout(backgroundColorLayout)
        layout.addLayout(clockColorLayout)
        layout.addLayout(lcdColorLayout)
        layout.addLayout(descriptionLayout)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

    def getFolder(self):
        dir = QDir('./')
        self.folderEdit.setText(dir.relativeFilePath(QFileDialog().getExistingDirectory(self.parent, 'Please select the folder the category will be using!')))

    def getCategory(self):
        return Category(name = self.nameEdit.text(),
                        description = self.descriptionEdit.toPlainText(),
                        backgroundColorHex = self.descriptionEdit.toPlainText(),
                        clockColorHex = self.clockColorEdit.toPlainText(),
                        lcdColorHex = self.lcdColorEdit.toPlainText(),
                        folderName = self.folderEdit.toPlainText()
                        )

    def loadInfo(self, cat:Category):
        self.nameEdit.setText(cat.name)
        self.descriptionEdit.setText(cat.description)
