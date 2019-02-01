# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:56:51 2019

@author: TeghanN
"""

from PyQt5 import QtWidgets
from page1.page1 import Page1
from page2.page2 import Page2
from page3.page3 import Page3
from page4.page4 import Page4


class MagicWizard(QtWidgets.QWizard):
    def __init__(self):
        super().__init__()
        self.setWizardStyle(self.ModernStyle)
        self.addPage(Page1())
        self.addPage(Page2())
        self.addPage(Page3())
        self.addPage(Page4())
        self.setWindowTitle("Survey Extractor")
        self.resize(800,600)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wizard = MagicWizard()
    wizard.show()
    sys.exit(app.exec_())