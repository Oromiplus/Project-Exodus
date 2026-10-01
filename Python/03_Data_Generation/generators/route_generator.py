"""
Project Exodus 2.0

Route Generator

Generates realistic Nigerian logistics route data.
"""

import random

import pandas as pd

from config import NUMBER_OF_ROUTES
cities = [
    "Ibadan",
    "Lagos",
    "Abeokuta",
    "Akure",
    "Osogbo",
    "Ado-Ekiti",
    "Ilorin",
    "Benin City",
    "Ile-Ife",
    "Ondo"
]

route_distances = {
    ("Ibadan", "Lagos"): 135,
    ("Ibadan", "Abeokuta"): 80,
    ("Ibadan", "Osogbo"): 90,
    ("Ibadan", "Ilorin"): 160,
    ("Ibadan", "Akure"): 150,
    ("Ibadan", "Ado-Ekiti"): 115,

    ("Lagos", "Abeokuta"): 110,
    ("Lagos", "Benin City"): 320,

    ("Abeokuta", "Lagos"): 110,
    ("Abeokuta", "Ibadan"): 80,

    ("Osogbo", "Ile-Ife"): 35,
    ("Osogbo", "Akure"): 100,
    ("Osogbo", "Ilorin"): 100,

    ("Akure", "Ondo"): 45,
    ("Akure", "Benin City"): 115,
    ("Akure", "Ado-Ekiti"): 75,

    ("Ado-Ekiti", "Ilorin"): 140,
    ("Ado-Ekiti", "Akure"): 75,

    ("Ilorin", "Benin City"): 300,

    ("Ile-Ife", "Ibadan"): 60,
    ("Ile-Ife", "Akure"): 115
}

route_types = [
    "Intra-State",
    "Inter-State"
]

def generate_routes():

    routes = []
    for i in range(NUMBER_OF_ROUTES):

        origin, destination = random.choice(
            list(route_distances.keys())
        )

        distance_km = route_distances[
            (origin, destination)
        ]

        estimated_time_min = round(
            (distance_km / 45) * 60
            + random.randint(10, 30)
        ) 
        route_type = random.choice(route_types)

        route_id = f"R{i+1:05d}"
        routes.append(
            {
                "Route_ID": route_id,
                "Origin": origin,
                "Destination": destination,
                "Distance_KM": distance_km,
                "Estimated_Time_Min": estimated_time_min,
                "Route_Type": route_type
            }
        )
    return pd.DataFrame(routes)