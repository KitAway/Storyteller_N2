'''
Created on Oct 16, 2015

@author: d038395
'''
#! python
#========================================#
__author__="Liang Ma"
__usage__='''usage: %s  [-l lang] [-u sec] file_directory
    -l lang : specify the language of the file
    -u sec  : fresh time period in the console, sec must be a float number
    -h or --help  : display the help
    '''%__file__
__description__='''
'''
#========================================#
import os
import sys

from Client.clientAPI.Tasks import Tasks
from Client.clientAPI.clientConst import UPDATE_TIME_SECOND
from commonAPI.constValue import (SERVER_PORT, SERVER_HOST, LANGUAGE_SUPPORT)


def main():
    print("welcom to storyteller.")
    argv=sys.argv[1:]
    if ('-h' in argv) or ('--help' in argv):
        print(__usage__)
        return

    if '-l' in argv:
        argv.remove('-l')
        try:
            lang=argv.pop(0)
        except IndexError :
            print('expect the language type')
            print(__usage__)
            return
            if lang not in LANGUAGE_SUPPORT:
                print(__usage__)
                return
    else:
        lang='en-us'
        
    if '-u' in argv:
        argv.remove('-u')
        try:
            uTime=float(argv.pop(0))
        except IndexError :
            print('expect the update time.')
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

    myTask= Tasks(server_url,filepath,lang,uTime)
    myTask.startTrans()
    myTask.display()
    print("finished")

if __name__ == '__main__':
    main()
