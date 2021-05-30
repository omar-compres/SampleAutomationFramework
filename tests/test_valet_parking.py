import time

from selenium import webdriver


class TestValetParking:

    def test_sample_script(self):
        browser = webdriver.Chrome()
        browser.get('https://google.com')
        time.sleep(5)


