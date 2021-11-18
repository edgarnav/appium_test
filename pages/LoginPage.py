from driver_interactions.ElementsInteractions import ElementsInteractions


class LoginPage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

