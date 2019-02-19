# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 09:09:12 2019

@author: TeghanN
"""

from page2.widgets2 import (QWizardPage, QLineEdit, QLabel, QVBoxLayout, 
                            QTextEdit, QPushButton)


class Page2(QWizardPage):
    def __init__(self):
        super().__init__()
        self.initWidgets()
        self.initLayout()
        
        
    def initWidgets(self):
        self.label_1 = QLabel(self)
        self.label_1.setText('<h2> File Grouping <\h2>')
        
        self.button_1 = QPushButton()
        self.button_1.setText('print field')
        self.button_1.clicked.connect(self.printfield)
    
    def initLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.label_1)
        layout.addWidget(self.button_1)
        self.setLayout(layout)
        
    def printfield(self):
        print(f'THE FIELD CONTAINS: {self.field("folder_path")}')