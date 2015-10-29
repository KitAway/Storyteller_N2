#========================================#
__author__="Liang Ma"
__version__='3.2'
__description__='''
- start the server ver8.0
'''
#========================================#


import time
import sys

from Server.serverAPI.server import Server
from Server.serverAPI.serverConst import *  # @UnusedWildImport
from commonAPI.constValue import *  # @UnusedWildImport
from Server.serverAPI.uEngine import Engine

def main():
    engineList=[]
    argv=sys.argv[1:]
    if len(argv)==0:
        lang='en-us'
    else:
        lang=argv[0]
    if lang in LANGUAGE_SUPPORT:
        engineList.append(Engine(ENGINE_DIRECTORY,
                         ENGINE_PORT,lang,js=r'storyteller_v1.0.js'))
        
    time.sleep(SECS_STARTENGINE)
    packetList=list()
    s=Server((SERVER_HOST,SERVER_PORT),WORKING_DIRECTORY,packetList)
    s.startServer()

if __name__=='__main__':
    main()
