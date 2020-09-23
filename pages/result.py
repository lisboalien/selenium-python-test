"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page
"""

from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:
    # Locators

    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    RESULT_IMAGES = (By.CSS_SELECTOR, 'span.tile--img__title')
    RESULT_VIDEOS = (By.XPATH, '//h6/a')
    RESULT_NEWS = (By.XPATH, '//div[contains(@class, "result--news")]//h2/a[1]')
    SEARCH_INPUT = (By.ID, 'search_form_input')
    SEARCH_BUTTON = (By.ID, 'search_button')
    MORE_RESULTS_BUTTON = (By.CSS_SELECTOR, 'a.result--more__btn')
    IMAGES_BUTTON = (By.CSS_SELECTOR, 'a.js-zci-link--images')
    VIDEOS_BUTTON = (By.CSS_SELECTOR, 'a.js-zci-link--videos')
    NEWS_BUTTON = (By.CSS_SELECTOR, 'a.js-zci-link--news')

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Element Methods

    def set_search_input(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.clear
        search_input.send_keys(phrase)

    def get_search_input_value(self):
        value = self.browser.find_element(
            *self.SEARCH_INPUT).get_attribute('value')
        return value

    def title(self):
        return self.browser.title

    def btn_search_click(self):
        self.browser.find_element(*self.SEARCH_BUTTON).click()

    def btn_more_results_click(self):
        self.browser.find_element(*self.MORE_RESULTS_BUTTON).click()

    def btn_images_click(self):
        self.browser.find_element(*self.IMAGES_BUTTON).click()

    def btn_videos_click(self):
        self.browser.find_element(*self.VIDEOS_BUTTON).click()

    def btn_news_click(self):
        self.browser.find_element(*self.NEWS_BUTTON).click()

    # Interaction Action Methods

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def result_image_titles(self):
        links = self.browser.find_elements(*self.RESULT_IMAGES)
        titles = [link.text for link in links]
        return titles

    def result_videos_titles(self):
        links = self.browser.find_elements(*self.RESULT_VIDEOS)
        titles = [link.text for link in links]
        return titles

    def result_news_titles(self):
        links = self.browser.find_elements(*self.RESULT_NEWS)
        titles = [link.text for link in links]
        return titles

    def search(self, phrase):
        self.set_search_input(phrase)
        self.btn_search_click()
