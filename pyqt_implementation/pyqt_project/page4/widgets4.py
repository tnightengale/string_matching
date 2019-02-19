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


"""
-- ==============
-- Custom Classes
-- ==============
"""

class QCSVTableWidget(QTableWidget):
    def __init__(self, data):
        self._data = data
        self._rows = len(data.values)
        self._cols = len(data.columns)
        super().__init__(self._rows,self._cols)
        
        # init data
        self.readData()
    
    def readData(self):
        for i in range(self._rows):
            for j in range(self._cols):
                self.setItem(i,j,QCSVItem(coordinate = (i,j),\
                                                  value = self._data.iloc[i,j]))
    
    
class QCSVItem(QTableWidgetItem):
    
    def __init__(self,coordinate,value):
        super().__init__(str(value))
        self.value_type = type(value)
        self.coordinate = coordinate
        self. coordinate_name = chr(ord('A') + coordinate[1]) + str(coordinate[0] + 1)
    
    

class QExportItem(QTableWidgetItem):
    
    def __init__(self,_QCSItem):
        self.value_type = _QCSItem.value_type
        self.coordinate = _QCSItem.coordinate
        self.coordinate_name = _QCSItem.coordinate_name
        
        super().__init__(self.coordinate_name)
    

        
    
    
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
    
"""
-- =========
-- Functions
-- =========
"""

def alphabetize(n):
    return [chr(ord('A')+i) for i in range(n)]
