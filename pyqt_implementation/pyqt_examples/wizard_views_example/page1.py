# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:03:23 2019

@author: TeghanN
"""

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtProperty
from PyQt5 import QtCore, QtWidgets
from widgets import QIComboBox


class Page1(QtWidgets.QWizardPage):
    def __init__(self, parent=None):
        super(Page1, self).__init__(parent)
        self.comboBox = QIComboBox(self)
        self.comboBox.addItem("Python","/path/to/filename1")
        self.comboBox.addItem("PyQt5","/path/to/filename2")
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.comboBox)
        layout.addWidget(QtWidgets.QTableWidget(3,3,self))
        self.setLayout(layout)