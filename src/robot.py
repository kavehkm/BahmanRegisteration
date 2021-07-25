# selenium
from selenium import webdriver


class Robot(object):
    def __init__(self, browser, driver_path):
        if browser == 'firefox':
            self._driver = webdriver.Firefox(executable_path=driver_path)
        elif browser == 'chrome':
            self._driver = webdriver.Chrome(executable_path=driver_path)

    def get(self, url):
        self._driver.get(url)

    def setupForm(self, data):
        pass
