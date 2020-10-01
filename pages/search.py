"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import choice

from pages.common import CommonPage


class DuckDuckGoSearchPage(CommonPage):

    # URL

    URL = 'https://duckduckgo.com/'

    # Locators

    # Lists Locators
    LIST_AUTO_COMPLETE_RESULTS = (By.CSS_SELECTOR, 'span.t-normal')

    # Input Locators
    TEXTBOX_SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    # Button Locators
    BUTTON_SEARCH = (By.ID, 'search_button_homepage')

    # Initializer

    def __init__(self, browser):
        super().__init__(browser)

    # Interaction Element Methods

    def load(self):
        self.browser.get(self.URL)

    def set_search_input(self, phrase):
        self.browser.find_element(*self.TEXTBOX_SEARCH_INPUT).send_keys(phrase)

    def btn_search_click(self):
        self.browser.find_element(*self.BUTTON_SEARCH).click()

    # Interaction Action Methods

    def search(self, phrase):
        self.set_search_input(phrase)
        self.btn_search_click()

    def auto_complete_results(self):
        results = self.browser.find_elements(*self.LIST_AUTO_COMPLETE_RESULTS)
        titles = [result.text for result in results]
        return titles

    def auto_complete_term_selection(self):
        results = self.browser.find_elements(*self.LIST_AUTO_COMPLETE_RESULTS)
        random_result = choice(results)
        random_result.click()
