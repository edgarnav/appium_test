from driver_interactions.AndroidDriver import AndroidDriver
from driver_interactions.ElementsInteractions import ElementsInteractions
import utilities.Logger as Logger
import time

log = Logger.func_logger()

def before_all(context):
    log.info("Script started")

def after_all(context):
    log.info("Script ended")

def before_scenario(context, scenario):
    context.prepare_driver = AndroidDriver()
    context.driver = context.prepare_driver.android_caps()
    ElementsInteractions(context.driver)

def after_scenario(context, scenario):
    time.sleep(5)
    context.driver.quit()
