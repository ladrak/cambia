Feature: CSV Sorting

Background: Loaded unsorted csv
    Given I have loaded "<unsorted_csv>"

Scenario: Sort Decending

    When I sort it
    Then I should have a "<sorted_csv>"