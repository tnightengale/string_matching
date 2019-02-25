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
                            MoveableListWidget,Counter,
                            ShortenedListItem, QMessageBox)


class Page3(QWizardPage):
    
    attribute = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.setTitle('Sheet Selection')
        self.initWidgets()
        self.initLayout()
        self.registerField("sheet_to_use*",self.list_main)
        self.list_of_file_paths = []
        
        
        
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
        self.button_1.setText('Load Selected Sheets')
        self.button_1.clicked.connect(self.checkSheets)
    
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
    
    
    
    def loadExcelFiles(self):
        '''
        '''
        self.excel_dict = {}
        for file in self.list_of_file_paths:
            try:
                self.excel_dict[file] = pd.read_excel(file, sheet_name = None)
            except Exception as e:
                error = f'The file {file} could not be read. Error: {e}'
                self.showError(error)
                
                
    def displaySheets(self):
        '''
        Called from QWizard.transitionToPage3().
        Lists the sheets available from the selected
        files on Page2.
        '''
        temp_tuples = list(self.excel_dict.items())
        temp_list_of_key_lists = [i[1].keys() for i in temp_tuples]
        temp_flattened_list = [item for sublist in temp_list_of_key_lists for item in sublist]
        
        ordered_sheets = list(Counter(temp_flattened_list).keys())
        
        self.QSheets = {}
        for sheet_name in ordered_sheets:
            
            self.list_sheets.addItem(sheet_name)
            
    def checkSheets(self):
        return 
    
    
    def showError(self, error_message):
       msg = QMessageBox()
       msg.setIcon(QMessageBox.Warning)
       msg.setText(error_message)
       msg.setWindowTitle("Error")
       msg.setStandardButtons(QMessageBox.Ok)
       msg.exec_()
       
        