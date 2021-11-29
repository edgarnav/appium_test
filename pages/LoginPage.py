from driver_interactions.ElementsInteractions import ElementsInteractions


class LoginPage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    id_user_input = "emailEditText"
    id_password_input = "passwordEditText"
    id_login_button = "loginButton"
    id_error_message = "errorContainer"
    activity_name_login = ".Login.view.LoginActivity"

    def verify_login_activity(self):
        self.verify_activity(self.activity_name_login)

    def send_user_password(self, user, password):
        self.send_text(self.id_user_input, "id", user)
        self.send_text(self.id_password_input, "id", password)

    def press_login_button(self):
        self.press_element(self.id_login_button, "id")

    def verify_error_message(self):
        self.explicit_wait(self.id_error_message, "id", 10)
