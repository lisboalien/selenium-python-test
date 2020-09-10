"""
This module contains step definitions for search.feature
"""

from pytest_bdd import scenarios, given, then, parsers

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


# Scenarios

scenarios('../features/search.feature')


# Given Steps

@given(parsers.parse('the user searches for "{text}"'))
@given(parsers.parse('the user searches for the phrase:\n"""{text}"""'))
def search_phrase(browser, text):
    search_page = DuckDuckGoSearchPage(browser)
    search_page.search(text)


# Then Steps

@then(parsers.parse('the search result query is "{phrase}"'))
def results_have_one(browser, phrase):
    result_page = DuckDuckGoResultPage(browser)
    assert phrase == result_page.search_input_value()


# And Steps

@then(parsers.parse('the search result links pertain to "{phrase}"'))
def result_links(browser, phrase):
    result_page = DuckDuckGoResultPage(browser)
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0


@then(parsers.parse('the search result title contains "{phrase}"'))
def result_text(browser, phrase):
    result_page = DuckDuckGoResultPage(browser)
    assert phrase in result_page.title()
