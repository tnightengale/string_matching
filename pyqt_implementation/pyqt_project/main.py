# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:56:51 2019

@author: TeghanN
"""

from PyQt5.QtWidgets import QWizard, QApplication
from page1.page1 import Page1
from page2.page2 import Page2
from page3.page3 import Page3
from page4.page4 import Page4


class MagicWizard(QWizard):
    def __init__(self):
        super().__init__()
        self.setWizardStyle(self.ModernStyle)
        self.setWindowTitle("Survey Extractor")
        self.resize(800,600)
        
        # init pages
        #self.Page1 = Page1()
        #self.Page2 = Page2()
        #self.Page3 = Page3()
        #self.Page4 = Page4()
        
        # add pages
        #self.addPage(self.Page1)
        #self.addPage(self.Page2)
        #self.addPage(self.Page3)
        #self.addPage(self.Page4)
        
        self.addPage(Page1())
        self.addPage(Page2())
        self.addPage(Page3())
        self.addPage(Page4())
        
        # create signal to init file groupings on Page2 on click of Page1 'Next'
        #self.button(QWizard.NextButton).clicked.connect(self.Page2.initGroupings)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    wizard = MagicWizard()
    wizard.show()
    sys.exit(app.exec_())