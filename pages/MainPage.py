from driver_interactions.ElementsInteractions import ElementsInteractions
import config.ConfigFile as ConfigFile


class MainPage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    id_lbl_username = "textview_first"

    def validate_main_activity(self):
        self.verify_activity(".ui.login.MainActivity")

    def validate_lbl_username(self):
        text = self.get_text(self.id_lbl_username, "id")
        if text != "Hello " + ConfigFile.username:
            assert False