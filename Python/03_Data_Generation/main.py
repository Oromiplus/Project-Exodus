from generators.delivery_generator import generate_deliveries
from generators.customer_generator import generate_customers
from generators.driver_generator import generate_drivers
from generators.vehicle_generator import generate_vehicles
from generators.route_generator import generate_routes
from validators.data_quality import validate_dataframe
from generators.payment_generator import generate_payments

from config import OUTPUT_PATH


OUTPUT_PATH.mkdir(
    parents=True,
    exist_ok=True
)


# ==============================
# Generate Customers
# ==============================

customers = generate_customers()

customer_valid = validate_dataframe(
    customers,
    "Customer_ID",
    "Customers"
)

if customer_valid:
    customers.to_csv(
        OUTPUT_PATH / "Customers.csv",
        index=False
    )


# ==============================
# Generate Drivers
# ==============================

drivers = generate_drivers()

driver_valid = validate_dataframe(
    drivers,
    "Driver_ID",
    "Drivers"
)

if driver_valid:
    drivers.to_csv(
        OUTPUT_PATH / "Drivers.csv",
        index=False
    )


# ==============================
# Generate Vehicles
# ==============================

vehicles = generate_vehicles()

vehicle_valid = validate_dataframe(
    vehicles,
    "Vehicle_ID",
    "Vehicles"
)

if vehicle_valid:
    vehicles.to_csv(
        OUTPUT_PATH / "Vehicles.csv",
        index=False
    )


# ==============================
# Preview
# ==============================

print("\nCustomers Preview:")
print(customers.head())

print("\nDrivers Preview:")
print(drivers.head())

print("\nVehicles Preview:")
print(vehicles.head())


# ==============================
# Generate Routes
# ==============================

routes = generate_routes()

route_valid = validate_dataframe(
    routes,
    "Route_ID",
    "Routes"
)

if route_valid:
    routes.to_csv(
        OUTPUT_PATH / "Routes.csv",
        index=False
    )


# ==============================
# Generate Deliveries
# ==============================
print("\n>>> STARTING DELIVERY GENERATION <<<")
deliveries = generate_deliveries(
    customers,
    drivers,
    vehicles,
    routes
)

delivery_valid = validate_dataframe(
    deliveries,
    "Delivery_ID",
    "Deliveries"
)

if delivery_valid:
    deliveries.to_csv(
        OUTPUT_PATH / "Deliveries.csv",
        index=False
    )


# ==============================
# Generate Payments
# ==============================

payments = generate_payments(
    deliveries
)

payment_valid = validate_dataframe(
    payments,
    "Payment_ID",
    "Payments"
)

if payment_valid:
    payments.to_csv(
        OUTPUT_PATH / "Payments.csv",
        index=False
    )


# ==============================
# Previews
# ==============================

print("\n")