Feature: Search Functionality
  @completed @pom
  Scenario Outline: Search For Valid Product
    Given I Launch The Browser
    When I Navigate to Url on Home pages
    When I Enter valid product "<product>" On Search Input Box
    And I Click On Search Button
    Then Validate the product Should get displayed in list
    Then I close browser
    Examples:
    |product|
    |Hp|
    |Hp|
    # this above line of code is data driven testing and no need for reading data from excel files and instead
   # getting data from features file

  @completed
  Scenario: Search For InValid Product
    Given I Launch The Browser
    When I Navigate to Url on Home pages
    When I Enter invalid product "mobile" On Search Input Box
    And I Click On Search Button
    Then Validate the product Should get displayed in list
    Then I close browser