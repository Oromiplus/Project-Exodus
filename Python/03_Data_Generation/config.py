"""
Project Exodus 2.0
Configuration File

Central settings for synthetic logistics data generation.
"""

from pathlib import Path


# ==============================
# Dataset Sizes
# ==============================

NUMBER_OF_CUSTOMERS = 500
NUMBER_OF_DRIVERS = 50
NUMBER_OF_VEHICLES = 40
NUMBER_OF_ROUTES = 50
NUMBER_OF_DELIVERIES = 10000


# ==============================
# Date Range
# ==============================

START_DATE = "2025-01-01"
END_DATE = "2026-12-31"


# ==============================
# Project Paths
# ==============================

BASE_DIR = Path(__file__).resolve().parent

OUTPUT_PATH = (
    BASE_DIR.parent.parent
    / "Datasets"
    / "Raw"
    / "Generated_Data"
)


# ==============================
# Delivery Status Distribution
# ==============================

COMPLETED_RATE = 0.90
PENDING_RATE = 0.07
CANCELLED_RATE = 0.03