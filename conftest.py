from pom.driver.driver import Driver


def pytest_runtest_setup():
    Driver.initialize()


def pytest_runtest_teardown():
    Driver.quit()
