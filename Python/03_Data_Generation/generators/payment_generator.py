"""
Project Exodus 2.0

Payment Generator

Generates payment records linked to deliveries.
"""

import random

from datetime import timedelta

import pandas as pd


# ==============================
# Payment Configuration
# ==============================

payment_methods = [
    "Cash",
    "Bank Transfer",
    "Card",
    "Mobile Money"
]


# ==============================
# Generate Payments
# ==============================

def generate_payments(deliveries):

    payments = []

    for i, delivery in deliveries.iterrows():

        payment_id = f"PAY{i + 1:06d}"

        delivery_id = delivery["Delivery_ID"]

        delivery_status = delivery["Status"]

        delivery_date = pd.to_datetime(
            delivery["Delivery_Date"]
        ).date()

        amount = delivery["Delivery_Fee"]

        # ==============================
        # Determine Payment Status
        # ==============================

        if delivery_status == "Completed":

            payment_status = random.choices(
                ["Paid", "Pending"],
                weights=[98, 2],
                k=1
            )[0]

        elif delivery_status == "Pending":

            payment_status = "Pending"

        else:

            payment_status = random.choice(
                ["Failed", "Refunded"]
            )

        # ==============================
        # Payment Date
        # ==============================

        if payment_status == "Paid":

            payment_date = delivery_date + timedelta(
                days=random.randint(0, 2)
            )

        elif payment_status == "Refunded":

            payment_date = delivery_date + timedelta(
                days=random.randint(1, 7)
            )

        else:

            payment_date = delivery_date

        # ==============================
        # Payment Method
        # ==============================

        if payment_status in ["Paid", "Refunded"]:

            payment_method = random.choice(
                payment_methods
            )

        else:

            payment_method = "Not Applicable"

        # ==============================
        # Transaction Reference
        # ==============================

        if payment_status in ["Paid", "Refunded"]:

            transaction_reference = (
                f"TXN-{random.randint(10000000, 99999999)}"
            )

        else:

            transaction_reference = "Not Generated"

        payments.append(
            {
                "Payment_ID": payment_id,
                "Delivery_ID": delivery_id,
                "Payment_Date": payment_date,
                "Payment_Method": payment_method,
                "Payment_Status": payment_status,
                "Amount": amount,
                "Transaction_Reference": transaction_reference
            }
        )

    return pd.DataFrame(payments)