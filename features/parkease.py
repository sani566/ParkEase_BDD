
class ParkEase:

    def __init__(self):
        self.logged_in = False
        self.driver = None
        self.vehicles = {}
        self.wallet = 0

    def login(self, driver):
        self.driver = driver
        self.logged_in = True

    def link_vehicle(self, plate, electric):
        self.vehicles[plate] = electric

    def set_wallet(self, rupees):
        self.wallet = rupees

    def exit(self, plate, minutes_parked):

        # Check driver login and vehicle link
        if not self.logged_in or plate not in self.vehicles:
            return {
                "message": "Wallet payment not allowed",
                "parkingFee": 0,
                "evDiscount": 0,
                "serviceCharge": 0,
                "totalPaid": 0,
                "gateOpen": False,
                "receipt": None
            }

        # Free exit within first 15 minutes
        if minutes_parked <= 15:
            return {
                "message": "Payment successful – gate opening",
                "parkingFee": 0,
                "evDiscount": 0,
                "serviceCharge": 0,
                "totalPaid": 0,
                "gateOpen": True,
                "receipt": {
                    "parkingFee": 0,
                    "evDiscount": 0,
                    "serviceCharge": 0,
                    "totalPaid": 0
                }
            }

        # Calculate started hours
        hours = (minutes_parked + 59) // 60

        # Calculate parking fee
        parking_fee = 100 + (hours - 1) * 60

        # Apply maximum parking fee cap
        parking_fee = min(parking_fee, 800)

        # Apply EV discount after the cap
        ev_discount = 0

        if self.vehicles[plate]:
            ev_discount = parking_fee * 25 // 100

        # Add service charge
        service_charge = 20

        # Calculate total payable
        total = parking_fee - ev_discount + service_charge

        # Check wallet balance
        if self.wallet < total:
            return {
                "message": "Insufficient wallet balance",
                "parkingFee": parking_fee,
                "evDiscount": ev_discount,
                "serviceCharge": service_charge,
                "totalPaid": 0,
                "gateOpen": False,
                "receipt": None
            }

        # Deduct payment from wallet
        self.wallet -= total

        # Return successful payment and receipt
        return {
            "message": "Payment successful – gate opening",
            "parkingFee": parking_fee,
            "evDiscount": ev_discount,
            "serviceCharge": service_charge,
            "totalPaid": total,
            "gateOpen": True,
            "receipt": {
                "parkingFee": parking_fee,
                "evDiscount": ev_discount,
                "serviceCharge": service_charge,
                "totalPaid": total
            }
        }

    def wallet_balance(self):
        return self.wallet
