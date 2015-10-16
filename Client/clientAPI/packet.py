'''
Created on Oct 16, 2015

@author: d038395
'''


import uuid
import os
from Client.clientAPI.clientConst import (NUM_TAB_PRINT,NUM_SPACE_PRINT,
            TASK_STATUS_INITIALED,TASK_DESCR_NONE)
import time

class Status():
    def __init__(self,filename):
        self.filename=filename
        self.status=TASK_STATUS_INITIALED
        self.description=TASK_DESCR_NONE
        self.timeUpdate=True
        self.startTime=time.time()
        self.timeLast=0
    def set(self,status,description,update=True):
        self.status=status
        self.description=description
        self.timeUpdate=update
    def display(self):
        print('%12s'%self.filename[0:NUM_SPACE_PRINT],'\t'*NUM_TAB_PRINT,
        '%10.1f'%self.timeLast,'\t'*NUM_TAB_PRINT,
        self.status,'\t'*NUM_TAB_PRINT,
        self.description)
        

class packet(Status):
    def __init__(self,filepath,language,mode):
        super(os.path.basename(filepath))
        self.id=uuid.uuid4()
        self.filepath=filepath
        self.language=language
        self.mode=mode
