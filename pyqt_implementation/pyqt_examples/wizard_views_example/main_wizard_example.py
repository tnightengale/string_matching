# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:56:51 2019

@author: TeghanN
"""

from PyQt5 import QtWidgets
from page1 import Page1 
from page2 import Page2


class MagicWizard(QtWidgets.QWizard):
    def __init__(self, parent=None):
        super(MagicWizard, self).__init__(parent)
        self.addPage(Page1(self))
        self.addPage(Page2(self))
        self.setWindowTitle("PyQt5 Wizard Example - pythonspot.com")
        self.resize(640,480)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wizard = MagicWizard()
    wizard.show()
    sys.exit(app.exec_())