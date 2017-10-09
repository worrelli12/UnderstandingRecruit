# Created by worre at 07-Oct-17
Feature: Springer Test Automation
  Search function of the Springer Nature Site

  Scenario: Search box present
    Given the Springer homepage is not loaded
    When the Springer homepage is loaded
    Then the Search box is present


  Scenario: Simple Search
    Given the Springer home is loaded
    When the term permissive hypotension is searched for
    Then the results for permissive hypotension are returned

   Scenario Outline: multi Simple Search
    Given the Springer home is loaded
    When the term <searchterm> is searched for
    Then the <results> are returned

    Examples: Search Terms
     |searchterm            |results|
     |blood                 |1,444,000  |
     |Blood                 |1,444,000  |
     |Permissive Hypotension|1,872      |
     |33                    |20,000     |
     |Andre Beckershoff M.A.|1          |
