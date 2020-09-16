"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import choice


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

    # Interaction Element Methods

    def load(self):
        self.browser.get(self.URL)

    def set_search_input(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)

    def btn_search_click(self):
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        search_button.click()

    # Interaction Action Methods

    def search(self, phrase):
        self.set_search_input(phrase)
        self.btn_search_click()

    def auto_complete_results(self):
        results = self.browser.find_elements(*self.AUTO_COMPLETE_RESULTS)
        titles = [result.text for result in results]
        return titles

    def auto_complete_term_selection(self):
        results = self.browser.find_elements(*self.AUTO_COMPLETE_RESULTS)
        test = choice(results)
        text = test.text
        test.click()
