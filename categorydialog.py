# This Python file uses the following encoding: utf-8
from PySide6 import QtWidgets
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QFontComboBox, QDialogButtonBox, QToolButton, QColorDialog
from PySide6.QtGui import QColor
from functools import partial
from db import Category
from config import DEFAULT_ROUND_FONT, DEFAULT_CLOCK_FONT

class CategoryDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Category")
        self.setupUI()

    def setupUI(self):
        #Name
        nameLayout = QHBoxLayout()
        self.nameEdit = QLineEdit(self)
        nameLayout.addWidget(QLabel("Name", self))
        nameLayout.addSpacing(28)
        nameLayout.addWidget(self.nameEdit)

        #Description
        descriptionLayout = QHBoxLayout()
        self.descriptionEdit = QTextEdit(self)
        descriptionLayout.addWidget(QLabel("Description", self))
        descriptionLayout.addWidget(self.descriptionEdit)

        #Name Text Color Hex
        nameColorLayout = QHBoxLayout()
        self.nameColorEdit = QLineEdit(self)
        self.nameColorButton = QToolButton()
        self.nameColorEdit.textChanged.connect(partial(self.updateButtonColor, self.nameColorButton))
        self.nameColorButton.clicked.connect(partial(self.getColor, self.nameColorEdit))
        nameColorLayout.addWidget(QLabel("Category Name Color", self))
        nameColorLayout.addWidget(self.nameColorButton)
        nameColorLayout.addWidget(self.nameColorEdit)

        #Clock Background Color Hex
        backgroundColorLayout = QHBoxLayout()
        self.backgroundColorEdit = QLineEdit(self)
        self.backgroundColorButton = QToolButton()
        self.backgroundColorEdit.textChanged.connect(partial(self.updateButtonColor, self.backgroundColorButton))
        self.backgroundColorButton.clicked.connect(partial(self.getColor, self.backgroundColorEdit))
        backgroundColorLayout.addWidget(QLabel("Clock Background Color", self))
        backgroundColorLayout.addWidget(self.backgroundColorButton)
        backgroundColorLayout.addWidget(self.backgroundColorEdit)

        #Clock Text Color Hex
        clockColorLayout = QHBoxLayout()
        self.clockColorEdit = QLineEdit(self)
        self.clockColorButton = QToolButton()
        self.clockColorEdit.textChanged.connect(partial(self.updateButtonColor, self.clockColorButton))
        self.clockColorButton.clicked.connect(partial(self.getColor, self.clockColorEdit))
        clockColorLayout.addWidget(QLabel("Clock Number Color", self))
        clockColorLayout.addWidget(self.clockColorButton)
        clockColorLayout.addWidget(self.clockColorEdit)

        #Name Font
        nameFontLayout = QHBoxLayout()
        self.nameFontComboBox = QFontComboBox()
        self.nameFontComboBox.setCurrentFont(DEFAULT_ROUND_FONT)
        nameFontLayout.addWidget(QLabel("Name Font", self))
        nameFontLayout.addWidget(self.nameFontComboBox)

        #Clock Font
        clockFontLayout = QHBoxLayout()
        self.clockFontComboBox = QFontComboBox()
        self.clockFontComboBox.setCurrentFont(DEFAULT_CLOCK_FONT)
        clockFontLayout.addWidget(QLabel("Clock Font", self))
        clockFontLayout.addWidget(self.clockFontComboBox)

        #Button Box
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        #Set layout
        layout = QVBoxLayout()
        layout.addLayout(nameLayout)
        layout.addLayout(descriptionLayout)
        layout.addLayout(nameColorLayout)
        layout.addLayout(backgroundColorLayout)
        layout.addLayout(clockColorLayout)
        layout.addLayout(nameFontLayout)
        layout.addLayout(clockFontLayout)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

    def getCategory(self):
        return Category(name = self.nameEdit.text(),
                        description = self.descriptionEdit.toPlainText(),
                        nameColor = self.nameColorEdit.text(),
                        backgroundColor = self.backgroundColorEdit.text(),
                        clockColor = self.clockColorEdit.text(),
                        nameFont = self.nameFontComboBox.currentText(),
                        clockFont = self.clockFontComboBox.currentText()
                        )

    def loadInfo(self, cat:Category):
        self.nameEdit.setText(cat.name)
        self.descriptionEdit.setText(cat.description)
        self.nameColorEdit.setText(cat.nameColor)
        self.backgroundColorEdit.setText(cat.backgroundColor)
        self.clockColorEdit.setText(cat.clockColor)
        self.nameFontComboBox.setCurrentFont(cat.nameFont)
        self.clockFontComboBox.setCurrentFont(cat.clockFont)

    def updateButtonColor(self, button, color):
        if QColor(color).isValid():
            button.setStyleSheet(f'background-color: {color}')
        else:
            button.setStyleSheet('')

    def getColor(self, lineEdit):
        initColor = QColor(lineEdit.text())
        if initColor.isValid():
            color = QColorDialog.getColor(initColor)
        else:
            color = QColorDialog.getColor()
        lineEdit.setText(color.name())
