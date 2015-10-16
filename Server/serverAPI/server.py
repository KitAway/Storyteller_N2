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
from Server.serverAPI.netOp import httpPOST,httpGET
import os
import subprocess
from Server.serverAPI.serverConst import *
import time

class httpHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self,content):
        self.send_response(content)
        self.send_header("Content-type", "text/html")
        self.end_headers()


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        auid=self.headers['id']
        portBias=int(self.headers['portBias'])
        audioname=self.headers['audioname']
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
            return
    
        if not os.path.exists(audiopath):
            self.do_HEAD(406)
            return
    
        rPort=ENGINE_PORT+ENGINE_PORT_STEP*(portBias%NUMBER_OF_ENGINES)
        URL_Server='%s:%s'%(ENGINE_HOST_IP,rPort)
        hrs={'Content-type':'application/json'}
        operating_mode='accurate'
        model={"name":'en-us'}
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
        except AttributeError:
            self.do_HEAD(404)


    def do_GET(self):
        portBias=int(self.headers['portBias'])
        rPort=ENGINE_PORT+ENGINE_PORT_STEP*(portBias%NUMBER_OF_ENGINES)
        URL_Server='%s:%s'%(ENGINE_HOST_IP,rPort)
        response=httpGET(URL_Server,self.path)
        jstr=''
        try:
            if response.status==200:
                self.do_HEAD(200)
                jstr=response.read()
                self.wfile.write(jstr)
            else:
                self.do_HEAD(404)
        except AttributeError:
            self.do_HEAD(404)


class Server:
    def __init__(self,url,path):
        self.path=path
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
        self.server = http.server.HTTPServer(self.url, httpHandler)
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
