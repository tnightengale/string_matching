# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:07:13 2019

@author: TeghanN
"""

from PyQt5 import QtCore
from PyQt5 import QtGui
from itertools import cycle
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtWidgets import (QWizardPage, QMainWindow, QGridLayout, QWidget, QTextEdit, QPushButton, 
                             QInputDialog, QMessageBox, QLineEdit, QLabel, QComboBox, 
                             QSlider, QLCDNumber, QVBoxLayout, QHBoxLayout, QGroupBox,
                             QTableWidget, QTableWidgetItem, QTableView)

class QITableWidget(QTableWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Add additional funcitonalityA

class PandasModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.values[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None
    
    