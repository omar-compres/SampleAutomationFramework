# SampleAutomationFramework

 SampleAutomationFramework is a sample project created to demonstrate my knowledge about automating test scenarios with Selenium. This automation uses Python as the programming language and pytest as the testing framework. Also, this project is structured following the PageObject model for better clarity and scalability.

## Getting Started


### Prerequisites
* Python 3
* Google Chrome
* Selenium Webdriver for Chrome
* Java (for allure reports)

### Steps for Windows

1. Clone the repository into your machine.

2. Install the virtual environment.
>`pip3 install virtualenv`

>`virtualenv venv`

3. Activate the virtual environment.
>`venv\Scripts\activate.bat`

4. Install all the repository dependencies.
>`pip3 install -r requirements.txt`

5. Run the tests with the following commands to generate an Allure report or use your IDE's test module if the report is not needed.
>`pytest tests -v --alluredir=test-report/`

>`allure serve test-report/`

### Steps for Linux

1. Clone the repository into your machine.

2. Install the virtual environment.
>`pip3 install virtualenv`

>`virtualenv venv`

3. Activate the virtual environment.
>`source venv/bin/activate`

4. Install all the repository dependencies.
>`pip3 install -r requirements.txt`

5. Run the tests with the following commands to generate an Allure report or use your IDE's test module if the report is not needed.
>`pytest tests -v --alluredir=test-report/`

>`allure serve test-report/`
