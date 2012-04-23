from sikuli.Sikuli import *
import sys, difflib, os

import seemonkey

addImagePath(os.path.dirname(__file__))

device = seemonkey.getDevice()

def get_shared_prefs(): 
    print(device.getMonkeyDevice().shell('cat /data/data/%s/shared_prefs/%s.xml' % (package, package)))

def the_app_is_started():
    # this is the place to determine if the app is running
    # to avoid trying to launch an instance of an Activity that already exists
    # this will probably be the most frequently used step
    p2pPackage = "com.paypal.android.p2pmobile"
    #launchActivity = ".activity.GridLauncherActivity"
    launchActivity = ".activity.IntroActivity"
    device.getMonkeyDevice().startActivity(component = "%s/%s" % (p2pPackage, launchActivity))
    device.sleep(3000) # wait for the app to launch before returning

def the_app_is_stopped():
    package = "com.paypal.android.p2pmobile"

    device.press('home')
    
    device.getMonkeyDevice().startActivity(
        action = "android.settings.APPLICATION_DETAILS_SETTINGS",
        data = "package:%s" % package,
        component = "com.android.settings/.applications.InstalledAppDetails")
    device.sleep(2000)

   
    if device.exists(Pattern("force-stop-mdpi.png").similar(0.99)):
        device.click("force-stop-mdpi.png")
        device.click("sys-ok-mdpi.png")
    device.press('home')

def I_click(*args):
    target = args[0].lower()

    if target == "done":
        device.click("mdpi-done.png")
    elif target == "the privacy policy link":
        device.click(Pattern("mdpi-privacy-policy-link.png").similar(0.79))
    elif target == "the user agreement link":
        device.click(Pattern("mdpi-user-agreement-link.png").similar(0.90))
    elif target == "login":
        device.click("mdpi-login-blue.png")
    elif target == "sign up":
        device.click("mdpi-sign-up.png")
    elif target == "switch user":
        device.click("switch-user-link-mdpi.png")
        device.sleep(500)
    elif target == 'forgot password':
        device.click("forgot-your-password-link-mdpi.png")
    elif target == 'cancel':
        device.click("cancel-button-mdpi.png")
    elif target == 'continue':
        device.click("continue-button-mdpi.png")   
    else:           
        device.click(args[0])

def I_accept_the_terms_of_service():
    device.click("mdpi-agree.png")

def I_view_the_terms_of_service():
    device.click("mdpi-view-terms.png")


def set_server(*args):
    # assumes the debug menu is reachable by long click
    device.longClick("paypal-logo-small-mdpi.png")
    device.sleep(500)
    srv = args[0].lower() 
    if srv == 'stage2mb107':
        device.click(Pattern("server-options-mdpi.png").targetOffset(-105,-110))
    elif srv == 'stage2mobile09':
        device.click(Pattern("server-options-mdpi.png").targetOffset(-105,-38))
    elif srv == 'stage2mobile10':
        device.click(Pattern("server-options-mdpi.png").targetOffset(-108,37))
    elif srv == 'sandbox':
        device.click(Pattern("server-options-mdpi.png").targetOffset(-102,103))
    else:
        device.click(Pattern("server-live-mdpi.png").targetOffset(-47,1))
            
            
    device.press('back')
def clear_accepted_license():
    device.longClick("paypal-logo-small-mdpi.png")
    device.sleep(500)

    for i in range(16):
        device.press('dpad_down')

    device.press('dpad_right')
    device.press('dpad_right')
    device.press('dpad_right')
    device.press('dpad_right')
    device.press('enter')
    device.press('back')
    

def an_error_dialog_should_be_displayed(*args):
    device.wait("done-button-mdpi.png", 30)
    device.click("done-button-mdpi.png")

def I_should_be_prompted_to_open_a_browser():
    device.exists("view-link-dialog-mdpi.png")
def the_browser_prompt_closes():
    device.sleep(500)
    assert(not device.exists("view-link-dialog-mdpi.png"))

                     
    
def select_tab(*args):
    tab = args[0].lower()
    if tab == 'pin':
        if not device.exists("PIN-tab-sel-mdpi.png"):
            device.click("PIN-tab-mdpi.png")
    elif tab == 'password':
        if not device.exists("password-tab-selected-mdpi.png"):
            device.click("pasword-tab-unselected-mdpi.png")

def go_to_screen(*args):
    scr = args[0].lower()

    if scr == 'login':
        if device.exists("intro-login-mdpi.png"):
            device.click("intro-login-mdpi.png")
            verify_screen('login')


def verify_element(element, visible):
    e = element.lower()
    v = (visible.lower() == 'true') # convert to a boolean value
    edict = {'a switch user link':"switch-user-mdpi.png",
            'a link to forgot password flow': "forgot-your-password-link-mdpi.png"}

    if e in edict.keys():
        e = edict[e]

    if v:
        assert(device.exists(e))
    else:
        assert(not device.exists(e))
                
                
def verify_screen(*args):
    scr = args[0].lower()        
    if scr == 'account':
        device.wait("default-avatar-mdpi.png", 30)
    elif scr == 'terms':
        device.wait("mdpi-terms-of-use-title.png", 30)
    elif scr == 'login':
        device.wait("secure-login-mdpi.png", 30)
    else:
        print("cannot verify unknown screen: %s" % scr)
