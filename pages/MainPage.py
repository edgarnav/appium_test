from driver_interactions.ElementsInteractions import ElementsInteractions
import config.ConfigFile as ConfigFile


class MainPage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
