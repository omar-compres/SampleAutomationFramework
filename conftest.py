from pom.driver.driver import Driver
import os
import allure


def pytest_runtest_setup(item):
    headless = headless_flag(item)
    driver_params = {"headless": headless}

    Driver.initialize(**driver_params)


def pytest_runtest_teardown(item):
    filename = 'screenshot-' + item.name
    log = Driver.driver.get_log('browser')

    Driver.driver.get_screenshot_as_file(os.path.abspath(os.path.join('.', 'screenshots', filename)))

    allure.attach(Driver.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=allure.attachment_type.PNG)
    allure.attach(str(log), name="Console Logs", attachment_type=allure.attachment_type.TEXT)

    Driver.quit()


def headless_flag(request):
    return request.config.getoption("-H")

def pytest_addoption(parser):
    parser.addoption("-H", "--headless",
                     dest="headless browser",
                     default="",
                     help="Run headless browser")
