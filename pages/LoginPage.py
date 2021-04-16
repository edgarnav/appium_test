from driver_interactions.ElementsInteractions import ElementsInteractions


class LoginPage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    id_email_input = "username"
    id_password_input = "password"
    id_login_button = "login"

    def validate_login_activity(self):
        self.verify_activity(".ui.login.LoginActivity")

    def send_username(self, username):
        self.send_text(username, self.id_email_input, "id")

    def send_password(self, password):
        self.send_text(password, self.id_password_input, "id")

    def press_login_button(self):
        self.press_element(self.id_login_button, "id")

    def validate_attribute_enabled(self, status):
        attribute = self.get_attribute(self.id_login_button, "id", "enabled")
        if attribute != status:
            assert False

