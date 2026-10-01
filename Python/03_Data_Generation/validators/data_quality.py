"""
Project Exodus 2.0

Data Quality Validator

Performs basic quality checks on generated datasets.
"""

import pandas as pd
def validate_dataframe(df, id_column, dataset_name):

    print(f"\n{'=' * 50}")
    print(f"{dataset_name.upper()} DATA QUALITY REPORT")
    print(f"{'=' * 50}")

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    missing_values = df.isnull().sum().sum()

    duplicate_ids = df[id_column].duplicated().sum()

    print(f"Missing Values: {missing_values}")
    print(f"Duplicate IDs: {duplicate_ids}")

    if missing_values == 0 and duplicate_ids == 0:
        print("STATUS: PASSED")
        return True

    print("STATUS: FAILED")
    return False