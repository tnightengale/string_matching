# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 09:15:56 2019

@author: TeghanN
"""

import pandas as pd
from PyQt5.QtCore import pyqtSignal
from page3.widgets3 import (QWizardPage, QLineEdit, QLabel, QVBoxLayout,
                            QHBoxLayout, QGroupBox, QGridLayout,
                            QTextEdit, QPushButton, QListWidget,
                            MoveableListWidget,
                            ShortenedListItem, QMessageBox)


class Page3(QWizardPage):
    
    attribute = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.setTitle('Sheet Selection')
        self.initWidgets()
        self.initLayout()
        self.registerField("sheet_to_use*",self.list_main)
        
        
    def initWidgets(self):
        self.label_1 = QLabel()
        text = '''
        1. Click "Group Files" to view excel files in the provided folder
        2. Drag and drop files to the "Files To Use" list
        3. Click "Next" to proceed with the choosen files
        '''
        self.label_1.setText(text)
        
        self.label_2 = QLabel()
        self.label_2.setText('<h2> Sheets to Accept </h2>')
        
        self.button_1 = QPushButton()
        self.button_1.setText('List Sheets')
        self.button_1.clicked.connect(self.findSheets)
    
        self.list_main = MoveableListWidget()
        self.list_sheets =  MoveableListWidget()
        
    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.label_1, 0, 0, 1, 2)
        layout.addWidget(self.button_1, 1, 0)
        layout.addWidget(self.label_2, 2, 0, 1, 1)
        layout.addWidget(self.list_main, 3, 0)
        layout.addWidget(self.list_sheets, 3, 1)
        self.setLayout(layout)
    
    def findSheets(self):
        '''
        Called from button_1 ("List Sheets").
        Lists the sheets available in the "files_to_use" field
        created on Page2.
        '''
        all_sheets = []
        
        self.attribute.emit('test value')
        self.list_sheets.addItem('balls')
        #print(f'files to use object is: {self.field("files_to_use")}')
        
        '''
        for index in range(self.field('files_to_use').count()):    
            try:
                file = self.field('files_to_use').item(index).full_path
            
                sheets_found = list(pd.read_excel(file, sheet_name = None).keys())
                
                self.list_sheets.addItem(' '.join(sheets_found))
                
                all_sheets += sheets_found
                
            except Exception as e:
                print(e)
                
            print(all_sheets)
        return
        '''
    
        
    def showError(self, error_message):
       msg = QMessageBox()
       msg.setIcon(QMessageBox.Warning)
       msg.setText(error_message)
       msg.setWindowTitle("Error")
       msg.setStandardButtons(QMessageBox.Ok)
       msg.exec_()
        
        