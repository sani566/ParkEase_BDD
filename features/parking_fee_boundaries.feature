
@boundary
Feature: ParkEase Petrol Parking Fee

  Scenario Outline: Calculate petrol parking fee
    Given a petrol car has been parked for "<duration>"
    And the wallet balance is Rs. 1,000
    When the driver exits the parking plaza
    Then the parking fee should be Rs. <fee>
    And the total payable should be Rs. <total>

    Examples: Free and rounding
      | duration   | fee | total |
      | 15 minutes | 0   | 0     |
      | 15m 1s     | 100 | 120   |
      | 60 minutes | 100 | 120   |
      | 61 minutes | 160 | 180   |

    Examples: Daily cap
      | duration | fee | total |
      | 12 hours  | 760 | 780   |
      | 12h 1m    | 800 | 820   |
