import pandas as pd

df = pd.read_csv("../data/clean_sales.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])

print("="*60)
print("KPI ANALYSIS")
print("="*60)

# Sales KPIs
total_revenue = df["Sales"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer Name"].nunique()

average_order_value = total_revenue / total_orders

# Profit KPIs
total_profit = df["Profit"].sum()
profit_margin = (total_profit / total_revenue) * 100

# Repeat Customers
repeat_customers = (
    df.groupby("Customer Name")["Order ID"]
      .nunique()
)

repeat_customers = repeat_customers[repeat_customers > 1]

retention_rate = (
    len(repeat_customers)
    / total_customers
) * 100

# Best Region
best_region = (
    df.groupby("Region")["Sales"]
      .sum()
      .idxmax()
)

# Best Product
best_product = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .idxmax()
)

print("\nTotal Revenue:", round(total_revenue,2))
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)
print("Average Order Value:", round(average_order_value,2))

print("\nTotal Profit:", round(total_profit,2))
print("Profit Margin %:", round(profit_margin,2))

print("\nBest Product:", best_product)
print("Best Region:", best_region)

print("\nRepeat Customers:", len(repeat_customers))
print("Retention Rate %:", round(retention_rate,2))