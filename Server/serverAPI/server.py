'''
Created on Oct 16, 2015

@author: d038395
'''

#========================================#
__author__="Liang Ma"
__version__='9.0'
__description__='''
- audio format conversion software 'ffmpeg'
'''
#========================================#
import http.server
import json
import os
import subprocess
import time

from Server.serverAPI.serverConst import *  # @UnusedWildImport
from commonAPI.constValue import * # @UnusedWildImport
from commonAPI.netOp import httpPOST, httpGET
from Server.serverAPI.packet import packet, pacStatus


class httpHandler(http.server.BaseHTTPRequestHandler):
    
    def __init__(self,packetList):
        self.packetList=packetList
    
    def do_HEAD(self,content,hrs=''):
        self.send_response(content)
        self.send_header("Content-type", "text/html",hrs)
        self.end_headers()


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        auid=self.headers['id']
#        portBias=int(self.headers['portBias'])
        audioname=self.headers['audioname']
        language=self.headers['language']
        operating_mode=self.headers['mode']
        
        
        pak=packet(auid,WORKING_DIRECTORY,language,operating_mode)
        self.packetList.append(pak)
        
        rPort=ENGINE_PORT
        URL_Server='%s:%s'%(ENGINE_HOST_IP,rPort)
        try:
            response=httpGET(URL_Server,r'/langpackdetails')
            jstr=''
            if response.status==200:
                jbyte=response.read()
                jstr=jbyte.decode('utf-8')
            else:
                self.do_HEAD(404)
                pak.update(PAC_FAILED)
            jdict=json.loads(jstr)
        except:
            self.do_HEAD(404)
            pak.update(PAC_FAILED)
            return
        if jdict['baseLanguage'].lower()!=language or jdict['modes'][0].lower()!=operating_mode:
            self.do_HEAD(400)
            pak.update(PAC_FAILED)
            return
        
        post_data = self.rfile.read(content_length)
    
        audioDir=os.path.join(WORKING_DIRECTORY,str(auid))
        if not os.path.exists(audioDir):
            os.mkdir(audioDir)
        audiopathOrg=os.path.join(audioDir,audioname)
        audiopath=os.path.join(audioDir,'%s.wav'%str(auid))
        with open(audiopathOrg,'wb') as fw:
            fw.write(post_data)
    
        command=[FFMPEG_PROG_PATH,'-i',audiopathOrg,
                           '-ar','16000',audiopath]
    
        try:
            p=subprocess.Popen(command)
            p.wait(20)
        except subprocess.TimeoutExpired:
            self.do_HEAD(406)
            pak.update(PAC_FAILED)
            return
    
        if not os.path.exists(audiopath):
            self.do_HEAD(406)
            pak.update(PAC_FAILED)
            return
    
        pak.update(PAC_RECEIVED)
#        rPort=ENGINE_PORT+ENGINE_PORT_STEP*(portBias%NUMBER_OF_ENGINES)
        rPort=ENGINE_PORT
        URL_Server='%s:%s'%(ENGINE_HOST_IP,rPort)
        hrs={'Content-type':'application/json'}
        
        model={"name":language}
        firstChannel={'url':audiopath,'format':'wave'}
        channels={'firstChannelLabel':firstChannel}
        data={'reference':auid,'operating_mode':operating_mode,
                                              'model':model,'channels':channels}
        uData=json.dumps(data)
        binary_data = uData.encode('utf-8')
        print("POST on %s"%URL_Server)
        response = httpPOST(URL_Server,binary_data,hrs)
        try:
            self.do_HEAD(response.status)
            pak.update(PAC_SUBMIT)
            pacStatus(pak).start()
        except AttributeError:
            self.do_HEAD(404)
            pak.update(PAC_FAILED)
        except ConnectionRefusedError:
            self.do_HEAD(404)
            pak.update(PAC_FAILED)

    def do_GET(self):
        sid=self.path[8:]
        sindex=self.packetList.index(packet(sid))
        self.do_HEAD(200,"'status':%s"%self.packetList[sindex].status)
        if self.packetList[sindex].status==PAC_SUCCESSED:
            self.do_HEAD(200)
            self.wfile.write(self.packetList[sindex].text)

class Server:
    def __init__(self,url,path,packetList):
        self.path=path
        self.packetList=packetList
        if type(url) is str:
            ulist=url.split(':')
            self.url=(ulist[0],int(ulist[1]))
        elif type(url) is tuple and type(url[1]) is int:
            self.url=url
        else:
            raise TypeError('The data type of ip address or port of a server is not correct.')
        self.server=None
        if not os.path.exists(self.path):
            os.mkdir(self.path)
    def startServer(self):  
        self.server = http.server.HTTPServer(self.url, httpHandler(self.packetList))
        print('Server start @%s:%s at time'%self.url,time.asctime())
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            self.server.server_close()
            print('Server stopped at time',time.asctime())

if __name__=="__main__":
    print("start the server")
    self=Server(('127.0.0.1',9999),'.')
    self.startServer()
