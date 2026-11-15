
@negative
Feature: ParkEase Wallet Payment

  Scenario: Payment fails due to insufficient wallet balance
    Given the driver is registered and logged in
    And a petrol vehicle is linked to the driver's account
    And the vehicle has been parked for 60 minutes
    And the parking fee is Rs. 100
    And the service charge is Rs. 20
    And the wallet balance is Rs. 119
    When the driver attempts to pay the parking fee
    Then the system should display "Insufficient wallet balance"
    And no amount should be deducted from the wallet
    And the wallet balance should remain Rs. 119
    And the parking exit gate should remain closed
