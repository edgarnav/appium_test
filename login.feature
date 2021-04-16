Feature: Login

  Scenario: Login with valid email and password

    Given Prepare class
    When Validate login activity
    Then Send user and password
    Then Press login button
    And Validate main page

  Scenario: If the password not fill the length, the sign in button is disabled

    Given Prepare class
    Then Validate login button enabled

  Scenario: Check that the username in the TextView is the text introduced in the username field

    Given Prepare class
    When Validate login activity
    Then Send user and password
    Then Press login button
    Then Validate main page
    And Validate lbl user name
