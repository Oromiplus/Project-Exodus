"""
Project Exodus 2.0

Customer Generator
"""

import random

import pandas as pd
from faker import Faker

from config import NUMBER_OF_CUSTOMERS

fake = Faker()


def generate_customers():

    customer_types = [
        "Individual",
        "SME",
        "Enterprise"
    ]

    locations = [
        ("Ibadan", "Oyo"),
        ("Lagos", "Lagos"),
        ("Abeokuta", "Ogun"),
        ("Osogbo", "Osun"),
        ("Akure", "Ondo"),
        ("Ado-Ekiti", "Ekiti"),
        ("Ilorin", "Kwara")
    ]

    customers = []

    for i in range(NUMBER_OF_CUSTOMERS):

        customer_id = f"C{i + 1:05d}"

        customer_type = random.choices(
            customer_types,
            weights=[40, 45, 15]
        )[0]

        city, state = random.choice(locations)

        if customer_type == "Individual":
            customer_name = fake.name()
        else:
            customer_name = fake.company()

        customers.append({
            "Customer_ID": customer_id,
            "Customer_Name": customer_name,
            "Customer_Type": customer_type,
            "City": city,
            "State": state
        })

    return pd.DataFrame(customers)