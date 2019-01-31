# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:42:28 2019

@author: TeghanN
"""

from PyQt5 import QtWidgets, QtCore

class ui_Secondwindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 650)
        Dialog.setMinimumSize(QtCore.QSize(552, 0))

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 240, 70, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.previouswindow)