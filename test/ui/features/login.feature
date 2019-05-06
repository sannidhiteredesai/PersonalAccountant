Feature: Login

    Scenario: Success test for login
        Given I am on login page
        And I enter valid username and password
        When I click on "Submit" button
        Then login is successful

    Scenario: Failure test for login
        Given I am on login page
        And I enter invalid username or password
        When I click on "Submit" button
        Then login fails
