import nativedriver, time

nd = nativedriver.AndroidNativeDriverBuilder().withDefaultServer().build();

def the_app_is_started():
    nd.startActivity("com.paypal.android.p2pmobile.activity.IntroActivity")

def I_click(text):
    t = text.lower()
    if t == "the log in button":
        nd.getKeyboard().sendKeys([nativedriver.AndroidKeys.DPAD_DOWN, nativedriver.AndroidKeys.ENTER])
        #nativedriver.clickId(nd, "login_widget_login_button_email")
    elif t == "agree":
        nativedriver.clickId(nd, "agree_to_terms_btn")
    elif t == "login":
        nativedriver.clickId(nd, "button_login_dash")
    else:
        nativedriver.clickText(nd, text)

def I_press(key):
    if key == back:
        nd.navigate().back()

def the_password_tab_is_selected():
    nativedriver.clickId(nd, "loginPhoneLeftTab")
    
def I_enter_the_email_address(emailAddress):
    nativedriver.clickId(nd, "login_widget_email_field")
    nd.getKeyboard().sendKeys([emailAddress])
    nd.navigate().back()
    time.sleep(.5)
    
def I_enter_the_password(password):
    nativedriver.clickId(nd, "login_widget_password_field")
    nd.getKeyboard().sendKeys([password])
    nd.navigate().back()
    time.sleep(.5)
    
def the_account_screen_should_be_displayed():
    nativedriver.waitForActivity(nd, "activity.DashActivity")
    
def the_login_screen_should_be_displayed():
    nativedriver.waitForActivity(nd, "activity.LoginActivity", 5)
    
    
    
