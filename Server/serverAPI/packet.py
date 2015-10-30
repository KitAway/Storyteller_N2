'''
Created on Oct 29, 2015

@author: d038395
'''

import json
import os
import threading
import time

from Server.serverAPI.serverConst import SECS_STATUS, ENGINE_PORT, ENGINE_HOST_IP
from commonAPI.constValue import *
from commonAPI.netOp import httpGET


class packet():
    def __init__(self,Id,filepath='',language='en-us',mode='accurate'):
        self._id=Id
        self._filepath=filepath
        self._language=language
        self._mode=mode
        self.status=PAC_ESTABLISH
        self.text=''
        
    def update(self,status):
        self.status=status

    def Text(self,text):
        self.text=text
        
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self._id == other._id)

    def __ne__(self, other):
        return not self.__eq__(other)

class pacStatus(threading.Thread):
    def __init__(self,packet):
        super().__init__()
        self.packet=packet
        
    def run(self):
        while(True):
            time.sleep(SECS_STATUS)
            rPort=ENGINE_PORT
            URL_Server='%s:%s'%(ENGINE_HOST_IP,rPort)
            response=httpGET(URL_Server,'/status/%s'%self.packet._id)
            jstr=''
            try:
                if response.status==200:
                    getstring=response.read()
                    jstr=getstring.decode('utf-8')
                    dict=json.loads(jstr)
                else:
                    self.packet.update(PAC_FAILED)
            except AttributeError:
                self.packet.update(PAC_FAILED)
            except TimeoutError:
                self.packet.update(PAC_FAILED)
            except ConnectionRefusedError:
                self.packet.update(PAC_FAILED)
            except Exception as e:
                self.packet.update(PAC_FAILED)
                print(e)
            
            if dict['status']=='TRANSCRIBED':
                self.packet.update(PAC_SUCCESSED)
                self.packet.Text(getstring)
                file=os.path.join(self.packet._filepath,self.packet._id)
                file=os.path.join(file,self.packet._id)
                with open(file,'w') as fw:
                    fw.write(jstr)
                break
            elif dict['status']=='QUEUED':
                self.packet.update(PAC_QUEUED)
            elif dict['status']=='TRANSCRIBING':
                self.packet.update(PAC_PROCESS)
            else:
                self.packet.update(PAC_FAILED)
                break
    
if __name__ == '__main__':
    pass