import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from faker import Faker

@pytest.fixture(scope="session")
def faker():
    return Faker()

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose your language: ru, en, es, fr")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = OptionsFirefox()
        options.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    if user_language == "ru":
        print("\nuse russian language..")
    elif user_language == "en":
        print("\nuse english language..")
    elif user_language == "es":
        print("\nuse espanian language..")
    elif user_language == "fr":
        print("\nuse french language..")
    else:
        raise pytest.UsageError("--language should be ru, en, es, fr")

    yield browser
    print("\nquit browser..")
    browser.quit()



