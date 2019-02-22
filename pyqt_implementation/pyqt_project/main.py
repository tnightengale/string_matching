# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:56:51 2019

@author: TeghanN
"""

from PyQt5.QtWidgets import QWizard, QApplication
from PyQt5.QtCore import pyqtSignal
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
        self.Page1 = Page1()
        self.Page2 = Page2()
        self.Page3 = Page3()
        self.Page4 = Page4()
        
        # add pages
        self.addPage(self.Page1)
        self.addPage(self.Page2)
        self.addPage(self.Page3)
        self.addPage(self.Page4)
        
        #self.addPage(Page1())
        #self.addPage(Page2())
        #self.addPage(Page3())
        #self.addPage(Page4())
        
        # create signal to init file groupings on Page2 on click of Page1 'Next'
        self.Page3.attribute.connect(self.signalTest)
    
    def signalTest(self, value):
        print('signalTest called')
        #self.Page3.list_sheets.clear()
        for i in range(self.Page2.list_main.count()):
            self.Page3.list_sheets.addItem(self.Page2.list_main.item(i))
            self.Page3.list_sheets.addItem('balls from signalTest')
            '''
            Problem is likely that item cannot be reassigned from parent
            to new widget. Needs to be copied!
            '''
            print(self.Page2.list_main.item(i))
        print(f'count of self.Page3.list_sheets is {self.Page3.list_sheets.count()}')
    def passWidgets(self,sending_page, recieving_page, sending_attribute, receiving_attribute):
        #self.recieving_page.recieving_attribute = self.sending_page.sending_attribute
        pass
        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    wizard = MagicWizard()
    wizard.show()
    sys.exit(app.exec_())