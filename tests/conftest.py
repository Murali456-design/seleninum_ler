from selenium import webdriver
import pytest
launch = None
def pytest_addoption(parser):
    parser.addoption(
        '--browser', action="store", default="chrome",help="send the browser, by default chrome is selected"
    )


@pytest.fixture(scope="class")
def setup(request):
    global launch
    browser = request.config.getoption("--browser")
    url = "https://rahulshettyacademy.com/angularpractice/"
    browser.lower()
    # launch = ""
    if browser == "edge":
        launch = webdriver.Edge(executable_path="c:\\Murali\\msedgedriver.exe")
    else:
        launch = webdriver.Chrome(executable_path="c:\\Murali\\chromedriver.exe")
    launch.maximize_window()
    launch.get(url)
    # launch.refresh()
    request.cls.launch = launch
    yield
    launch.close()


