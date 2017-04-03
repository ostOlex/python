Feature: check search result

  Scenario: check that search result contains 8 products
     Given I open browser at home page
     then I search item by "RYSLINGE" text
     then I check is search result contain 8 products