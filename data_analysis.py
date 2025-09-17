import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("📂 Current Working Directory:", os.getcwd())
print("📄 Files in this folder:", os.listdir())


# Load your CSV file (make sure name is correct, e.g., "sales.csv")
df = pd.read_csv(r"C:\Users\Mayuri\OneDrive\Desktop\python\sample_sales_data.csv.csv")

# Show first rows
print("\nFirst 5 rows:\n", df.head())

# Column names
print("\nColumns in CSV:", df.columns.tolist())

# --- Analysis ---

# Total Revenue (ignoring missing values)
total_revenue = df["Sales"].sum(skipna=True)
print("\n💰 Total Revenue:", total_revenue)

# Sales by Product
product_sales = df.groupby("Product")["Sales"].sum()
print("\n📊 Sales by Product:\n", product_sales)

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()
print("\n📊 Sales by Category:\n", category_sales)

# Sales by Month
monthly_sales = df.groupby("Month")["Sales"].sum()
print("\n📊 Sales by Month:\n", monthly_sales)

# --- Visualization ---

# Sales by Product
product_sales.plot(kind="bar", figsize=(8,5), color="skyblue", title="Sales by Product")
plt.ylabel("Total Sales")
plt.show()

# Sales by Category
category_sales.plot(kind="bar", figsize=(6,4), color="orange", title="Sales by Category")
plt.ylabel("Total Sales")
plt.show()

# Monthly Sales Trend
monthly_sales.plot(kind="line", marker="o", figsize=(8,5), color="green", title="Monthly Sales Trend")
plt.ylabel("Total Sales")
plt.show()

# Seaborn Category Chart
plt.figure(figsize=(6,4))
sns.barplot(x="Category", y="Sales", data=df, estimator=sum, palette="Set2")
plt.title("Sales by Category (Seaborn)")
plt.show()
