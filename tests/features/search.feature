Feature: Searching for a term in DuckDuckGo page

  Background: Opening DuckDuckGo home page
    Given the DuckDuckGo home page is displayed

  Scenario: Search DuckDuckGo
    Given the user searches for "panda"
    Then the search result query is "panda"
    And the search result links pertain to "panda"
    And the search result title contains "panda"