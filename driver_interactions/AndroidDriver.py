from appium import webdriver
import config.ConfigFile as ConfigFile


class AndroidDriver:

    @staticmethod
    def android_caps():
        return webdriver.Remote('http://127.0.0.1:4723/wd/hub', ConfigFile.desired_caps)
