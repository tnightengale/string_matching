# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:03:23 2019

@author: TeghanN
"""


from page1.widgets1 import (QWizardPage, QLineEdit, QLabel, QVBoxLayout, 
                            QTextEdit, QtGui, QFileDialog, QPushButton)


class Page1(QWizardPage):
    def __init__(self):
        super().__init__()
        self.initWidgets()
        self.initLayout()
        self.registerField("folder_path*",self.line_1)
        
    def initWidgets(self):
        self.label_1 = QLabel(self)
        self.label_1.setText('<b> Folder path: </b>')
        
        self.button_1 = QPushButton()
        self.button_1.setText('Choose folder')
        self.button_1.clicked.connect(self.chooseFolder)
        
        self.line_1 = QLineEdit()
        self.line_1.setPlaceholderText('Enter or choose folder path containing surveys')
        
        instructions = '<h1>Instructions here.</h1>'
        self.text_1 = QTextEdit(self)
        self.text_1.setText(instructions)
        self.text_1.setReadOnly(True)
    
        
    def initLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.label_1)
        layout.addWidget(self.line_1)
        layout.addWidget(self.button_1)
        layout.addWidget(self.text_1)
        self.setLayout(layout)
        
    
    def chooseFolder(self):
        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.line_1.setText(folder)
        
        
    def fileGrouping():
        pass
        # run file grouping algorithm on path
        # when next button is pressed
        # Make next button unpressable until
        # path is supplied
        # conditional page outcome based
        # on file grouping algo
        
        
        