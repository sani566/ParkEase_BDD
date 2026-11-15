# ParkEase Smart Parking – BDD Automation

## Project Overview
ParkEase is a smart parking application that automatically calculates parking fees and deducts payments from registered drivers' wallets when they exit the parking plaza.

This project uses **Python and Behave** to implement Behaviour-Driven Development (BDD) testing with Gherkin scenarios.

## Technologies Used
- Python
- Behave
- Gherkin
- VS Code

## Project Structure
```text
ParkEase_BDD/
│
├── features/
│   ├── steps/
│   │   └── parking_steps.py
│   ├── successful_payment.feature
│   ├── parking_fee_boundaries.feature
│   ├── insufficient_balance.feature
│   └── parkease.py
│
└── README.md
```

## Implemented Features
- Registered driver and linked vehicle verification
- Free parking exit within 15 minutes
- Parking fee calculation and started-hour rounding
- Maximum parking fee cap of Rs. 800
- 25% discount for registered electric vehicles
- Fixed Rs. 20 service charge
- Insufficient wallet balance handling
- Successful wallet payment and receipt generation

## Installation
Install Python, then install Behave:

```bash
pip install behave
```

## Run the Tests
Open the terminal in the main project folder and execute this single command:

```bash
python -m behave
```

## Test Results
The project successfully executed:
- 3 Features Passed
- 8 Scenarios Passed
- 56 Steps Passed
- 0 Failed

The project includes successful payment, parking fee boundary, and insufficient wallet balance scenarios.