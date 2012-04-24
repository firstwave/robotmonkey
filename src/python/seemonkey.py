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

    def sequence(self, seq):
        '''
        This method accepts a string seq that represents a sequence of keystrokes
        to be translated into the appropriate press() call of _device.

        If characters contained in longPressable[] is passed, then the
        corresponding press will be a long-press

        To repeat a sequence, use the * operator:
            EvilMonkey.sequence( 'llc' + ',' * 4 + 'dc')
        is the same as:
            Evilmonkey.sequence( 'llc,,,,dc' )

        Supported characters are:
            u - KEYCODE_DPAD_UP
            d - KEYCODE_DPAD_DOWN
            l - KEYCODE_DPAD_LEFT
            r - KEYCODE_DPAD_RIGHT
            c - KEYCODE_DPAD_CENTER

            h - KEYCODE_HOME
            b - KEYCODE_BACK
            m - KEYCODE_MENU
            s - KEYCODE_SEARCH

            > - newline
            < - backspace (del)

            , - comma adds a 0.5 second pause
            . - period adds a 2 second pause

        To send a literal portion of a sequence to EvilMonkey.type(), escape the sequence with
        backticks ` or slashes /

        Unless within an escaped literal, spaces and other characters are ignored, allowing you to visually group steps:
            EvilMonkey.sequence( 'dddc /escaped literal/ dc `foo/bar`')

            * note that 'foo/bar' is a string literal (the slash is ignored because
            backticks were used to escape this literal)
        '''

    longPressable = ('C', 'H', 'B', 'M', 'S')
    keycodeDict = {
        'u': 'KEYCODE_DPAD_UP',
        'd': 'KEYCODE_DPAD_DOWN',
        'l': 'KEYCODE_DPAD_LEFT',
        'r': 'KEYCODE_DPAD_RIGHT',
        'c': 'KEYCODE_DPAD_CENTER',

        'h': 'KEYCODE_HOME',
        'b': 'KEYCODE_BACK',
        'm': 'KEYCODE_MENU',
        's': 'KEYCODE_SEARCH',
        'n': 'KEYCODE_ENTER',
        'b': 'KEYCODE_DEL'
    }

    escapeChars = ('`', '/')
    pauseChars = {',': 0.5, '.': 2}

    keycode = None

    for ch in seq:
        if keycode is None:
            # if keycode is none, that means ch isn't literal
            if ch in escapeChars:
                # begin escaping a literal
                keycode = ch

            elif ch in pauseChars.keys():
                # pause for the time associated with ch as key
                MonkeyRunner.sleep(pauseChars[ch])

            else:
                try: # check if ch is in the dictionary, if not
                    # the error is caught and we don't do anything
                    # this way, anything not explicitly listed is ignored
                    keycode = keycodeDict[ch.lower()]
                    if ch in longPressable:
                        # long-press
                        self._device.press(keycode, MonkeyDevice.DOWN)
                        MonkeyRunner.sleep(self.longPressDuration)
                        self._device.press(keycode, MonkeyDevice.UP)
                    else:
                        # tap
                        self._device.press(keycode, MonkeyDevice.DOWN_AND_UP)

                except (KeyError):
                    # this means ch was not in the dictionary, it's an ignored character
                    pass
                keycode = None

        else:
            # that mean's this ch is a literal
            if ch == keycode:
                # stop escaping
                keycode = None
            else:
                self.type(ch)
                
class SeeMonkeyRegion(object):
    def __init__(self):
        pass
    
class SeeMonkeyMatch(object):
    def __init__(self):
        pass