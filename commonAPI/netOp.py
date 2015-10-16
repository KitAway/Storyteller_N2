'''
Created on Oct 16, 2015

@author: d038395
'''
#========================================#
__author__="Liang Ma"
__version__='1.0'

__description__='''
'''
#========================================#

import http.client

def httpPOST(url,data,headers):
    # throw TimeoutError, ConnectionRefusedError#
    if not type(data) is bytes:
        data=data.encode('utf-8')
    conn = http.client.HTTPConnection(url)
    conn.request("POST", "", data, headers)
    response = conn.getresponse()
    return response


def httpsPOST(url,data,headers):
    # throw TimeoutError, ConnectionRefusedError#
    if not type(data) is bytes:
        data=data.encode('utf-8')
    conn = http.client.HTTPSConnection(url)
    conn.request("POST", "", data, headers)
    response = conn.getresponse()
    return response

def httpGET(url,pos,hr={}):
    conn = http.client.HTTPConnection(url)
    conn.request("GET", "%s"%pos,'',hr)
    response = conn.getresponse()
    return response
