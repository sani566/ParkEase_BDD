
@smoke
Feature: ParkEase Smart Parking

  As a registered ParkEase driver,
  I want my parking fee to be charged automatically
  from my wallet when I exit,
  so that I can leave the plaza without queuing
  at a payment booth.

  Scenario: Successful exit payment for a registered EV
    Given the driver is registered and logged in
    And an electric vehicle is linked to the driver's account
    And the wallet balance is Rs. 1,000
    And the vehicle entered the parking plaza at 9:00 AM
    And the vehicle has been parked for 3 hours 40 minutes
    When the driver exits the parking plaza at 12:40 PM
    Then the payment should be successful
    And the parking fee should be Rs. 280
    And the EV discount should be Rs. 70
    And the service charge should be Rs. 20
    And the total payable should be Rs. 230
    And the final wallet balance should be Rs. 770
    And the system should display "Payment successful – gate opening"
    And the gate should open
    And a receipt with the fee breakdown should be displayed
