#problem 02

import pandas as pd

# Load dataset
df = pd.read_csv("sales_large.csv")

# Compute total sales for each product in each region
total_sales = df.groupby(["Region", "Product"])["Sales"].sum().reset_index()

# Identify the product with the highest total sales
top_product = df.groupby("Product")["Sales"].sum().idxmax()

print(total_sales)
print("Top Product:", top_product)
