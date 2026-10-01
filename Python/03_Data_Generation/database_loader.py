import sqlite3
from pathlib import Path
import pandas as pd


# Project paths
BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = (
    BASE_DIR.parent.parent
    / "Datasets"
    / "Raw"
    / "Generated_Data"
)

DATABASE_PATH = (
    BASE_DIR.parent.parent
    / "database"
    / "project_exodus.db"
)


# Connect to SQLite database
conn = sqlite3.connect(DATABASE_PATH)


# Load CSV files into SQLite
datasets = {
    "customers": "Customers.csv",
    "drivers": "Drivers.csv",
    "vehicles": "Vehicles.csv",
    "routes": "Routes.csv",
    "deliveries": "Deliveries.csv"
}


for table_name, filename in datasets.items():

    file_path = DATA_PATH / filename

    df = pd.read_csv(file_path)

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


conn.close()

print("\nDatabase creation complete.")