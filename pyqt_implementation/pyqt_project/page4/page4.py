# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:04:29 2019

@author: TeghanN
"""


#from PyQt5 import QtGui
#from PyQt5.QtCore import pyqtProperty
from page4.widgets4 import (QWizardPage, QITableWidget, QLabel, QGridLayout, 
                            QVBoxLayout, QPushButton, QGroupBox)


class Page4(QWizardPage):
    def __init__(self):
        super().__init__()
        self.initWidgets()
        self.initLayout()

    def initWidgets(self):
        self.label_1 = QLabel()
        self.label_1.setText("Importing Table")
        self.label_2 = QLabel()
        self.label_2.setText("Exporting Table")
        
        self.button_1 = QPushButton()
        self.button_1.setText('Action 1 >>')
        self.button_2 = QPushButton()
        self.button_2.setText('Action 2 <<')
        
        self.table_1 = QITableWidget(3,3)
        self.table_2 = QITableWidget(3,3)
        
        
    def initLayout(self):
        b_group = QGroupBox()
        b_layout = QVBoxLayout()
        b_layout.addWidget(self.button_1)
        b_layout.addWidget(self.button_2)
        b_group.setLayout(b_layout)
        
        layout = QGridLayout()
        layout.addWidget(self.label_1,0,0)
        layout.addWidget(self.label_2,0,2)
        layout.addWidget(self.table_1,1,0)
        layout.addWidget(self.table_2,1,2)
        layout.addWidget(b_group,1,1)
        self.setLayout(layout)