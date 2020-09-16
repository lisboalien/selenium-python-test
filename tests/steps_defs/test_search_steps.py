"""
This module contains step definitions for search.feature
"""

from pytest_bdd import scenarios, given, when, then, parsers

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


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


# When Steps

@when('the user selects one of the auto-complete suggestions')
def select_auto_complete_suggestion(browser):
    search_page = DuckDuckGoSearchPage(browser)
    search_page.auto_complete_term_selection()

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
    assert result == result_page.search_input_value()


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
    result_page.more_results_button_click()
    check_search_results(browser, initial)


@then('the written term pertain to the auto-complete suggestion')
def check_auto_complete(browser, initial):
    search_page = DuckDuckGoSearchPage(browser)
    results = search_page.auto_complete_results()
    matches = [t for t in results if initial in t]
    assert len(matches) > 0