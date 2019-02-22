# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 09:08:41 2019

@author: TeghanN
"""

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtWidgets import (QWizardPage, QMainWindow, QGridLayout, QWidget, QTextEdit, QPushButton, 
                             QInputDialog, QMessageBox, QLineEdit, QLabel, QComboBox, 
                             QSlider, QLCDNumber, QVBoxLayout, QHBoxLayout, QGroupBox,
                             QListWidget, QAbstractItemView, QTableWidget, QListWidgetItem,
                             QMessageBox)

class MoveableListWidget(QListWidget):
    
    def __init__(self):
        super().__init__()
        self.setIconSize(QtCore.QSize(124, 124))
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setAcceptDrops(True)
        

class ShortenedListItem(QListWidgetItem):
    
    def __init__(self, text):
        super().__init__(text)
        self.full_path = text
        self.setText(self.full_path.split('\\')[-1])