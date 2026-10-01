import sqlite3
from pathlib import Path

DATABASE_PATH = (
    Path(__file__).resolve().parent.parent
    / "database"
    / "project_exodus.db"
)

conn = sqlite3.connect(DATABASE_PATH)

cursor = conn.cursor()

cursor.execute("""
SELECT
    d.Driver_Name,
    COUNT(del.Delivery_ID) AS total_deliveries,
    ROUND(SUM(del.Profit), 2) AS total_profit
FROM deliveries AS del
JOIN drivers AS d
    ON del.Driver_ID = d.Driver_ID
GROUP BY d.Driver_Name
ORDER BY total_profit DESC
LIMIT 10;
""")

results = cursor.fetchall()

for row in results:
    print(row)

conn.close()
