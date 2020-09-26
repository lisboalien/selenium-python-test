Feature: Searching for a term in DuckDuckGo page

  Background: Opening DuckDuckGo home page
    Given the DuckDuckGo home page is displayed


  Scenario: Search DuckDuckGo
    Given the user searches for "panda"
    Then the search result query is "panda"
    And the search result links pertain to "panda"
    And the search result title contains "panda"
    And the second page result also pertain to the searched term


  Scenario Outline: Search for the different phrases
    Given the user searches for "<initial>"
    Then the search result query, link and title is like the searched term
    And the second page result also pertain to the searched term

    Examples:
      | initial |
      | duck    |
      | ball    |

  Scenario: Verifying auto-complete suggestion
    Given the user writes "cracker" in search input
    Then the written term pertain to the auto-complete suggestion

  Scenario: Searching by selecting an auto-complete term
    Given the user writes "development" in search input
    When the user selects one of the auto-complete suggestions
    Then the search result query, link and title is like the searched term

  Scenario: Searching from the result page
    Given the user searches for "red panda"
    When the user searches from result page for "bear"
    Then the search result query is "bear"
    And the search result links pertain to "bear"
    And the search result title contains "bear"

  Scenario: Image search
    Given the user searches for "car"
    When the user changes to image search
    Then the search result images pertain to the searched term

  Scenario: Video search
    Given the user searches for "car"
    When the user changes to video search
    Then the search result videos pertain to the searched term

  Scenario: News search
    Given the user searches for "bicicle"
    When the user changes to news search
    Then the search result news pertain to the searched term

  Scenario: Changing settings
    Given the user searches for "lalala"
    When the user access the settings dropdown menu
    And the user disables the site icons configuration
    Then the site icons are not displayed anymore