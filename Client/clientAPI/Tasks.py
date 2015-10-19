'''
Created on Oct 16, 2015

@author: d038395
'''

#========================================#
__author__="Liang Ma"
__version__='1.0'
__description__='''

'''
#========================================#
#! python
import json
import os
import subprocess
import threading
import time

from Client.clientAPI.clientConst import *  # @UnusedWildImport
from Client.clientAPI.htmlFrame import myHTML
from Client.clientAPI.jsonReadText import readJson
from Client.clientAPI.package import package
from commonAPI.netOp import httpPOST, httpGET


class Tasks():
    def __init__(self,server_url,audiopath,updateTime):
        self.package=package(audiopath)
        self.server_url="%s:%self"%self.server_url
        self.status=False
        self.updateTime=updateTime

    def startTrans(self):
        for one in self.package.packetList:
            uniTrans(one,self.server_url).start()
        
    def display(self):
        while True:
            if self.status:
                break
            time.sleep(self.updateTime)
    
    def myPrint(self):
        self.status=True
        length=len(self.package.packetList)
        cls=subprocess.call('cls',shell=True)
        print(time.asctime(),'\n')
        print('filename','\t'*NUM_TAB_PRINT,
                'time last','\t'*NUM_TAB_PRINT,
                'status','\t'*NUM_TAB_PRINT,
                'description')
        print('-'*NUM_SPACE_PRINT,'\t'*NUM_TAB_PRINT,
                '-'*NUM_SPACE_PRINT,'\t'*NUM_TAB_PRINT,
                '-'*NUM_SPACE_PRINT,'\t'*NUM_TAB_PRINT,
                '-'*NUM_SPACE_PRINT)
    
        Ctime=time.time()
        for num in range(length):
            tSta=self.package.packetList[num]
            if tSta.timeUpdate:
                tSta.timeLast=Ctime-tSta.startTime
                self.status=False
                tSta.display()


#    def getStatus(self):
#        if self.status:
#            return self.status
#        for one in self.package.packetList:
#            if one.status==False:
#                return False
#        self.status=True
#        return True
        

class uniTrans(threading.Thread):
    def __init__(self,packet,server_url,daemon=True):
        self.packet=packet
        self.server_url=server_url
        filepath=packet.filepath
        resultPath=os.path.join(os.path.dirname(filepath),packet.filename+'.result')
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        self.jsonPath=os.path.join(resultPath,packet.filename+'.json')
        self.textPath=os.path.join(resultPath,packet.filename+'.txt')
        self.htmlPath=os.path.join(resultPath,packet.filename+'.html')
        self.jsPath=os.path.join(resultPath,packet.filename+'.js')
        self.daemon=daemon
    def post(self):
        with open(self.packet.filepath,'rb') as fr:
            data=fr.read()
        hrs={'id':str(self.packet.id),'audioname':self.packet.filename}
        try:
            response=httpPOST(self.server_url,data,hrs)
            return response.status
        except:
            return
        
    def get(self):
        try:
            hrs={}
            response= httpGET(self.server_url,'/status/%s'%self.id,hrs)
            if response.status==200:
                return response.read().decode('utf-8')
        except:
            return
        
    def creatHtml(self,*,wLong=10):
        with open(self.textPath,'r') as fr:
            strFile=fr.read()
        fileDict=json.loads(strFile)
        chann=fileDict['1'].items()
        chann=[x for x in chann if x[1][0]!='!']
        chann=sorted(chann,key=lambda x: float(x[0]))
    
        myweb=myHTML(chann,self.packet.filename,wLong)
        with open(self.htmlPath,'w+') as fh:
            fh.write(myweb.getHTML())
        with open(self.jsPath,'w+') as fj:
            fj.write(myweb.getJs())  
            
    def run(self):
        status=self.post()
        if status==200:
            self.packet.set(TASK_STATUS_SUBMIT,TASK_DESCR_NONE)
            while True:
                time.sleep(QUERYING_TIME)
                try:
                    jsonText=self.get()
                    dict=json.loads(jsonText)  # @ReservedAssignment
                except ValueError:
                    self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_MISS)
                except TypeError:
                    self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_MISS)
                if dict['status']=='TRANSCRIBED':
                    self.packet.set(TASK_STATUS_FINISHED,TASK_DESCR_GOT)
                    try:
                        with open(self.jsonPath,'w+') as fd:
                            fd.write(json.dumps(dict, sort_keys=True,indent=4, separators=(',', ': ')))
                        if readJson(self.jsonPath,self.textPath):
                            self.creatHtml()
                            return
                    except:
                        self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_ANALYSIS)
                        return
                    else:
                        self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_ANALYSIS)
                        return
                    break
                elif dict['status']=='FAILED':
                    self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_GOT)
                    return False
                elif dict['status']=='QUEUED':
                    self.packet.set(TASK_STATUS_QUEUED,TASK_DESCR_GOT)
                    continue
                elif dict['status']=='TRANSCRIBING':
                    self.packet.set(TASK_STATUS_PROGRESS,TASK_DESCR_GOT)
                    continue
                else:
                    self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_STATUS)
        elif status==404:
            self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_SERVER)
        elif status==406:
            self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_FILE)
        

if __name__=='__main__':
    pass
