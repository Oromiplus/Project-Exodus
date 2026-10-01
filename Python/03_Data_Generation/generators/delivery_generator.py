"""
Project Exodus 2.0

Delivery Generator

Generates realistic logistics delivery transaction data.
"""

import random

from datetime import date, timedelta

import pandas as pd

from config import NUMBER_OF_DELIVERIES

delivery_statuses = [
    "Completed",
    "In Transit",
    "Pending",
    "Cancelled"
]
START_DATE = date(2025, 1, 1)
END_DATE = date(2026, 12, 31)

def generate_deliveries(
    customers,
    drivers,
    vehicles,
    routes
):

    deliveries = []

    for i in range(NUMBER_OF_DELIVERIES):

        delivery_id = f"DL{i+1:06d}"

        customer_id = random.choice(
            customers["Customer_ID"].tolist()
        )

        driver_id = random.choice(
            drivers["Driver_ID"].tolist()
        )

        vehicle_id = random.choice(
            vehicles["Vehicle_ID"].tolist()
        )

        route_id = random.choice(
            routes["Route_ID"].tolist()
        )
        delivery_date = START_DATE + timedelta(
            days=random.randint(
                0,
                (END_DATE - START_DATE).days
            )
        )

        status = random.choice(
            delivery_statuses
        )
        route = routes[
            routes["Route_ID"] == route_id
        ].iloc[0]

        distance_km = route["Distance_KM"]
        delivery_time_min = round(
            (distance_km / 45) * 60
            + random.randint(10, 45)
        )

        delivery_fee = round(
            1500
            + (distance_km * random.uniform(80, 120)),
            2
        )

        fuel_cost = round(
            distance_km
            * random.uniform(35, 55),
            2
        )

        profit = round(
            delivery_fee - fuel_cost,
            2
        )

        deliveries.append(
            {
                "Delivery_ID": delivery_id,
                "Delivery_Date": delivery_date,
                "Customer_ID": customer_id,
                "Driver_ID": driver_id,
                "Vehicle_ID": vehicle_id,
                "Route_ID": route_id,
                "Distance_KM": distance_km,
                "Delivery_Time_Min": delivery_time_min,
                "Delivery_Fee": delivery_fee,
                "Fuel_Cost": fuel_cost,
                "Profit": profit,
                "Status": status
            }
        )

    return pd.DataFrame(deliveries)


    
