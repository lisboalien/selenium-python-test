"""
This module contains step definitions for search.feature
"""

from pytest_bdd import scenarios, given, when, then, parsers

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from pages.common import CommonPage


# Scenarios

scenarios('../features/search.feature')


# Given Steps

@given(parsers.parse('the user searches for "{initial}"'))
@given(parsers.parse('the user searches for the phrase:\n"""{initial}"""'))
@given('the user searches for "<initial>"')
def search_phrase(browser, initial):
    search_page = DuckDuckGoSearchPage(browser)
    search_page.search(initial)


@given(parsers.parse('the user writes "{initial}" in search input'))
@given('the user writes "<initial>" in search input')
def search_input(browser, initial):
    search_page = DuckDuckGoSearchPage(browser)
    search_page.set_search_input(initial)


@given(parsers.parse('the user changes the country to "{region}"'))
@given('the user changes the country to "<region>"')
def set_result_per_region(browser, region):
    result_page = DuckDuckGoResultPage(browser)
    result_page.select_country(browser, region)


# When Steps

@when('the user selects one of the auto-complete suggestions')
def select_auto_complete_suggestion(browser):
    search_page = DuckDuckGoSearchPage(browser)
    search_page.auto_complete_term_selection()


@when('the user changes to image search')
def changing_to_image_search(browser):
    result_page = DuckDuckGoResultPage(browser)
    result_page.btn_images_click()


@when('the user changes to video search')
def changing_to_video_search(browser):
    result_page = DuckDuckGoResultPage(browser)
    result_page.btn_videos_click()


@when('the user changes to news search')
def changing_to_news_search(browser):
    result_page = DuckDuckGoResultPage(browser)
    result_page.btn_news_click()


@when('the user access the settings dropdown menu')
def settings_dropdown_menu(browser):
    result_page = DuckDuckGoResultPage(browser)
    result_page.btn_settings_click()


@when('the user disables the site icons configuration')
def site_icons_configuration(browser):
    result_page = DuckDuckGoResultPage(browser)
    result_page.chk_site_icons_click()


@when(parsers.parse('the user searches from result page for "{initial}"'))
@when('the user searches from result page for "<initial>"')
def search_from_result_page(browser, initial):
    result_page = DuckDuckGoResultPage(browser)
    result_page.search(initial)

# Then Steps


@then('the search result query, link and title is like the searched term')
def check_search_results(browser, initial):
    results_have_one(browser, initial)
    result_links(browser, initial)
    result_text(browser, initial)


@then(parsers.parse('the search result query is "{result}"'))
@then('the search result query is "<result>"')
def results_have_one(browser, result):
    result_page = DuckDuckGoResultPage(browser)
    assert result in result_page.get_search_input_value()


@then(parsers.parse('the search result links pertain to "{phrases}"'))
@then('the search result links pertain to "<phrases>"')
def result_links(browser, phrases):
    result_page = DuckDuckGoResultPage(browser)
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrases.lower() in t.lower()]
    assert len(matches) > 0


@then(parsers.parse('the search result title contains "{phrase}"'))
@then('the search result links pertain to "<phrase>"')
def result_text(browser, phrase):
    result_page = DuckDuckGoResultPage(browser)
    assert phrase in result_page.title()


@then('the second page result also pertain to the searched term')
def second_page_search(browser, initial):
    result_page = DuckDuckGoResultPage(browser)
    result_page.btn_more_results_click()
    check_search_results(browser, initial)


@then('the written term pertain to the auto-complete suggestion')
def check_auto_complete(browser, initial):
    search_page = DuckDuckGoSearchPage(browser)
    common = CommonPage(browser)
    results = search_page.auto_complete_results()
    assert common.list_matches(initial, results)


@then('the search result images pertain to the searched term')
def check_result_images(browser, initial):
    result_page = DuckDuckGoResultPage(browser)
    common = CommonPage(browser)
    titles = result_page.result_image_titles()
    assert common.list_matches(initial, titles)


@then('the search result videos pertain to the searched term')
def check_result_videos(browser, initial):
    result_page = DuckDuckGoResultPage(browser)
    common = CommonPage(browser)
    titles = result_page.result_videos_titles()
    assert common.list_matches(initial, titles)


@then('the search result news pertain to the searched term')
def check_result_news(browser, initial):
    result_page = DuckDuckGoResultPage(browser)
    common = CommonPage(browser)
    titles = result_page.result_news_titles()
    assert common.list_matches(initial, titles)


@then('the site icons are not displayed anymore')
def check_site_icons(browser):
    result_page = DuckDuckGoResultPage(browser)
    icons_status = result_page.get_result_links_icons_status()
    matches = [status for status in icons_status if 'is-hidden' in status]
    assert len(matches) > 0


@then('the selected country changed')
def check_selected_country(browser, region):
    result_page = DuckDuckGoResultPage(browser)
    country = result_page.get_selected_country()
    assert country == region
