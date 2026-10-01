"""
Project Exodus 2.0

Vehicle Generator

Generates realistic Nigerian logistics fleet data.
"""

import random

import pandas as pd

from config import NUMBER_OF_VEHICLES


vehicle_types = [
    "Delivery Van",
    "Light Truck",
    "Pickup Truck",
    "Mini Truck"
]


vehicle_makes = [
    "Toyota",
    "Mitsubishi",
    "Ford",
    "Isuzu",
    "Mercedes-Benz"
]


vehicle_models = {
    "Toyota": ["Hiace", "Hilux", "Dyna"],
    "Mitsubishi": ["Canter", "L200"],
    "Ford": ["Transit", "Ranger"],
    "Isuzu": ["NPR", "NQR"],
    "Mercedes-Benz": ["Sprinter", "Atego"]
}


fuel_types = [
    "Diesel",
    "Petrol"
]


vehicle_statuses = [
    "Available",
    "In Service",
    "Maintenance",
    "Inactive"
]


def generate_vehicles():

    vehicles = []

    for i in range(NUMBER_OF_VEHICLES):

        vehicle_id = f"V{i+1:05d}"

        make = random.choice(vehicle_makes)

        model = random.choice(
            vehicle_models[make]
        )

        vehicle_type = random.choice(vehicle_types)

        year = random.randint(2016, 2025)

        capacity_kg = random.choice(
            [500, 750, 1000, 1500, 2000, 3000, 5000]
        )

        fuel_type = random.choice(fuel_types)

        status = random.choice(vehicle_statuses)
        vehicles.append(
            {
                "Vehicle_ID": vehicle_id,
                "Vehicle_Type": vehicle_type,
                "Make": make,
                "Model": model,
                "Year": year,
                "Capacity_KG": capacity_kg,
                "Fuel_Type": fuel_type,
                "Status": status
            }
        )

    return pd.DataFrame(vehicles)