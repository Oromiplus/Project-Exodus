import sqlite3

from pathlib import Path

import pandas as pd


# ==============================
# Project Paths
# ==============================

BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = (
    BASE_DIR.parent.parent
    / "Datasets"
    / "Raw"
    / "Generated_Data"
)

DATABASE_DIR = (
    BASE_DIR.parent.parent
    / "Database"
)

DATABASE_PATH = (
    DATABASE_DIR
    / "project_exodus.db"
)


# ==============================
# Create Database Directory
# ==============================

DATABASE_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ==============================
# Connect to SQLite Database
# ==============================

conn = sqlite3.connect(
    DATABASE_PATH
)


# ==============================
# Dataset Configuration
# ==============================

datasets = {

    "customers": "Customers.csv",

    "drivers": "Drivers.csv",

    "vehicles": "Vehicles.csv",

    "routes": "Routes.csv",

    "deliveries": "Deliveries.csv",

    "payments": "Payments.csv"

}


# ==============================
# Load CSV Files into SQLite
# ==============================

for table_name, filename in datasets.items():

    file_path = DATA_PATH / filename

    df = pd.read_csv(
        file_path
    )

    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )

    print(
        f"{table_name}: "
        f"{len(df)} rows loaded"
    )


# ==============================
# Close Database Connection
# ==============================

conn.close()

print("\nDatabase creation complete.")