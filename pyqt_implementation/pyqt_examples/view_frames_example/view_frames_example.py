# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:37:38 2019

@author: TeghanN
"""

'''
First of all the classes that Qt Designer offers are not widgets,
and it is recommended that if you modify the .ui when recompiling 
you will lose the modifications of the logic. So for the 2 previous
arguments I recommend you restore both files.
'''

from PyQt5 import QtWidgets

from ui_firstwindow import ui_Firstwindow
from ui_secondwindow import ui_Secondwindow

        
'''
Your problem is that to show a window you have to access the window object, 
but in your case if you want to do it in several files you may have problems 
with circular imports, undefined variables, etc. The correct thing is that all 
windows have the same scope.

Then we will create a main.py file where we will implement the classes that 
implement the widgets using the previous design. We create a class where the
windows will be created and we will connect the clicked signals to the show() 
method of the other window. In each class the clicked signal of the button is 
connected to the hide() method of the window.
'''

class Firstwindow(QtWidgets.QMainWindow, ui_Firstwindow):
    def __init__(self, parent=None):
        super(Firstwindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hide)


class Secondwindow(QtWidgets.QDialog, ui_Secondwindow):
    def __init__(self, parent=None):
        super(Secondwindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.hide)


class Manager:
    def __init__(self):
        self.first = Firstwindow()
        self.second = Secondwindow()

        self.first.pushButton.clicked.connect(self.second.show)
        self.second.pushButton_2.clicked.connect(self.first.show)

        self.first.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())