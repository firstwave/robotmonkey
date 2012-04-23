import seemonkey

@seemonkey.deco
def sanityCheck():
    scr = seemonkey.getDevice()
    scr.wake()
    scr.press('HOME')
    
sanityCheck()
exit(0)