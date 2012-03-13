from sikuli import *
import datetime, inspect
import os, errno

# this module is a hack used to contain single-instance classes and variables
# with a global scope (i.e. a "singleton").
# A basic use of this module would be to contain a globally
# accessible SeeMonkey object to be used across multiple TestCase classes

# these members should be set to valid references before importing into test suite modules
ui = None # application ui library
platform = None # android platform library, i.e. aosp in mdpi, touchwiz in hdpi, etc.
device = None # reference to a SeeMonkey or MonkeyDevice object
state = {} # global dictionary to store state information, if needed

# pretty log output
def Log(message = "", priority = "info"):
    if message == "":
        message = timestamp()
    caller = inspect.stack()[1][3]
    print("[%s:%s] %s" % (str(priority).upper(), caller, str(message)))

def Snapshot(device, name = "", path = "snapshots"):
    '''
    take a reference to a device, an optional name and path prefix and write a
    screenshot to disk.
    By default the snapshot is saved as:
    ./snapshots/${timestamp}.png
    '''
    try:
        os.makedirs(path)
    except OSError, e:
        if e.errno != errno.EEXIST:
            raise
    
    # strip trailing slash, if present
    if path[-1] == '/':
        path = path[:-1]
    
    img = device.getMonkeyDevice().takeSnapshot()
    # if no name is passed, use the name of the calling function
    if name == "":
        name = inspect.stack()[1][3]

    now = timestamp()
    file = "%s/%s.%s.png" % (path, now, name)
    img.writeToFile(file,'png')
    Log( "saved snapshot:%s/%s.%s.png" % (path, now, name), "info")

def timestamp():
    return datetime.datetime.now().strftime("%Y%m%d-%H%M%S")


