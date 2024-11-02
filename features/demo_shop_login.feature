Feature: DemoShopLogin
  Background:
    Given Launch Browser
    When Navigate To Url
    When Maximize browser
    And Validate home page
    And Click On Login Button

  Scenario Outline: demo shop login with valid credential
    And Enter username "<username>" and password "<password>"
    And Click On Submit Button
    Then Validate with logout button
    Then close browser

    Examples:
    |username|password|
    | shadab.alam.bca@gmail.com |  Nnagma@1231     |

  Scenario: demo shop login with valid credential
    And Enter username "shadab.alam.bca@gmail.com" and password "Nnagma@1231"
    And Click On Submit Button
    Then Validate with logout button
    Then close browser

