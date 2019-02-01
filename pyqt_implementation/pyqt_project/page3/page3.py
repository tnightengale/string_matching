# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 09:15:56 2019

@author: TeghanN
"""

from page3.widgets3 import QWizardPage, QLineEdit, QLabel, QVBoxLayout, QTextEdit


class Page3(QWizardPage):
    def __init__(self):
        super().__init__()
        self.initWidgets()
        self.initLayout()
        
    def initWidgets(self):
        self.label_1 = QLabel(self)
        self.label_1.setText('<h2> Sheet Selection <\h2>')
    
    def initLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.label_1)
        self.setLayout(layout)
        