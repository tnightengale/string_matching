# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 09:09:12 2019

@author: TeghanN
"""

from page2.widgets2 import (QWizardPage, QLineEdit, QLabel, QVBoxLayout,
                            QHBoxLayout, QGroupBox, QGridLayout,
                            QTextEdit, QPushButton, QListWidget,
                            NewDragDropWidget, QLineEdit)

from page2.functions2 import (runrec, groupings)


class Page2(QWizardPage):
    
    def __init__(self):
        super().__init__()
        self.setTitle('File Grouping')
        self.groupingsInitialized = False # bool to ensure initGourpings() is called only on first click of 'next' button in wizard
        #self.QLists = {}
        # self.initGroupings() cannot init because page2 inits with program and field is empty until set on page1
        # need to call with signal from 'next clicked' on page1
        self.initWidgets()
        self.initLayout()
        
        
    def initWidgets(self):
        self.text_1 = QLineEdit(self)
        text = '''
        self.text_1.setText('Click the group files "Group Files" button.')
        self.text_1.setText('Click the group files "Group Files" button.')
        self.text_1.setText('Click the group files "Group Files" button.')
        self.text_1.setText('Click the group files "Group Files" button.')
        self.text_1.setText('Click the group files "Group Files" button.')
        self.text_1.setText('Click the group files "Group Files" button.')
        self.text_1.setText('Click the group files "Group Files" button.')
        self.text_1.setText('Click the group files "Group Files" button.')
        self.text_1.setText('Click the group files "Group Files" button.')
        self.text_1.setText('Click the group files "Group Files" button.')
        self.text_1.setText('Click the group files "Group Files" button.')
        '''
        self.text_1.setText(text)
        #self.text_1.setReadOnly(True)
        
        self.button_1 = QPushButton()
        self.button_1.setText('Group Files')
        self.button_1.clicked.connect(self.initGroupings)
        
        self.button_2 = QPushButton()
        self.button_2.setText('print list items')
        self.button_2.clicked.connect(self.printItems)
        
        self.button_3 = QPushButton()
        self.button_3.setText('print page children')
        self.button_3.clicked.connect(self.printPageChildren)
        
    def initLayout(self):
        self.list_group = QGroupBox()
        self.list_layout = QHBoxLayout()
        self.list_group.setLayout(self.list_layout)
        
        layout = QGridLayout()
        layout.addWidget(self.text_1, 0, 0, 1, 2)
        layout.addWidget(self.button_1, 1, 0, 5, 1)
        layout.addWidget(self.button_2, 1, 1, 5, 1)
        layout.addWidget(self.button_3, 1, 2, 5, 1)
        layout.addWidget(self.list_group, 6, 0, 5, 2)
        self.setLayout(layout)
    
    def printItems(self):
        for key in self.QLists.keys():
            print(f'Key is {key}')
            for i in range(self.QLists[key].count()):
                print(f'item {i} is {self.QLists[key].item(i).text()}')
    
    def printPageChildren(self):
        print(self.findChildren(NewDragDropWidget))
    
    def initGroupings(self):
        #if self.groupingsInitialized == False:
            #try:
                self.QLists = {}
                for i in range(self.list_layout.count()): 
                    self.list_layout.itemAt(i).widget().close()
                    
                    
                a = list(runrec(self.field("folder_path")))
                self.grouping = groupings(a)
                
                
                for k in sorted(self.grouping, key = lambda k: len(self.grouping[k]), reverse = True):
                    print(k, len(self.grouping[k]))
                    
                    self.QLists['list_' + str(k)] = NewDragDropWidget()
                    for excel_file_path in self.grouping[k]:
                        
                        self.QLists['list_' + str(k)].addItem(excel_file_path)
                    self.list_layout.addWidget(self.QLists['list_' + str(k)])
           # finally:
                #self.groupingsInitialized = True
                
                
    def initLists(self):
        #QLists = {}
        for k in sorted(self.groupings, key = lambda k: len(self.groupings[k])):
            pass
        
        
        