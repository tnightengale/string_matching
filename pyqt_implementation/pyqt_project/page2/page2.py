# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 09:09:12 2019

@author: TeghanN
"""

from page2.widgets2 import (QWizardPage, QLineEdit, QLabel, QVBoxLayout,
                            QHBoxLayout, QGroupBox, QGridLayout,
                            QTextEdit, QPushButton, QListWidget,
                            MoveableListWidget)

from page2.functions2 import (runrec, groupings)


class Page2(QWizardPage):
    
    def __init__(self):
        super().__init__()
        self.setTitle('File Grouping')
        self.groupingsInitialized = False # bool to ensure initGourpings() is called only on first click of 'next' button in wizard
        # self.initGroupings() cannot init because page2 inits with program and field is empty until set on page1
        # need to call with signal from 'next clicked' on page1
        self.initWidgets()
        self.initLayout()
        
        
    def initWidgets(self):
        self.text_1 = QTextEdit(self)
        self.text_1.setText('Click the group files "Group Files" button.')
        self.text_1.setReadOnly(True)
        
        self.button_1 = QPushButton()
        self.button_1.setText('Group Files')
        self.button_1.clicked.connect(self.initGroupings)
    
    def initLayout(self):
        self.list_group = QGroupBox()
        self.list_layout = QHBoxLayout()
        self.list_group.setLayout(self.list_layout)
        
        layout = QGridLayout()
        layout.addWidget(self.text_1, 0, 0)
        layout.addWidget(self.button_1, 1, 0)
        layout.addWidget(self.list_group, 2, 0)
        self.setLayout(layout)
        
    
    def initGroupings(self):
        if self.groupingsInitialized == False:
            QLists = {}
            try:
                a = list(runrec(self.field("folder_path")))
                self.grouping = groupings(a)
                for k in sorted(self.grouping, key = lambda k: len(self.grouping[k]), reverse = True):
                    print(k, len(self.grouping[k]))
                    
                    QLists['list_' + str(k)] = MoveableListWidget()
                    for excel_file_path in self.grouping[k]:
                        
                        QLists['list_' + str(k)].addItem(excel_file_path)
                    self.list_layout.addWidget(QLists['list_' + str(k)])
            finally:
                self.groupingsInitialized = True
                
                
    def initLists(self):
        #QLists = {}
        for k in sorted(self.groupings, key = lambda k: len(self.groupings[k])):
            pass
        
        
        