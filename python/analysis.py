# E-Commerce Sales Analysis

import pandas as pd

# Load the dataset
df = pd.read_csv("data/orders.csv")

# Display the data
print(df)

# Calculate revenue
df["revenue"] = df["quantity"] * df["price"]

# Total revenue
total_revenue = df["revenue"].sum()
print("Total Revenue:", total_revenue)

# Total orders
total_orders = df["order_id"].nunique()
print("Total Orders:", total_orders)

# Best-selling products
best_selling = (
    df.groupby("product")["quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("Best-Selling Products:")
print(best_selling)
