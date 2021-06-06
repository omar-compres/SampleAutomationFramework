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
        cls.options.add_argument('--headless')
        cls.options.add_argument('--no-sandbox')
        cls.options.add_argument('--disable-dev-shm-usage')
        cls.driver = webdriver.Chrome(options=cls.options)

    @classmethod
    def quit(cls):
        if cls.driver:
            cls.driver.quit()
