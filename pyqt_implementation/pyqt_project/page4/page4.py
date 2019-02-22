# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:04:29 2019

@author: TeghanN
"""


#from PyQt5 import QtGui
#from PyQt5.QtCore import pyqtProperty
from page4.widgets4 import (QWizardPage, QTableWidget, QLabel, QGridLayout, 
                            QVBoxLayout, QPushButton, QGroupBox,PandasModel,
                            QTableView, QTableWidgetItem, QtCore, QMessageBox,
                            cycle, QCSVTableWidget, alphabetize, QExportItem,
                            QtGui)

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
    
    #error = QtCore.pyqtSignal()
    mac_path = r'/Users/tnightengale/Desktop/Projects/string_matching/pyqt_implementation/mock_excels/mock3.xlsx'
    
    mac_file_paths = [r'/Users/tnightengale/Desktop/Projects/string_matching/pyqt_implementation/mock_excels/mock1.xlsx',
                  r'/Users/tnightengale/Desktop/Projects/string_matching/pyqt_implementation/mock_excels/mock2.xlsx',
                  r'/Users/tnightengale/Desktop/Projects/string_matching/pyqt_implementation/mock_excels/mock3.xlsx']
    
    mac_write_path = r'/Users/tnightengale/Desktop/Projects/string_matching/pyqt_implementation/mock_excels/test.csv'
    
    
    
    windows_path = r"\Users\TeghanN\Desktop\string_matching\pyqt_implementation\mock_excels\mock3.xlsx"
    
    window_file_paths = [r"\Users\TeghanN\Desktop\string_matching\pyqt_implementation\mock_excels\mock1.xlsx",
                         r"\Users\TeghanN\Desktop\string_matching\pyqt_implementation\mock_excels\mock2.xlsx",
                         r"\Users\TeghanN\Desktop\string_matching\pyqt_implementation\mock_excels\mock3.xlsx"]
    
    window_write_path = r'C:\Users\TeghanN\Desktop\string_matching\pyqt_implementation\mock_excels\test.csv'
    
    def __init__(self):
        super().__init__()
        #self.error.connect(self.showError)
        self.pandaframe = pd.read_excel(self.windows_path)
        #self.pandaframe = pd.read_excel(self.mac_path)
        self.initWidgets()
        self.initLayout()
        
        self.color = 0
        
    def cellname(i, j):
        return f'{chr(ord("A")+j)}{i+1}'

    def initWidgets(self):
        self.label_1 = QLabel()
        self.label_1.setText("Importing Table")
        self.label_2 = QLabel()
        self.label_2.setText("Exporting Table")
        
        self.button_1 = QPushButton()
        self.button_1.setText('Delete Row')
        self.button_1.clicked.connect(self.deleteRow)
        
        self.button_2 = QPushButton()
        self.button_2.setText('Delete Column')
        self.button_2.clicked.connect(self.deleteColumn)
        
        self.button_3 = QPushButton()
        self.button_3.setText('Set Selected coordinates')
        self.button_3.clicked.connect(self.setWidgets)
        
        self.button_4 = QPushButton()
        self.button_4.setText('export table')
        self.button_4.clicked.connect(self.exportToCSV)
        
        self.button_5 = QPushButton()
        self.button_5.setText('Add Column')
        self.button_5.clicked.connect(self.addColumn)
        
        self.button_6 = QPushButton()
        self.button_6.setText('Add Rows')
        self.button_6.clicked.connect(self.addRow)
        
        self.table_1 = QCSVTableWidget(self.pandaframe)
        self.table_1.setHorizontalHeaderLabels(alphabetize(self.table_1._cols))
        #self.table_1 = QTableView()
        self.table_2 = QTableWidget()
        self.model = PandasModel(self.pandaframe)
        #self.table_1.setModel(self.model)
        #self.table_1.setShowGrid(True)
        
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
        b_layout.addWidget(self.button_6)
        b_group.setLayout(b_layout)
        
        layout = QGridLayout()
        layout.addWidget(self.label_1,0,0)
        layout.addWidget(self.label_2,0,2)
        layout.addWidget(self.table_1,1,0)
        layout.addWidget(self.table_2,1,2)
        layout.addWidget(b_group,1,1)
        self.setLayout(layout)
    
    def newColor(self):
        self.color = (self.color + 190) % 360 
        print(f'newColor() called and self.color is {self.color}')
        new_color = QtGui.QColor(1,1,1)
        new_color.setHsv(self.color,60,255)
        print(f'in newColor(), and new_color is {new_color}')
        return new_color
    
    
    def addColumn(self):
        current_column = self.table_2.columnCount()
        selected_labels = self.table_1.selectedIndexes()
        try: # ensure only one cell selected as header
            print(f'selected labels are: {selected_labels} and len is: {len(selected_labels)}')
            assert(len(selected_labels) == 1)
            selected_label = str(selected_labels[0].data())
            self.table_2.insertColumn(current_column)
            self.table_2.setHorizontalHeaderItem(current_column,QTableWidgetItem(selected_label))
        except AssertionError:
            print('except triggered')
            error = 'You cannot add more than one column at a time.'
            self.showError(error)
    
    def deleteColumn(self):
        current_column = self.table_2.columnCount() - 1
        print(f'current col number is {current_column}')
        self.table_2.removeColumn(current_column)
    
    def addRow(self):
        current_row = self.table_2.rowCount()
        self.table_2.insertRow(current_row)
        
    def deleteRow(self):
        current_row = self.table_2.rowCount() - 1 
        self.table_2.removeRow(current_row)
        
        
    def printIndex(self):
        #print(f'index is {[self.table_1.indexAt(a) for a in self.table_1.selectedIndexes()]}')
        print(f'data in index is {[(a.row(),a.column()) for a in self.table_1.selectedIndexes()]}')
        print(f'data in index is {self.table_1.selectedIndexes()}')
    
    def widgetIndex(self):
        print(f'current item is: {self.table_2.currentItem()}')
    
    def setWidgets(self):
        tb_1_coordinates = [(a.row(),a.column()) for a in self.table_1.selectedIndexes()]
        tb_2_coordinates = [(a.row(),a.column()) for a in self.table_2.selectedIndexes()]
        try:
            assert(len(tb_1_coordinates) <= len(tb_2_coordinates))
            curr_color = self.newColor()
            for c1,c2 in zip(cycle(tb_1_coordinates),tb_2_coordinates):
                # self.table_2.setItem(c2[0],c2[1],QTableWidgetItem(str(c1)))
                self.table_2.setItem(c2[0],c2[1],QExportItem(self.table_1.item(c1[0],c1[1])))
                
                # check for current color (because want to reuse)
                # print(f'color OF TABLE1 ITEM IS: {self.table_1.item(c1[0],c1[1]).background().color().getHsv()}')
                
                
                # adjust colors
                self.table_1.item(c1[0],c1[1]).setBackground(curr_color)
                self.table_2.item(c2[0],c2[1]).setBackground(curr_color)
                
                print(f' coordinate is {self.table_1.item(c1[0],c1[1]).coordinate_name}')
            print(f'table 1 coordinates are: {tb_1_coordinates}')
            print(f'table 2 coordinates are: {tb_2_coordinates}')
        except AssertionError:
            error = 'Selected cells in importing table exceed selected cells in exporting table.'
            self.showError(error)
            
    def exportToFrame(self):
        data = []
        for row in range(self.table_2.rowCount()):
                rowdata = []
                for column in range(self.table_2.columnCount()):
                    item = self.table_2.item(row, column)
                    print(item) ##
                    if item is not None:
                        rowdata.append({'coordinate':item.coordinate,'type':item.value_type})
                    else:
                        rowdata.append('')
                data.append(rowdata)
                            
        frame = pd.DataFrame(data)
        print(data)
        print(frame)
        return frame
    
    def showError(self, error_message):
       msg = QMessageBox()
       msg.setIcon(QMessageBox.Warning)
       msg.setText(error_message)
       msg.setWindowTitle("Error")
       msg.setStandardButtons(QMessageBox.Ok)
       msg.exec_()
       
       
    def exportToCSV(self):
       # declare test vars
        frame_map = self.exportToFrame()
        #file_paths = self.mac_file_paths
        #write_path = self.mac_write_path
        
        file_paths = self.window_file_paths
        write_path = self.window_write_path
        
        
        frame_to_export = pd.DataFrame(columns = frame_map.columns)
        
        for file in file_paths:
            current_read_frame = pd.read_excel(file)
            current_write_frame = pd.DataFrame(index = frame_map.index, columns = frame_map.columns)
            
            for i in range(len(frame_map.values)):
                for j in range(len(frame_map.columns)):
                    
                    print(f'frame is {frame_map}') ####
                    print(f'type of i,j is {(type(i),type(j))}') ####
                    print(f'frame cell i,j is {frame_map.iloc[i,j]}')
                    try:
                        current_coord = frame_map.iloc[i,j]['coordinate']
                        current_write_frame.iloc[i,j] = current_read_frame.iloc[current_coord]
                    except TypeError:
                        current_write_frame.iloc[i,j] = ""
            
            frame_to_export = frame_to_export.append(current_write_frame)
            print(current_write_frame)
            
        frame_to_export.to_csv(write_path)
        print(frame_to_export)
        