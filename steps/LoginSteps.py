from behave import given, when, then
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage
import config.ConfigFile as ConfigFile

class LoginSteps:

    @given("Prepare class")
    def prepare_class(context):
        context.login = LoginPage(context.driver)
        context.main = MainPage(context.driver)

    @when("Validate login activity")
    def validate_login_activity(context):
        context.login.validate_login_activity()

    @then("Send user and password")
    def send_user_password(context):
        context.login.send_username(ConfigFile.username)
        context.login.send_password(ConfigFile.password)

    @then("Press login button")
    def press_login_button(context):
        context.login.press_login_button()

    @then("Validate main page")
    def validate_main_page(context):
        context.main.validate_main_activity()

    @then("Validate login button enabled")
    def validate_login_enabled(context):
        context.login.validate_attribute_enabled("false")

    @then("Validate lbl user name")
    def validate_lbl_username(context):
        context.main.validate_lbl_username()
