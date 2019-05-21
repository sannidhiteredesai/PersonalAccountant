Feature: Notifications

    @current
    Scenario: Notifications of FDs maturing till next 45 days
        Given I am a logged in user
        When I navigate to "notifications" page
        Then I see the fds that are maturing till next 45 days
