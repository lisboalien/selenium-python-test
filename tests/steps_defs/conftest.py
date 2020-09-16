"""
This module contains the project shared fixtures.
"""

import json
import pytest
import selenium.webdriver
from pytest_bdd import given
from pages.search import DuckDuckGoSearchPage


# Hooks

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step} by {exception}')


@pytest.fixture
def config(scope='session'):
    # Read the config file
    with open('config_test.json') as config_file:
        config = json.load(config_file)

    # Assert config so it can be used
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):
    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the setup
    b.quit()


# Shared Given Steps

@given('the DuckDuckGo home page is displayed')
def ddg_home(browser):
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
