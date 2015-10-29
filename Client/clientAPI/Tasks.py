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
import http
import json
import os
import subprocess
import threading
import time

from commonAPI.constValue import *  # @UnusedWildImport
from Client.clientAPI.clientConst import *  # @UnusedWildImport
from Client.clientAPI.htmlFrame import myHTML
from Client.clientAPI.jsonReadText import readJson
from Client.clientAPI.package import package
from commonAPI.netOp import httpPOST, httpGET


class Tasks():
    def __init__(self,server_url,audiopath,language,updateTime):
        self.package=package(audiopath,language=language)
        self.server_url="%s:%s"%server_url
        self.status=False
        self.updateTime=updateTime

    def startTrans(self):
        for one in self.package.packetList:
            uniTrans(one,self.server_url).start()
            time.sleep(1)
        
    def display(self):
        while True:
            if self.status:
                break
            self.myPrint()
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
        super().__init__()
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
        hrs={'id':str(self.packet.id),
             'audioname':self.packet.filename.encode('unicode-escape'),
             'language':self.packet.language, 'mode':self.packet.mode}
        try:
            response=httpPOST(self.server_url,data,hrs)
            return response.status
        except http.client.HTTPException:
            self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_CONNECTION,False)
        except http.client.NotConnected:
            self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_CONNECTION,False)
        except:
            self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_CONNECTION,False)

        
    def get(self):
        try:
            hrs={}
            response= httpGET(self.server_url,'/status/%s'%self.packet.id,hrs)
            if response.status==200:
                return response.read().decode('utf-8')
        except http.client.HTTPException:
            self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_MISS,False)
        except http.client.NotConnected:
            self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_MISS,False)

        
    def creatHtml(self,*,wLong=10):
        with open(self.textPath,'r') as fr:
            strFile=fr.read()
        fileDict=json.loads(strFile)
        chann=fileDict['1'].items()
        chann=[x for x in chann if x[1][0]!='!']
        chann=sorted(chann,key=lambda x: float(x[0]))
    
        myweb=myHTML(chann,self.packet.filename,self.packet.language,wLong)
        with open(self.htmlPath,'w+') as fh:
            fh.write(myweb.getHTML())
        with open(self.jsPath,'w+') as fj:
            fj.write(myweb.getJs())  
            
    def run(self):
        try:
            status=self.post()
        except TimeoutError:
            self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_CONNECTION,False)
        if status==200:
            self.packet.set(TASK_STATUS_SUBMIT,TASK_DESCR_NONE)
            while True:
                time.sleep(QUERYING_TIME)
                try:
                    jsonText=self.get()
                    dict=json.loads(jsonText)  # @ReservedAssignment
                except ValueError:
                    self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_MISS,False)
                    return
                except TypeError:
                    self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_MISS,False)
                    return
                if dict['status']=='TRANSCRIBED':
                    self.packet.set(TASK_STATUS_FINISHED,TASK_DESCR_GOT,False)
                    try:
                        with open(self.jsonPath,'w+') as fd:
                            fd.write(json.dumps(dict, sort_keys=True,indent=4, separators=(',', ': ')))
                        if readJson(self.jsonPath,self.textPath):
                            self.creatHtml()
                            return
                    except:
                        self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_ANALYSIS,False)
                        return
                    else:
                        self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_ANALYSIS,False)
                        return
                elif dict['status']=='FAILED':
                    self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_GOT,False)
                    return
                elif dict['status']=='QUEUED':
                    self.packet.set(TASK_STATUS_QUEUED,TASK_DESCR_GOT)
                    continue
                elif dict['status']=='TRANSCRIBING':
                    self.packet.set(TASK_STATUS_PROGRESS,TASK_DESCR_GOT)
                    continue
                else:
                    self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_STATUS,False)
        elif status==404:
            self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_SERVER,False)
        elif status==406:
            self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_FILE,False)
        else:
            self.packet.set(TASK_STATUS_FAILED,TASK_DESCR_GOT,False)
        

if __name__=='__main__':
    pass
