"""
This module contains step definitions for search.feature
"""

from pytest_bdd import scenarios, given, then, parsers

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


# Then Steps

@then(parsers.parse('the search result query is "{result}"'))
@then('the search result query is "<result>"')
def results_have_one(browser, result):
    result_page = DuckDuckGoResultPage(browser)
    assert result == result_page.search_input_value()


@then('the search result query, link and title is like the searched term')
def check_search_results(browser, initial):
    results_have_one(browser, initial)
    result_links(browser, initial)
    result_text(browser, initial)


# And Steps

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
