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
def step_search_phrase(browser, initial):
    search_page = DuckDuckGoSearchPage(browser)
    search_page.search(initial)


@given(parsers.parse('the user writes "{initial}" in search input'))
@given('the user writes "<initial>" in search input')
def step_search_input(browser, initial):
    search_page = DuckDuckGoSearchPage(browser)
    search_page.set_search_input(initial)


@given(parsers.parse('the user changes the country to "{region}"'))
@given('the user changes the country to "<region>"')
def step_set_result_per_region(browser, region):
    result_page = DuckDuckGoResultPage(browser)
    result_page.select_country(region)


# When Steps

@when('the user selects one of the auto-complete suggestions')
def step_select_auto_complete_suggestion(browser):
    search_page = DuckDuckGoSearchPage(browser)
    search_page.auto_complete_term_selection()


@when('the user changes to image search')
def step_changing_to_image_search(browser):
    result_page = DuckDuckGoResultPage(browser)
    result_page.btn_images_click()


@when('the user changes to video search')
def step_changing_to_video_search(browser):
    result_page = DuckDuckGoResultPage(browser)
    result_page.btn_videos_click()


@when('the user changes to news search')
def step_changing_to_news_search(browser):
    result_page = DuckDuckGoResultPage(browser)
    result_page.btn_news_click()


@when('the user access the settings dropdown menu')
def step_settings_dropdown_menu(browser):
    result_page = DuckDuckGoResultPage(browser)
    result_page.btn_settings_click()


@when('the user disables the site icons configuration')
def step_site_icons_configuration(browser):
    result_page = DuckDuckGoResultPage(browser)
    result_page.swich_site_icons_click()


@when(parsers.parse('the user searches from result page for "{initial}"'))
@when('the user searches from result page for "<initial>"')
def step_search_from_result_page(browser, initial):
    result_page = DuckDuckGoResultPage(browser)
    result_page.search(initial)


# Then Steps

@then('the search result query, link and title is like the searched term')
def step_assert_search_results(browser, initial):

    step_assert_result_query(browser, initial)
    step_assert_result_links(browser, initial)
    step_assert_result_text(browser, initial)


@then(parsers.parse('the search result query is "{result}"'))
@then('the search result query is "<result>"')
def step_assert_result_query(browser, result):
    result_page = DuckDuckGoResultPage(browser)
    assert result in result_page.get_search_input_value()


@then(parsers.parse('the search result links pertain to "{phrases}"'))
@then('the search result links pertain to "<phrases>"')
def step_assert_result_links(browser, phrases):
    result_page = DuckDuckGoResultPage(browser)
    titles = result_page.get_result_link_titles()
    matches = [t for t in titles if phrases.lower() in t.lower()]
    assert len(matches) > 0


@then(parsers.parse('the search result title contains "{phrase}"'))
@then('the search result links pertain to "<phrase>"')
def step_assert_result_text(browser, phrase):
    result_page = DuckDuckGoResultPage(browser)
    assert phrase in result_page.get_browser_title()


@then('the second page result also pertain to the searched term')
def step_assert_second_page_search(browser, initial):
    result_page = DuckDuckGoResultPage(browser)
    result_page.btn_more_results_click()
    step_assert_search_results(browser, initial)


@then('the written term pertain to the auto-complete suggestion')
def step_assert_auto_complete(browser, initial):
    search_page = DuckDuckGoSearchPage(browser)
    common = CommonPage(browser)
    results = search_page.auto_complete_results()
    assert common.list_matches(initial, results)


@then('the search result images pertain to the searched term')
def step_assert_result_images(browser, initial):
    result_page = DuckDuckGoResultPage(browser)
    common = CommonPage(browser)
    titles = result_page.get_result_image_titles()
    assert common.list_matches(initial, titles)


@then('the search result videos pertain to the searched term')
def step_assert_result_videos(browser, initial):
    result_page = DuckDuckGoResultPage(browser)
    common = CommonPage(browser)
    titles = result_page.get_result_videos_titles()
    assert common.list_matches(initial, titles)


@then('the search result news pertain to the searched term')
def step_assert_result_news(browser, initial):
    result_page = DuckDuckGoResultPage(browser)
    common = CommonPage(browser)
    titles = result_page.get_result_news_titles()
    assert common.list_matches(initial, titles)


@then('the site icons are not displayed anymore')
def step_assert_site_icons(browser):
    result_page = DuckDuckGoResultPage(browser)
    icons_status = result_page.get_result_links_icons_status()
    matches = [status for status in icons_status if 'is-hidden' in status]
    assert len(matches) > 0


@then('the selected country changed')
def step_assert_selected_country(browser, region):
    result_page = DuckDuckGoResultPage(browser)
    country = result_page.get_selected_country()
    assert country == region
