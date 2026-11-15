
from behave import given, when, then, register_type
from parse import with_pattern
from parkease import ParkEase


# Convert amounts such as Rs. 1,000 into integers
@with_pattern(r"\d[\d,]*")
def parse_amount(text):
    return int(text.replace(",", ""))


register_type(Amount=parse_amount)


# Compare actual and expected values
def check_value(actual, expected, label):
    assert actual == expected, (
        f"{label}: Expected {expected}, but got {actual}"
    )


# Create ParkEase application
def get_app(context):
    if not hasattr(context, "app"):
        context.app = ParkEase()
    return context.app


# ---------------- GIVEN STEPS ----------------

@given("the driver is registered and logged in")
def step_login(context):
    get_app(context).login("driver1")


@given("an electric vehicle is linked to the driver's account")
def step_link_ev(context):
    context.plate = "EV-101"
    context.app.link_vehicle(context.plate, True)


@given("a petrol vehicle is linked to the driver's account")
def step_link_petrol(context):
    context.plate = "PETROL-101"
    context.app.link_vehicle(context.plate, False)


@given("the wallet balance is Rs. {amount:Amount}")
def step_wallet_balance(context, amount):
    get_app(context).set_wallet(amount)


def parse_duration(value):
    durations = {
        "15 minutes": 15,
        "15m 1s": 16,
        "60 minutes": 60,
        "61 minutes": 61,
        "12 hours": 720,
        "12h 1m": 721
    }
    return durations[value.strip().lower()]


@given('a petrol car has been parked for "{duration}"')
def step_petrol_duration(context, duration):
    app = get_app(context)
    app.login("driver1")

    context.plate = "PETROL-101"
    app.link_vehicle(context.plate, False)

    context.duration = parse_duration(duration)


@given("the vehicle has been parked for 3 hours 40 minutes")
def step_ev_duration(context):
    context.duration = 220


@given("the vehicle entered the parking plaza at 9:00 AM")
def step_entry_time(context):
    context.entry_time = "9:00 AM"


@given("the vehicle has been parked for 60 minutes")
def step_c3_duration(context):
    context.duration = 60


@given("the parking fee is Rs. {amount:Amount}")
def step_expected_parking_fee(context, amount):
    context.expected_parking_fee = amount


@given("the service charge is Rs. {amount:Amount}")
def step_expected_service_charge(context, amount):
    context.expected_service_charge = amount


# ---------------- WHEN STEPS ----------------

@when("the driver exits the parking plaza at 12:40 PM")
def step_exit_ev(context):
    context.result = context.app.exit(
        context.plate,
        context.duration
    )


@when("the driver exits the parking plaza")
def step_exit(context):
    context.result = context.app.exit(
        context.plate,
        context.duration
    )


@when("the driver attempts to pay the parking fee")
def step_attempt_payment(context):
    context.result = context.app.exit(
        context.plate,
        context.duration
    )


# ---------------- THEN STEPS ----------------

@then("the payment should be successful")
def step_payment_success(context):
    check_value(
        context.result["message"],
        "Payment successful – gate opening",
        "Payment message"
    )


@then('the system should display "{message}"')
def step_check_message(context, message):
    check_value(
        context.result["message"],
        message,
        "System message"
    )


@then("the parking fee should be Rs. {amount:Amount}")
def step_check_parking_fee(context, amount):
    check_value(
        context.result["parkingFee"],
        amount,
        "Parking fee"
    )


@then("the total payable should be Rs. {amount:Amount}")
def step_check_total(context, amount):
    check_value(
        context.result["totalPaid"],
        amount,
        "Total payable"
    )


@then("the EV discount should be Rs. {amount:Amount}")
def step_check_discount(context, amount):
    check_value(
        context.result["evDiscount"],
        amount,
        "EV discount"
    )


@then("the service charge should be Rs. {amount:Amount}")
def step_check_service(context, amount):
    check_value(
        context.result["serviceCharge"],
        amount,
        "Service charge"
    )


@then("the final wallet balance should be Rs. {amount:Amount}")
def step_final_wallet(context, amount):
    check_value(
        context.app.wallet_balance(),
        amount,
        "Final wallet balance"
    )


@then("the gate should open")
def step_gate_open(context):
    check_value(
        context.result["gateOpen"],
        True,
        "Gate status"
    )


@then("no amount should be deducted from the wallet")
def step_no_deduction(context):
    check_value(
        context.result["totalPaid"],
        0,
        "Amount deducted"
    )


@then("the wallet balance should remain Rs. {amount:Amount}")
def step_wallet_unchanged(context, amount):
    check_value(
        context.app.wallet_balance(),
        amount,
        "Wallet balance"
    )


@then("the parking exit gate should remain closed")
def step_gate_closed(context):
    check_value(
        context.result["gateOpen"],
        False,
        "Gate status"
    )


@then("a receipt with the fee breakdown should be displayed")
def step_receipt_displayed(context):
    receipt = context.result["receipt"]

    assert receipt is not None, "Expected a receipt, but got None"

    check_value(
        receipt["parkingFee"],
        context.result["parkingFee"],
        "Receipt parking fee"
    )

    check_value(
        receipt["evDiscount"],
        context.result["evDiscount"],
        "Receipt EV discount"
    )

    check_value(
        receipt["serviceCharge"],
        context.result["serviceCharge"],
        "Receipt service charge"
    )

    check_value(
        receipt["totalPaid"],
        context.result["totalPaid"],
        "Receipt total"
    )
