import com.criticalpath.seemonkey.SeeMonkey
import com.criticalpath.seemonkey.SeeMonkeyDevice
from sikuli.Sikuli import *

_seemonkey = None

def init():
    global _seemonkey
    _seemonkey = com.criticalpath.seemonkey.SeeMonkey()

def getDevice():
    global _seemonkey
    if _seemonkey == None:
        init()
    return SeeMonkeyDevice(_seemonkey.waitForConnection())

def shutdown():
    global _seemonkey
    print("TODO:seemonkey.shutdown")

class SeeMonkeyDevice(com.criticalpath.seemonkey.SeeMonkeyDevice):
    def __init__(self, device):
        com.criticalpath.seemonkey.SeeMonkeyDevice.__init__(self, device)
        print("SeeMonkeyDevice init")
                
class SeeMonkeyRegion(object):
    def __init__(self):
        pass
    
class SeeMonkeyMatch(object):
    def __init__(self):
        pass