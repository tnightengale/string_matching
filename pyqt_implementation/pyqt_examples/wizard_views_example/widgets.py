# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:07:13 2019

@author: TeghanN
"""

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtProperty
from PyQt5 import QtCore, QtWidgets

class QIComboBox(QtWidgets.QComboBox):
    def __init__(self,parent=None):
        super(QIComboBox, self).__init__(parent)