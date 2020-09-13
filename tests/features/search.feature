Feature: Searching for a term in DuckDuckGo page

  Background: Opening DuckDuckGo home page
    Given the DuckDuckGo home page is displayed


  Scenario: Search DuckDuckGo
    Given the user searches for "panda"
    Then the search result query is "panda"
    And the search result links pertain to "panda"
    And the search result title contains "panda"


  Scenario Outline: Search for the different phrases
    Given the user searches for "<initial>"
    Then the search result query, link and title is like the searched term

    Examples:
      | initial  |
      | duck     | 
      | football |