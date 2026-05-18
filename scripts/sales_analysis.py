import pandas as pd

# Load dataset
df = pd.read_csv("../data/superstore.csv", encoding='latin1')

# Show first 5 rows
print(df.head())

print(df.columns)

#Total sales
total_sales = df["Sales"].sum()

print("Total Sales:", total_sales)

#total profit
total_profit = df["Profit"].sum()

print("Total Profit:", total_profit)

#Sales By region
region_sales = df.groupby("Region")["Sales"].sum()

print(region_sales)

#Profit by category
category_profit = df.groupby("Category")["Profit"].sum()

print(category_profit)

#Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

#Sales by Region Chart
region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.show()

#Profit by Category
category_profit.plot(kind="bar")

plt.title("Profit by Category")

plt.show()

#Convert Date Column
df["Order Date"] = pd.to_datetime(df["Order Date"])

#Extract Month
df["Month"] = df["Order Date"].dt.month

#Monthly Sales
monthly_sales = df.groupby("Month")["Sales"].sum()

print(monthly_sales)

#Plot Trend
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

#Export Cleaned dataset
df.to_csv("../output/cleaned_sales_data.csv", index=False)

print("Cleaned dataset exported successfully")

