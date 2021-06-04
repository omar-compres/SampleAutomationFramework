from pom.driver.driver import Driver
import pytest
import os
import allure


def pytest_runtest_setup():
    Driver.initialize()


def pytest_runtest_teardown(item):
    filename = 'screenshot-' + item.name
    log = Driver.driver.get_log('browser')

    Driver.driver.get_screenshot_as_file(os.path.abspath(os.path.join('.', 'screenshots', filename)))

    allure.attach(Driver.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
    allure.attach(str(log), name="Console Logs", attachment_type=allure.attachment_type.TEXT)

    Driver.quit()
