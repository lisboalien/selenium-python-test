"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page
"""

from selenium.webdriver.common.by import By
from random import choice

from pages.common import CommonPage


class DuckDuckGoResultPage(CommonPage):
    # Locators

    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    RESULT_IMAGES = (By.CSS_SELECTOR, 'span.tile--img__title')
    RESULT_VIDEOS = (By.XPATH, '//h6/a')
    RESULT_NEWS = (
        By.XPATH, '//div[contains(@class, "result--news")]//h2/a[1]')
    SEARCH_INPUT = (By.ID, 'search_form_input')
    SEARCH_BUTTON = (By.ID, 'search_button')
    MORE_RESULTS_BUTTON = (By.CSS_SELECTOR, 'a.result--more__btn')
    IMAGES_BUTTON = (By.CSS_SELECTOR, 'a.js-zci-link--images')
    VIDEOS_BUTTON = (By.CSS_SELECTOR, 'a.js-zci-link--videos')
    NEWS_BUTTON = (By.CSS_SELECTOR, 'a.js-zci-link--news')
    RESULT_PER_REGION_SWITCH = (
        By.CSS_SELECTOR, 'div.js-region-filter-switch > span')
    REGION_DROPDOWN_BUTTON = (By.CSS_SELECTOR, 'div.dropdown--region > a')
    COUNTRIES_LIST = (By.XPATH, '//a[contains(@class, "modal__list__link")]')
    SETTINGS_BUTTON = (By.CSS_SELECTOR, 'div.dropdown--settings')
    SITE_ICONS_CHECKBOX = (By.XPATH, '//label[@for="setting_kf"]')
    SITE_ICONS_CONFIG_VALUE = (
        By.XPATH, '//div[contains(@class, "js-settings-dropdown-appearance")]/div[2]')
    SITE_ICONS = (By.CSS_SELECTOR, 'span.result__icon')

    # Initializer

    def __init__(self, browser):
        super().__init__(browser)

    # Interaction Element Methods

    def set_search_input(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.clear
        search_input.send_keys(phrase)

    def get_site_icons_config_value(self):
        value = self.browser.find_element(
            *self.REGION_DROPDOWN_BUTTON).text
        return value

    def get_search_input_value(self):
        value = self.browser.find_element(
            *self.SEARCH_INPUT).get_attribute('value')
        return value

    def get_selected_country(self):
        value = self.browser.find_element(
            *self.REGION_DROPDOWN_BUTTON).get_attribute('innerText')
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

    def btn_settings_click(self):
        self.browser.find_element(*self.SETTINGS_BUTTON).click()

    def chk_site_icons_click(self):
        self.browser.find_element(*self.SITE_ICONS_CHECKBOX).click()

    def switch_result_per_region(self):
        self.browser.find_element(*self.RESULT_PER_REGION_SWITCH).click()

    def get_select_box_country_list(self):
        self.browser.find_element(*self.REGION_DROPDOWN_BUTTON).click()
        countries = self.browser.find_elements(*self.COUNTRIES_LIST)
        return countries

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

    def get_result_links_icons_status(self):
        icons = self.browser.find_elements(*self.SITE_ICONS)
        icons_status = [link.get_attribute('class') for link in icons]
        return icons_status

    def search(self, phrase):
        self.set_search_input(phrase)
        self.btn_search_click()

    def select_country(self, browser, region):
        self.switch_result_per_region()
        countries = self.get_select_box_country_list()
        country = self.find_webelement_on_list(region, countries)
        country.click()
