"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page
"""

from selenium.webdriver.common.by import By
from random import choice

from pages.common import CommonPage


class DuckDuckGoResultPage(CommonPage):
    # Locators

    # Lists Locators
    LIST_RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    LIST_RESULT_IMAGES = (By.CSS_SELECTOR, 'span.tile--img__title')
    LIST_RESULT_VIDEOS = (By.XPATH, '//h6/a')
    LIST_RESULT_NEWS = (
        By.XPATH, '//div[contains(@class, "result--news")]//h2/a[1]')
    LIST_COUNTRIES = (By.XPATH, '//a[contains(@class, "modal__list__link")]')
    LIST_SITE_ICONS = (By.CSS_SELECTOR, 'span.result__icon')

    # Input Locators
    TEXTBOX_SEARCH_INPUT = (By.ID, 'search_form_input')

    # Button Locators
    BUTTON_SEARCH = (By.ID, 'search_button')
    BUTTON_MORE_RESULTS = (By.CSS_SELECTOR, 'a.result--more__btn')
    BUTTON_IMAGES = (By.CSS_SELECTOR, 'a.js-zci-link--images')
    BUTTON_VIDEOS = (By.CSS_SELECTOR, 'a.js-zci-link--videos')
    BUTTON_NEWS = (By.CSS_SELECTOR, 'a.js-zci-link--news')
    BUTTON_REGION_DROPDOWN = (By.CSS_SELECTOR, 'div.dropdown--region > a')
    BUTTON_SETTINGS = (By.CSS_SELECTOR, 'div.dropdown--settings')
    SWITCH_SITE_ICONS = (By.XPATH, '//label[@for="setting_kf"]')
    SWITCH_RESULT_PER_REGION = (
        By.CSS_SELECTOR, 'div.js-region-filter-switch > span')

    # Other Locators
    VALUE_SITE_ICONS_CONFIG = (
        By.XPATH, '//div[contains(@class, "js-settings-dropdown-appearance")]/div[2]')

    # Initializer

    def __init__(self, browser):
        super().__init__(browser)

    # Interaction Element Methods

    def set_search_input(self, phrase):
        search_input = self.browser.find_element(*self.TEXTBOX_SEARCH_INPUT)
        search_input.clear
        search_input.send_keys(phrase)

    def get_site_icons_config_value(self):
        value = self.browser.find_element(
            *self.BUTTON_REGION_DROPDOWN).text
        return value

    def get_search_input_value(self):
        value = self.browser.find_element(
            *self.TEXTBOX_SEARCH_INPUT).get_attribute('value')
        return value

    def get_selected_country(self):
        value = self.browser.find_element(
            *self.BUTTON_REGION_DROPDOWN).get_attribute('innerText')
        return value

    def get_browser_title(self):
        return self.browser.title

    def btn_search_click(self):
        self.browser.find_element(*self.BUTTON_SEARCH).click()

    def btn_more_results_click(self):
        self.browser.find_element(*self.BUTTON_MORE_RESULTS).click()

    def btn_images_click(self):
        self.browser.find_element(*self.BUTTON_IMAGES).click()

    def btn_videos_click(self):
        self.browser.find_element(*self.BUTTON_VIDEOS).click()

    def btn_news_click(self):
        self.browser.find_element(*self.BUTTON_NEWS).click()

    def btn_settings_click(self):
        self.browser.find_element(*self.BUTTON_SETTINGS).click()

    def swich_site_icons_click(self):
        self.browser.find_element(*self.SWITCH_SITE_ICONS).click()

    def switch_result_per_region_click(self):
        self.browser.find_element(*self.SWITCH_RESULT_PER_REGION).click()

    # Interaction Action Methods

    def get_result_link_titles(self):
        links = self.browser.find_elements(*self.LIST_RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def get_result_image_titles(self):
        links = self.browser.find_elements(*self.LIST_RESULT_IMAGES)
        titles = [link.text for link in links]
        return titles

    def get_result_videos_titles(self):
        links = self.browser.find_elements(*self.LIST_RESULT_VIDEOS)
        titles = [link.text for link in links]
        return titles

    def get_result_news_titles(self):
        links = self.browser.find_elements(*self.LIST_RESULT_NEWS)
        titles = [link.text for link in links]
        return titles

    def get_result_links_icons_status(self):
        icons = self.browser.find_elements(*self.LIST_SITE_ICONS)
        icons_status = [link.get_attribute('class') for link in icons]
        return icons_status

    def get_select_box_country_list(self):
        self.browser.find_element(*self.BUTTON_REGION_DROPDOWN).click()
        countries = self.browser.find_elements(*self.LIST_COUNTRIES)
        return countries

    def select_country(self, region):
        self.switch_result_per_region_click()
        countries = self.get_select_box_country_list()
        country = self.find_webelement_on_list(region, countries)
        country.click()

    def search(self, phrase):
        self.set_search_input(phrase)
        self.btn_search_click()
