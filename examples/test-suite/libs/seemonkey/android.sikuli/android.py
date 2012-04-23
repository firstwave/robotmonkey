from sikuli import *
import sys, difflib, os

import seemonkey, robotmonkey

if os.path.dirname(__file__) not in getImagePath():
    addImagePath(os.path.dirname(__file__))

device = seemonkey.getDevice()

    
    
def the_device_is_ready():
    print("android.sikuli getImagePath() == %s" % getImagePath())
    device.wake()
    if device.exists("unlock-mdpi.png"):
        device.dragDrop("unlock-mdpi.png",Pattern("unlock-mdpi.png").targetOffset(326,0))

def key_press(keycode):
    device.press(keycode)

def the_app_data_is_cleared(package = None):
    # this should realistically only be running an adb shell command, probably `pm`
    device.press('home')
    if package == None:
        package = "com.paypal.android.p2pmobile"      
    cmd = "pm clear %s" % package 
    rv = device.getMonkeyDevice().shell(cmd)
