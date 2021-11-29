from driver_interactions.ElementsInteractions import ElementsInteractions


class MyAccountPage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    id_login_button = "loginButton"
    id_create_account_button = "createAccountText"
    id_close_session_button = "logOutText"

    def press_login_button(self):
        self.explicit_wait(self.id_login_button, "id", 5)
        self.press_element(self.id_login_button, "id")

    def verify_user_logged(self):
        if self.explicit_wait(self.id_login_button, "id", 2):
            self.press_element(self.id_login_button, "id")
            return False
        else:
            self.press_element(self.id_close_session_button, "id")
            return True
