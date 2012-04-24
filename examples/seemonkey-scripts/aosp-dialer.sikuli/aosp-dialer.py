# This script was written against a Gingerbread (2.3.7) emulator
# to run this script against a physical device, ensure that you have
# connected an mdpi, AOSP-based device, such as the Nexus One or a Gingerbread powered Nexus S

from sikuli.Sikuli import *
import seemonkey

device = seemonkey.getDevice()

device.wake()


# define a dictionary of UI resources

dialerKeys = {'1':"key-1.png", '2':"key-2.png", '3':"key-3.png",
        '4':"key-4.png", '5':"key-5.png", '6':"key-6.png", 
        '7':"key-7.png", '8':"key-8.png", '9':"key-9.png",
         '0':"key-0.png", 'send':"key-send.png", 'end':"key-end.png"
        }


# Unlock the device if the lockscreen is visible
if device.exists("unlock-icon.png"):
    device.dragDrop("unlock-icon.png",Pattern("unlock-icon.png").targetOffset(321,0))


# go to the home screen
device.press('home')

# launch the dialer
device.click("dialer-app-icon.png")

device.sleep(2) # wait for the ui to settle down again

# dial and send
for digit in '5035551236':
    device.click(dialerKeys[digit])

device.click(dialerKeys['send'])

# waitfo r the end call button to appear, then click it
device.wait(dialerKeys['end']) # will throw an exception if not found
device.click(dialerKeys['end'])

device.press('back')

# due to a bug in the Sikuli interpereter, you must explicitly quit a script with the following command:
exit(0)
