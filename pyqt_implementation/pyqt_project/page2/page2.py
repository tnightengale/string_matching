# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 09:09:12 2019

@author: TeghanN
"""

from page2.widgets2 import (QWizardPage, QLineEdit, QLabel, QVBoxLayout,
                            QHBoxLayout, QGroupBox, QGridLayout,
                            QTextEdit, QPushButton, QListWidget,
                            MoveableListWidget,
                            ShortenedListItem, QMessageBox)

from page2.functions2 import (runrec, groupings)


class Page2(QWizardPage):
    
    def __init__(self):
        super().__init__()
        self.setTitle('File Grouping')
        self.initWidgets()
        self.initLayout()
        self.registerField("files_to_use*",self.list_main)
        
    def initWidgets(self):
        self.label_1 = QLabel()
        text = '''
        1. Click "Group Files" to view excel files in the provided folder
        2. Drag and drop files to the "Files To Use" list
        3. Click "Next" to proceed with the choosen files
        '''
        self.label_1.setText(text)
        
        self.label_2 = QLabel()
        self.label_2.setText('<h2> Files To Use </h2>')
        
        self.button_1 = QPushButton()
        self.button_1.setText('Group Files')
        self.button_1.clicked.connect(self.initGroupings)
        
        self.button_2 = QPushButton()
        self.button_2.setText('check reg field')
        self.button_2.clicked.connect(self.check)
    
        self.list_main = MoveableListWidget()
        
    def initLayout(self):
        self.list_group = QGroupBox()
        self.list_layout = QHBoxLayout()
        self.list_group.setLayout(self.list_layout)
        
        layout = QGridLayout()
        layout.addWidget(self.label_1, 0, 0, 1, 2)
        layout.addWidget(self.button_1, 1, 0)
        layout.addWidget(self.button_2, 1, 1)
        layout.addWidget(self.label_2, 2, 0, 1, 1)
        layout.addWidget(self.list_main, 3, 0, 1, 1)
        layout.addWidget(self.list_group, 3, 1, 1, 4)
        self.setLayout(layout)
    
    def initGroupings(self):
        '''
        Called from button_1 ("Group Files").
        Creates groupings of excel files found at each 
        depth of the folder_path field on Page1. Removes
        existing groupings before creating new groupings
        and displaying them in list widgets.
        '''
        # create dict to generate list widgets from in loop
        self.QLists = {}
        
        # clear files currently in "Files to Use" ListWidget
        self.list_main.clear()
        
        # clear existing list widgets
        for i in range(self.list_layout.count()): 
            self.list_layout.itemAt(i).widget().close()
        
        # create dict of file groupings at each depth
        temp_list = list(runrec(self.field("folder_path")))
        self.grouping = groupings(temp_list)
        
        for a_key in self.grouping:
            # create widget and add to layout
             self.QLists['list_' + str(a_key)] = MoveableListWidget()
             self.list_layout.addWidget(self.QLists['list_' + str(a_key)])
             
             # add files names to each created listWidget
             for file_path in self.grouping[a_key]:
                    self.QLists['list_' + str(a_key)].addItem(ShortenedListItem(file_path))
        
        # show warning if no excel files in folder_path
        if len(self.grouping) == 0:
            error = "No excel files found in provided folder path."
            self.showError(error)
    
    def check(self):
        print(f'REGISTERED FIELD "files_to_use" is: {self.field("files_to_use")}')
        
    def showError(self, error_message):
       msg = QMessageBox()
       msg.setIcon(QMessageBox.Warning)
       msg.setText(error_message)
       msg.setWindowTitle("Error")
       msg.setStandardButtons(QMessageBox.Ok)
       msg.exec_()
        