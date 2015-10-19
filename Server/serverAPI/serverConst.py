'''
Created on Oct 16, 2015

@author: d038395
'''

##--------------------------  Parameters for server  ------------------------------##

SOX_PROG_PATH           =   "E:\\Program Files (x86)\\sox-14.4.2\\sox.exe"
FFMPEG_PROG_PATH        =   "E:\\Program files\\ffmpeg-20150928-git-1d0487f-win64-static\\bin\\ffmpeg.exe"
WORKING_DIRECTORY       =   "E:\\STORYTELLER_TMP"
SERVER_PORT             =   9999
SERVER_PORTS            =   9998
SERVER_HOST             =   'denethor.cdsdom.polito.it'
SECS_STARTENGINE        =   15
##--------------------------  Parameters for engine  ------------------------------##
MAX_NUMBER_OF_ENGINES   =   3
ENGINE_PORT             =   40801
ENGINE_PORTS            =   9087
ENGINE_PORT_STEP        =   2
ENGINE_DIRECTORY        =   "E:\\Program Files\\Nuance\\Transcription Engine\\"
ENGINE_HOST_IP          =   '127.0.0.1'

NUMBER_OF_ENGINES       =   1



if NUMBER_OF_ENGINES>MAX_NUMBER_OF_ENGINES:
    raise Exception('The number of engines to start exccess the maximum number.')

if NUMBER_OF_ENGINES!=1:
    raise Exception('Only one engine is supported in SDK2.0')

if __name__ == '__main__':
    pass