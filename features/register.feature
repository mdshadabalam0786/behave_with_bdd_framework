Feature: Register
  @am
  Scenario: Register to account with valid data
    Given I Navigate to home page
    When I click on my account button on homepage
    And I click on register button
    And I enter below details into mandatory fields
    |first_name|last_name|email|mobile|password|confirm_password|
    |shadab|alam|alam@gmail.com|7050327916|admin@123|admin@123|
    Then Account should get created
