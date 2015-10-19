'''
Created on Oct 16, 2015

@author: d038395
'''
#========================================#
__author__="Liang Ma"
#========================================#
import os
import shlex
import shutil
import subprocess
import uuid


class Engine:
    def __init__(self,dirEngine,port,*,node=r'bin\node.exe', js=r'app.js'):
        self.dirEngine=dirEngine
        dirTMP=os.path.join(dirEngine,'tmp')
        self.port=port
        self.id=uuid.uuid4()
        self.dirTMP=os.path.join(dirTMP,str(id))
        self.js=js
        self.node=node
        self.engine=None
        self.startEngine()
    
    def __del__(self):
        try:
            self.stopEngine()
            shutil.rmtree(self.dirTMP)
        except:
            pass

    def startEngine(self):
        cur=os.path.abspath(os.path.curdir)
        os.chdir(self.dirEngine)
        args=[os.path.join(self.dirEngine,self.node),os.path.join(self.dirEngine,self.js)]
        paras=r'-httpPort=%d -engineUUID=%s'%(self.port,str(self.id))
        args+=shlex.split(paras)
        #print(args)
        self.engine=subprocess.Popen(args)
        os.chdir(cur)
        print("Engine started at HttpPort:%d"%self.port)
    
    def stopEngine(self):
        self.engine.kill()

if __name__ == '__main__':
    pass