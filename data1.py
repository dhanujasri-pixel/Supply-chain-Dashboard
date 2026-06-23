import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

products = [
    "Laptop", "Mobile", "Keyboard", "Mouse", "Monitor",
    "Printer", "Tablet", "Headphones", "Speaker", "Webcam"
]

suppliers = [
    "TechSource", "GlobalTech", "SmartSupply",
    "VisionElectronics", "PrimeDistributors"
]

regions = [
    "North", "South", "East", "West", "Central"
]

data = []

for i in range(1, 1001):
    order_date = datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 365))
    delivery_days = np.random.randint(1, 15)
    delivery_date = order_date + timedelta(days=delivery_days)

    product = np.random.choice(products)

    quantity = np.random.randint(1, 100)
    inventory = np.random.randint(50, 1000)

    shipping_cost = round(np.random.uniform(50, 1000), 2)

    data.append([
        i,
        product,
        np.random.choice(suppliers),
        order_date.strftime("%Y-%m-%d"),
        delivery_date.strftime("%Y-%m-%d"),
        quantity,
        inventory,
        shipping_cost,
        np.random.choice(regions)
    ])

columns = [
    "Order_ID",
    "Product",
    "Supplier",
    "Order_Date",
    "Delivery_Date",
    "Quantity",
    "Inventory",
    "Shipping_Cost",
    "Region"
]

df = pd.DataFrame(data, columns=columns)

# Add some missing values
for col in ["Supplier", "Shipping_Cost"]:
    idx = np.random.choice(df.index, size=20, replace=False)
    df.loc[idx, col] = np.nan

# Add duplicate rows
duplicates = df.sample(20)
df = pd.concat([df, duplicates], ignore_index=True)

df.to_csv("supply_chain_dataset.csv", index=False)

print("Dataset generated successfully!")
print(df.head())
