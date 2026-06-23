
import pandas as pd

# Load dataset
df = pd.read_csv("supply_chain_dataset.csv")

# Check dataset information
print(df.info())
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

# Convert date columns
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Delivery_Date'] = pd.to_datetime(df['Delivery_Date'])

# Create Delivery_Time column
df['Delivery_Time'] = (
    df['Delivery_Date'] - df['Order_Date']
).dt.days

# Create Month column
df['Month'] = df['Order_Date'].dt.month_name()

# Display first 5 rows
print(df.head())

# Save cleaned dataset
df.to_csv("cleaned_supply_chain.csv", index=False)
