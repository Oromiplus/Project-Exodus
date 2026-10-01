"""
Project Exodus 2.0

Driver Generator

Generates realistic Nigerian logistics driver data.
"""

import random

import pandas as pd

from config import NUMBER_OF_DRIVERS


male_names = [
    "Adebayo",
    "Oluwaseun",
    "Tunde",
    "Chinedu",
    "Emeka",
    "Ibrahim",
    "Sani",
    "Yusuf",
    "Kayode",
    "Segun"
]


female_names = [
    "Aisha",
    "Blessing",
    "Chioma",
    "Yetunde",
    "Funke",
    "Amaka",
    "Bola",
    "Mary",
    "Esther",
    "Grace"
]


surnames = [
    "Ogunleye",
    "Adeyemi",
    "Okafor",
    "Balogun",
    "Adebisi",
    "Eze",
    "Yusuf",
    "Mohammed",
    "Olawale",
    "Ajayi",
    "Oromidayo"
]


def generate_drivers():

    drivers = []

    license_classes = [
        "B",
        "C",
        "D",
        "E"
    ]

    employment_types = [
        "Full-Time",
        "Contract",
        "Part-Time"
    ]

    cities = [
        "Ibadan",
        "Lagos",
        "Abeokuta",
        "Akure",
        "Osogbo",
        "Ado-Ekiti",
        "Ilorin"
    ]

    statuses = [
        "Active",
        "Inactive",
        "On Leave"
    ]

    for i in range(NUMBER_OF_DRIVERS):

        driver_id = f"D{i+1:05d}"

        gender = random.choice(
            ["Male", "Female"]
        )

        if gender == "Male":
            first_name = random.choice(male_names)
        else:
            first_name = random.choice(female_names)

        surname = random.choice(surnames)

        driver_name = f"{first_name} {surname}"

        phone_number = (
            "080"
            + str(random.randint(10000000, 99999999))
        )

        drivers.append(
            {
                "Driver_ID": driver_id,
                "Driver_Name": driver_name,
                "Gender": gender,
                "Phone_Number": phone_number,
                "License_Class": random.choice(license_classes),
                "Years_Experience": random.randint(1, 20),
                "Employment_Type": random.choice(employment_types),
                "Base_City": random.choice(cities),
                "Status": random.choice(statuses)
            }
        )

    return pd.DataFrame(drivers)