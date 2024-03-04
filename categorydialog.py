# This Python file uses the following encoding: utf-8
from PySide6 import QtWidgets
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QDialogButtonBox
from db import Category

class CategoryDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
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
        layout.addLayout(descriptionLayout)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

    def getCategory(self):
        name = self.nameEdit.text()
        description = self.descriptionEdit.toPlainText()
        return Category(name=name, description=description)

    def loadInfo(self, cat:Category):
        self.nameEdit.setText(cat.name)
        self.descriptionEdit.setText(cat.description)
