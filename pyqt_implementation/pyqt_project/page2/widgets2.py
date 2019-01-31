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
                             QSlider, QLCDNumber, QVBoxLayout, QHBoxLayout, QGroupBox,
                             QTableWidget, QTableWidgetItem)

class QITableWidget(QTableWidget):
    def __init__(self, rows, columns):
        super().__init__(rows, columns)
        # Add additional funcitonality