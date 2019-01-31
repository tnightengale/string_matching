# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:04:29 2019

@author: TeghanN
"""
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtProperty
from PyQt5 import QtCore, QtWidgets

class Page2(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        super(Page2, self).__init__(parent)
        self.label1 = QtWidgets.QLabel()
        self.label2 = QtWidgets.QLabel()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        self.setLayout(layout)
        
    def initializePage(self):
        self.label1.setText("Example text")
        self.label2.setText("Example text")