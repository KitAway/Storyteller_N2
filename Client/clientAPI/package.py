'''
Created on Oct 16, 2015

@author: d038395
'''

import os

from Client.clientAPI.clientConst import RECOG_AUDIO_FORMAT

from Client.clientAPI.packet import packet


def isValidAudioFiles(one):
    if os.path.isfile(one):
        ends=os.path.splitext(one)[1]
        return ends.lower() in RECOG_AUDIO_FORMAT
class package():
    def __init__(self,path,*,language='en-us',mode='accurate'):
        self.packetList=list()
        if os.path.isdir(path):
            tmpList=os.listdir(path)
            for one in tmpList:
                filepath=os.path.join(path,one)
                if isValidAudioFiles(filepath):
                    #print(one)
                    self.packetList.append(packet(filepath,language,mode))
        elif isValidAudioFiles(path):
            self.packetList.append(packet(path,language,mode))
def main():
    path='E:\\Storyteller_DEMO\\'
    p=package(path)
    print(p.packetList)

if __name__=='__main__':
    main()
