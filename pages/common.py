"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page
"""

class CommonPage:
    # Locators

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Common Assertions
    def list_matches(self, phrase, term_list):
        matches = [t for t in term_list if phrase in t]
        return len(matches) > 0