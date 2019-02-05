# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:04:29 2019

@author: TeghanN
"""


#from PyQt5 import QtGui
#from PyQt5.QtCore import pyqtProperty
from page4.widgets4 import (QWizardPage, QITableWidget, QLabel, QGridLayout, 
                            QVBoxLayout, QPushButton, QGroupBox,PandasModel,
                            QTableView, QTableWidgetItem, QtCore, QMessageBox)

import pandas as pd

'''
TO DO:
    
Explore mapping between indexes of selected cells (template) and using those indexes
to pull data from each frame in the list of sheets that are converted to frames. 

Also included in this process is validating data that does not match the selected
template.

Figure out how to create excel-like lables on table_1.

Figure out how to create columns based on selected cells.

Figure out how to map selected cells in table_1 to selected cells in table_2.
'''

class Page4(QWizardPage):
    
    error = QtCore.pyqtSignal()
    
    
    def __init__(self):
        super().__init__()
        
        self.pandaframe = pd.read_excel(r"\Users\TeghanN\Desktop\string_matching\pyqt_implementation\mock_excels\mock3.xlsx")
        self.initWidgets()
        self.initLayout()
        
    def cellname(i, j):
        return f'{chr(ord("A")+j)}{i+1}'

    def initWidgets(self):
        self.label_1 = QLabel()
        self.label_1.setText("Importing Table")
        self.label_2 = QLabel()
        self.label_2.setText("Exporting Table")
        
        self.button_1 = QPushButton()
        self.button_1.setText('Print table 1 cell index')
        self.button_1.clicked.connect(self.printIndex)
        
        self.button_2 = QPushButton()
        self.button_2.setText('Print table 1 cell index')
        self.button_2.clicked.connect(self.widgetIndex)
        
        self.button_3 = QPushButton()
        self.button_3.setText('Set Selected cordinates')
        self.button_3.clicked.connect(self.setWidgets)
        
        self.button_4 = QPushButton()
        self.button_4.setText('export table')
        self.button_4.clicked.connect(self.exportToFrame)
        
        self.button_5 = QPushButton()
        self.button_5.setText('Add Column')
        self.button_5.clicked.connect(self.addColumn)
        
        self.table_1 = QTableView()
        self.table_2 = QITableWidget()
        self.model = PandasModel(self.pandaframe)
        self.table_1.setModel(self.model)
        self.table_1.setShowGrid(True)
        
        # create excel style cell col and index
        #self.table_1.setHorizontalHeader(list(map(lambda j: chr(ord('A') + j),range(self.model.columnCount()))))
        print(f'header is {self.table_1.horizontalHeader()}')
        print(f'\n there are {self.model.rowCount()} rows')
        print(f'\n there are {self.model.columnCount()} columns')
        
    def initLayout(self):
        b_group = QGroupBox()
        b_layout = QVBoxLayout()
        b_layout.addWidget(self.button_1)
        b_layout.addWidget(self.button_2)
        b_layout.addWidget(self.button_3)
        b_layout.addWidget(self.button_4)
        b_layout.addWidget(self.button_5)
        b_group.setLayout(b_layout)
        
        layout = QGridLayout()
        layout.addWidget(self.label_1,0,0)
        layout.addWidget(self.label_2,0,2)
        layout.addWidget(self.table_1,1,0)
        layout.addWidget(self.table_2,1,2)
        layout.addWidget(b_group,1,1)
        self.setLayout(layout)
    
    def addColumn(self):
        current_column = self.table_2.columnCount()
        self.table_2.insertColumn(current_column)
        
        selected_labels = self.table_1.selectedIndexes()
        
        try:
            # ensure only one cell selected as header
            print(f'selected labels are: {selected_labels} and len is: {len(selected_labels)}')
            assert(len(selected_labels) == 1)
            selected_label = str(selected_labels[0].data())
            self.table_2.setHorizontalHeaderItem(current_column,QTableWidgetItem(selected_label))
            
        except AssertionError:
            self.error.connect(self.showError)
            self.error.emit()
            #self.showError()
        
    def printIndex(self):
        #print(f'index is {[self.table_1.indexAt(a) for a in self.table_1.selectedIndexes()]}')
        print(f'data in index is {[(a.row(),a.column()) for a in self.table_1.selectedIndexes()]}')
        print(f'data in index is {self.table_1.selectedIndexes()}')
    
    def widgetIndex(self):
        print(f'current item is: {self.table_2.currentItem()}')
    
    def setWidgets(self):
        for cordinate in [(a.row(),a.column()) for a in self.table_1.selectedIndexes()]:
            self.table_2.setItem(cordinate[0],cordinate[1],QTableWidgetItem(str(cordinate)))
            
    def exportToFrame(self):
        data = []
        for row in range(self.table_2.rowCount()):
                rowdata = []
                for column in range(self.table_2.columnCount()):
                    item = self.table_2.item(row, column)
                    if item is not None:
                        rowdata.append(
                            str(item.text()))
                    else:
                        rowdata.append('')
                data.append(rowdata)
                            
        frame = pd.DataFrame(data)
        print(data)
        print(frame)
    
    def showError(self):
       msg = QMessageBox()
       msg.setIcon(QMessageBox.Warning)
    
       msg.setText("You cannot do that!")
       msg.setWindowTitle("Error")
       msg.setStandardButtons(QMessageBox.Ok)
       