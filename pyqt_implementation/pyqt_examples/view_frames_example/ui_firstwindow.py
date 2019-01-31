# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:43:25 2019

@author: TeghanN
"""

from PyQt5 import QtWidgets, QtCore, QtGui

class ui_Firstwindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 471)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 140, 191, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.nextWindow)