from sikuli.Sikuli import *
import sys, difflib, os

import seemonkey

addImagePath(os.path.dirname(__file__))

class TestApp(object):
    def __init__(self):
        self.device = seemonkey.getDevice()

    def the_app_is_launched(self):
        # this is the place to determine if the app is running
        # to avoid trying to launch an instance of an Activity that already exists
        # this will probably be the most frequently used step
        p2pPackage = "com.paypal.android.p2pmobile"
        #launchActivity = ".activity.GridLauncherActivity"
        launchActivity = ".activity.IntroActivity"
        self.device.getMonkeyDevice().startActivity(component = "%s/%s" % (p2pPackage, launchActivity))
        self.device.sleep(2000) # wait for the app to launch before returning


    def I_click(self, *args):
        target = args[0].lower()

        if target == "done":
            self.device.click("mdpi-done.png")
        elif target == "the privacy policy link":
            self.device.click(Pattern("mdpi-privacy-policy-link.png").similar(0.79))
        elif target == "the user agreement link":
            self.device.click(Pattern("mdpi-user-agreement-link.png").similar(0.90))
        elif target == "login":
            self.device.click("mdpi-login-blue.png")
        elif target == "sign up":
            self.device.click("mdpi-sign-up.png")
        else:           
            self.device.click(args[0])

    def I_accept_the_terms_of_service(self):
        self.device.click("mdpi-agree.png")

    def I_view_the_terms_of_service(self):
        self.device.click("mdpi-view-terms.png")
    

    def set_server(self, *args):
        # assumes the debug menu is reachable by long click
        self.device.longClick("paypal-logo-small-mdpi.png")
        self.device.sleep(500)
        srv = args[0].lower() 
        if srv == 'stage2mb107':
            self.device.click(Pattern("server-options-mdpi.png").targetOffset(-105,-110))
        elif srv == 'stage2mobile09':
            self.device.click(Pattern("server-options-mdpi.png").targetOffset(-105,-38))
        elif srv == 'stage2mobile10':
            self.device.click(Pattern("server-options-mdpi.png").targetOffset(-108,37))
        elif srv == 'sandbox':
            self.device.click(Pattern("server-options-mdpi.png").targetOffset(-102,103))
        else:
            self.device.click(Pattern("server-live-mdpi.png").targetOffset(-47,1))
                
                
        self.device.press('back')

    def an_error_dialog_should_be_displayed(self, *args):
        self.device.wait("done-button-mdpi.png", 30)
        self.device.click("done-button-mdpi.png")

    def go_to_screen(self, *args):
        print(args)

    def verify_screen(self, *args):
        scr = args[0].lower()        
        if scr == 'account':
            self.device.wait("default-avatar-mdpi.png", 30)
        elif scr == 'terms':
            self.device.wait("mdpi-terms-of-use-title.png", 30)
        elif scr == 'login':
            self.device.wait("secure-login-mdpi.png", 30)
        else:
            print("cannot verify unknown screen: %s" % scr)


          

                
class Login(object): 
    def __init__(self):
        self.device = seemonkey.getDevice()

    def select_tab(self, *args):
        tab = args[0].lower()
        if tab == 'pin':
            if not self.device.exists("PIN-tab-sel-mdpi.png"):
                self.device.click("PIN-tab-mdpi.png")
        elif tab == 'password':
            if not self.device.exists("password-tab-selected-mdpi.png"):
                self.device.click("pasword-tab-unselected-mdpi.png")
                
    def the_PIN_tab_should_be_selected_by_default(self):
        self.device.exists("PIN-tab-sel-mdpi.png")
        
    def I_enter_the_email_address(self, *args):
        self.device.click("email-field-mdpi.png")
        self.device.type(args[0])
        self.device.press('back')
        
        
    def I_enter_the_password(self, *args):
        self.device.click("password-field-mdpi.png")
        self.device.type(args[0])
        self.device.press('back')

    def I_enter_the_mobile_number(self, *args):
        self.device.click(Pattern("mobile-number-field-mdpi.png").similar(0.91).targetOffset(-2,49))
        # make sure theres nothing prefilled
        if not self.device.exists("mobilenumber-prefill-mdpi.png"):
            for i in range(15):
                self.device.press('del') 
        self.device.type(args[0])
        self.device.press('back')

    def I_enter_the_PIN(self, *args):
        self.device.click("enter-PIN-field-mdpi.png")
        self.device.type(args[0])
        self.device.press('back')
        
    def I_click_the_login_button(self):
        self.device.click("LogIn-button-mdpi.png")

    