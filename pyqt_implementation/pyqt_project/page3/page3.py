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
        1. Drag the sheets to use from "Found Sheets" into "Sheets To Accept" 
        2. Click on any given sheet in "Sheets to Accept" to enable "Next"
        3. Click "Next" to proceed with the choosen sheets
        '''
        self.label_1.setText(text)
        
        self.label_2 = QLabel()
        self.label_2.setText('<h2> Sheets To Accept </h2>')
        
        self.label_3 = QLabel()
        self.label_3.setText('<h2> Found Sheets </h2>')
        
        self.button_1 = QPushButton()
        self.button_1.setText('Load Selected Sheets')
        self.button_1.clicked.connect(self.checkSheets)
    
        self.list_main = MoveableListWidget()
        self.list_sheets =  MoveableListWidget()
        
        
        
    def initLayout(self):
        layout = QGridLayout()
        layout.addWidget(self.label_1, 0, 0, 1, 2)
        #layout.addWidget(self.button_1, 1, 0)
        layout.addWidget(self.label_2, 2, 0, 1, 1)
        layout.addWidget(self.label_3, 2, 1, 1, 1)
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
        
        for sheet_name in ordered_sheets:
            self.list_sheets.addItem(sheet_name)
            
            
            
    def checkSheets(self):
        '''
        '''
        if self.list_main.count() == 0:
            error = "You must add at least one sheet to the 'Sheets to Accept' list."
            self.showError(error)
        else:
            for file in self.list_of_file_paths:
                pass
        return 
    
    
    def showError(self, error_message, title="Error", icon=QMessageBox.Warning):
       msg = QMessageBox()
       msg.setIcon(icon)
       msg.setText(error_message)
       msg.setWindowTitle(title)
       msg.setStandardButtons(QMessageBox.Ok)
       msg.exec_()
       
        