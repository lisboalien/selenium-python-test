"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:

    # URL

    URL = 'https://duckduckgo.com/'

    # Locators

    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')
    SEARCH_BUTTON = (By.ID, 'search_button_homepage')
    AUTO_COMPLETE_RESULTS = (By.CSS_SELECTOR, 'span.t-normal')

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)

    def set_search_input(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)

    def search(self, phrase):
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        self.set_search_input(phrase)
        search_button.click()

    def auto_complete_results(self):
        results = self.browser.find_elements(*self.AUTO_COMPLETE_RESULTS)
        titles = [results.text for results in results]
        return titles