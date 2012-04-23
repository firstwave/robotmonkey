from sikuli.Sikuli import *
import sys, difflib, os

import seemonkey

addImagePath(os.path.dirname(__file__))

device = seemonkey.getDevice()


            
def the_PIN_tab_should_be_selected_by_default():
    device.exists("PIN-tab-sel-mdpi.png")

def the_password_tab_should_be_selected_by_default():
    the_password_login_form_should_be_displayed() 
def the_password_login_form_should_be_displayed():
    device.exists("password-tab-selected-mdpi.png")

def I_enter_the_email_address(*args):
    device.click("email-field-mdpi.png")
    device.type(args[0])
    device.press('back')
    
    
def I_enter_the_password(*args):
    device.click("password-field-mdpi.png")
    device.type(args[0])
    device.press('back')

def I_enter_the_mobile_number(*args):
    device.click(Pattern("mobile-number-field-mdpi.png").similar(0.91).targetOffset(-2,49))
    # make sure theres nothing prefilled
    if not device.exists("mobilenumber-prefill-mdpi.png"):
        for i in range(15):
            device.press('del') 
    device.type(args[0])
    device.press('back')

def I_enter_the_PIN(*args):
    device.click("enter-PIN-field-mdpi.png")
    device.type(args[0])
    device.press('back')
    
def I_click_the_login_button():
    device.click("LogIn-button-mdpi.png")
    # the remaining code is in pklace to workaround latency/session token issues on
    # stage environments!

    retry = 3

    while (retry > 0):
        device.sleep(5000)
        if device.exists(Pattern("login-failed-stage-mdpi.png").similar(0.99)):
            print("WARNING: retrying login. It isn't unusual to see this on stage servers")
            device.click(Pattern("login-failed-stage-mdpi.png").targetOffset(2,72))
            device.sleep(2000)
            device.click("LogIn-button-mdpi.png")
            retry = retry - 1
            
        else:
            retry = 0

def my_browser_launches_to_the_forgot_password_flow():
    device.wait("forgot-password-website-mdpi.png", 30)
def I_exit_the_browser():
    device.press('back')
    