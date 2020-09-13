"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoResultPage:
    # Locators

    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')
    MORE_RESULTS_BUTTON = (By.CSS_SELECTOR, 'a.result--more__btn')

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interactions Methods

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.browser.title

    def more_results_button_click(self):
        self.browser.find_element(*self.MORE_RESULTS_BUTTON).click()
