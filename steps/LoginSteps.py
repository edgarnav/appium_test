from behave import given, when, then
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.MyAccountPage import MyAccountPage


class LoginSteps:

    # Flujo principal

    @given("Preparar clases para el flujo de login")
    def objets_class(context):
        context.login_page = LoginPage(context.driver)
        context.home_page = HomePage(context.driver)
        context.your_account_page = MyAccountPage(context.driver)

    @when("Verificar vista home")
    def verify_home_page(context):
        context.home_page.verify_home_activity()

    @when("Presionar boton tu cuenta")
    def press_your_account_button(context):
        context.home_page.press_your_account_button()

    @when("Presionar boton login en tu cuenta")
    def press_login_button_your_account(context):
        if context.your_account_page.verify_user_logged():
            context.home_page.press_your_account_button()
            context.your_account_page.press_login_button()

    @then("Validar vista login")
    def verify_login_page(context):
        context.login_page.verify_login_activity()

    @when("Ingresar usuario y contraseña {user} {password}")
    def send_user_password(context, user, password):
        context.login_page.send_user_password(user, password)

    @then("Presionar boton iniciar sesion")
    def press_login_button(context):
        context.login_page.press_login_button()

    @then("Validar home despues de login")
    def verify_home_activity_after_login(context):
        context.home_page.verify_home_activity()