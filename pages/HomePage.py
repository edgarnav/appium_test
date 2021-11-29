from driver_interactions.ElementsInteractions import ElementsInteractions


class HomePage(ElementsInteractions):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    activity_name_home = ".home.view.activity.HomeActivity"
    id_navigation_account_button = "navigation_account"
    id_campaign_banner = "firstBannerImage"
    id_carousel_banner = "carouselImage"

    def verify_home_activity(self):
        self.verify_activity(self.activity_name_home)

    def press_your_account_button(self):
        self.press_element(self.id_navigation_account_button, "id")
