'''
Created on Oct 29, 2015

@author: d038395
'''



class packet():
    def __init__(self,Id,filepath,language,mode):
        self._id=Id
        self._filepath=filepath
        self._language=language
        self._mode=mode
        self.status=False
        
    def update(self,status):
        self.status=status


if __name__ == '__main__':
    pass