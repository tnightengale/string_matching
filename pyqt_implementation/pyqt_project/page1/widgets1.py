# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:07:13 2019

@author: TeghanN
"""

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtWidgets import (QWizardPage, QMainWindow, QGridLayout, QWidget, QTextEdit, QPushButton, 
                             QInputDialog, QMessageBox, QLineEdit, QLabel, QComboBox, 
                             QSlider, QLCDNumber, QVBoxLayout, QHBoxLayout, QGroupBox)

class QIComboBox(QComboBox):
    def __init__(self,parent=None):
        super(QIComboBox, self).__init__(parent)
        
class QILineEdit(QLineEdit):
    def __init__(self):
        super().__init__()
        # additional requirements