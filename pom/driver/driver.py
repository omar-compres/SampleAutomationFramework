from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver(object):
    driver = None
    wait_timeout = 30
    base_url = ''
    options = Options()

    @classmethod
    def initialize(cls):
        cls.options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(options=cls.options)

    @classmethod
    def quit(cls):
        if cls.driver:
            cls.driver.quit()
