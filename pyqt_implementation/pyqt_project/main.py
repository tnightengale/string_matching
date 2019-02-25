# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:56:51 2019

@author: TeghanN
"""

from PyQt5.QtWidgets import QWizard, QApplication
from PyQt5.QtCore import pyqtSignal
from page1.page1 import Page1
from page2.page2 import Page2
from page2.widgets2 import QListWidgetItem
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
        
        # connect ListWdigetChanged signal to slot signalTest
        #self.Page2.list_main.ListWidgetChanged.connect(self.signalTest)
    
    
        self.button(QWizard.NextButton).clicked.connect(self.nextController)
        
    def nextController(self):
        '''
        Slot for the NextButton signal. Controller to
        call transition pages.
        '''
        current_page = str(self.currentPage())
        
        if "Page2" in current_page:
            self.transitionToPage2()
            
        elif "Page3" in current_page:
            self.transitionToPage3()
            
        elif "Page4" in current_page:
            self.transitionToPage4()
            
        return False
      
    def transitionToPage2(self):
        print('TTP2 called')
        
    def transitionToPage3(self):
        print('TTP3 called')
        
        # create list of file_paths to use
        self.Page3.list_of_file_paths = []
        for i in range(self.Page2.list_main.count()):
            current_file_path = self.Page2.list_main.item(i).whatsThis()
            self.Page3.list_of_file_paths.append(current_file_path)
        
        # load files into pd.frames
        #print(self.Page3.list_of_file_paths)
        self.Page3.loadExcelFiles()
        
        # display available sheets
        self.Page3.displaySheets()
    
    
    def transitionToPage4(self):
        print('TTP4 called')
        
        
        
    
    def passWidgets(self,sending_page, recieving_page, sending_attribute, receiving_attribute):
        #self.recieving_page.recieving_attribute = self.sending_page.sending_attribute
        pass
        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    wizard = MagicWizard()
    wizard.show()
    sys.exit(app.exec_())