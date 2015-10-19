

#========================================#
__author__="Liang Ma"
__version__='1.0.1'
#========================================#

import copy
import json
import os
import sys


#def getFileNumber(fileName):
#  match=re.match('S-(\d+).',fileName)
#  num=int(match.group(1))
#  return str("%03d"%(num))
def readJson(inPath,outPath):
    with open(inPath,'rU') as fid:  
        fstr=fid.read()    
    try:
        fdict=json.loads(fstr)
    except:
        return
      
    if fdict['status']=='TRANSCRIBED' :
        try:
            lattice=fdict['channels']['firstChannelLabel']['lattice']
        except KeyError:
            print('Error happend,',fdict['channels']['firstChannelLabel']['errors'])
            return False
        chann={}
        for num in lattice:
            links=fdict['channels']['firstChannelLabel']['lattice'][num]['links']
            resultDict={}
            for keyDict in links:
                valueDict=links[keyDict]
                if valueDict['best_path']==True: #and valueDict['word']!='!NULL':
                    resultDict[valueDict['start']]=valueDict['word']
            chann[num]=copy.deepcopy(resultDict)  
        with open(outPath,'w+') as fod:
            fod.write(json.dumps(chann,sort_keys=True,indent=4,separators=(',', ': ')))
        return True  
def main():
    argv=sys.argv
    if len(argv)!=2:
        raise Exception('error use command')
    filePath=argv[-1]
    fileDir=os.path.split(filePath)[0]
    filename=os.path.split(filePath)[1]
    readJson(filePath,os.path.join(fileDir,'result_%s'%filename))
  
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
