#========================================#
__author__="Liang Ma"
__version__='3.2'
__description__='''
- start the server ver8.0
'''
#========================================#


from Server.serverAPI.server import Server
from Server.serverAPI.uEngine import Engine
from Server.serverAPI.serverConst import *
import time



def main():
    engineList=[]
    for num in range(NUMBER_OF_ENGINES):
        engineList.append(Engine(ENGINE_DIRECTORY,
                             ENGINE_PORT+num*ENGINE_PORT_STEP,
                             js=r'storyteller_v1.0.js'))
        engineList[num].startEngine()
        time.sleep(SECS_STARTENGINE)
    s=Server((SERVER_HOST,SERVER_PORT),WORKING_DIRECTORY)
    s.startServer()

if __name__=='__main__':
    main()
