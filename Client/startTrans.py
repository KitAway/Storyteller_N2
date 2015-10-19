'''
Created on Oct 16, 2015

@author: d038395
'''
#! python
#========================================#
__author__="Liang Ma"
__usage__='''usage: %s  [-u sec] file_directory
    -u sec  : fresh time period in the console, sec must be a float number
    -h or --help  : display the help
    '''%__file__
__description__='''
'''
#========================================#
import os
import sys

from Client.clientAPI.Tasks import Tasks
from Client.clientAPI.clientConst import (SERVER_PORT, SERVER_HOST, UPDATE_TIME_SECOND)


def main():
    argv=sys.argv[1:]
    if ('-h' in argv) or ('--help' in argv):
        print(__usage__)
        return 0

    if '-u' in argv:
        argv.remove('-u')
        try:
            uTime=float(argv.pop(0))
        except IndexError :
            print('lack of the update time.')
            print(__usage__)
            return -1
        except  ValueError:
            print('the update time must be a number')
            print(__usage__)
            return -1
    else:
        uTime=UPDATE_TIME_SECOND
    try:
        filepath=argv.pop()
    except IndexError:
        filepath='.'
    if not os.path.exists(filepath):
        print('%s does not exist!'%filepath)
        print(__usage__)
        return -1

#=================   Start the transcription   ==============#
    server_url=(SERVER_HOST, SERVER_PORT)

    myTask= Tasks(server_url,filepath,uTime)
    myTask.startTrans()
    myTask.display()

if __name__ == '__main__':
    pass