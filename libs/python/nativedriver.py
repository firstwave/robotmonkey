import sys, time
from subprocess import call

sys.packageManager.makeJavaPackage("com.google.android.testing.nativedriver.client", \
                                   "AdbConnection, AdbConnectionBuilder, AdbException, \
                                   AndroidNativeDriver, AndroidNativeDriverBuilder, \
                                   AndroidNativeElement, ClassNames, FrameBufferFormat", None)
from com.google.android.testing.nativedriver.client import *

sys.packageManager.makeJavaPackage("com.google.android.testing.nativedriver.common", \
                                   "AndroidCapabilities, AndroidKeys, AndroidNativeBy, \
                                   AndroidNativeDriverCommand, FindsByText, HasTouchScreen, Touch", None)
from com.google.android.testing.nativedriver.common import *

def startInstrumentation(instrumentation):
    call(["adb", "shell", "am", "instrument", instrumentation])
    
def getDriver():
    return AndroidNativeDriverBuilder().withDefaultServer().build();
    
    
def clickText(driver, text):
    driver.findElement(AndroidNativeBy.text(text)).click();
    
def clickId(driver, id):
    driver.findElement(AndroidNativeBy.id(id)).click()

def waitForActivity(driver, activity, timeout = 30):
    endTime = time.time() + timeout
    url = ""
    # wait for `timeout` seconds for `activity` to appear in the current activity url
    while activity not in url:
        url = driver.getCurrentUrl()
        url = url[url.find("://")+3:url.find("?")] # get the text between '://' and '?'
        time.sleep(0.25)
        if time.time() > endTime:
            assert(False)