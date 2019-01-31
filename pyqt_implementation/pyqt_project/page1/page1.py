# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:03:23 2019

@author: TeghanN
"""


from page1.widgets1 import QWizardPage, QILineEdit, QLabel, QVBoxLayout, QTextEdit


class Page1(QWizardPage):
    def __init__(self):
        super().__init__()
        self.initWidgets()
        self.initLayout()
    
    
    def initWidgets(self):
        self.label_1 = QLabel(self)
        self.label_1.setText('<b> Enter Path: </b>')
        
        self.line_1 = QILineEdit()
        self.line_1.setPlaceholderText('Enter file path')
        
        instructions = \
        '''
        instructionsinstructionsinstructionsinstructionsinstructions \
        instructionsinstructionsinstructionsinstructionsinstructions \
        instructionsinstructionsinstructionsinstructionsinstructions
        '''
        self.text_1 = QTextEdit(self)
        self.text_1.setText(instructions)
        self.text_1.setReadOnly(True)
    
        
    def initLayout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.label_1)
        layout.addWidget(self.line_1)
        layout.addWidget(self.text_1)
        self.setLayout(layout)
        

    def fileGrouping():
        pass
        # run file grouping algorithm on path
        # when next button is pressed
        # Make next button unpressable until
        # path is supplied
        # conditional page outcome based
        # on file grouping algo
        
        
        