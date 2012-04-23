from sikuli.Sikuli import *
import seemonkey

device = seemonkey.getDevice()
 
def wake_device():
    device.wake()