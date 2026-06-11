import pandas as pd
import sqlite3

print("=" * 60)
print("SQL BUSINESS ANALYSIS")
print("=" * 60)

# ------------------------------------
# LOAD CLEAN DATA
# ------------------------------------

df = pd.read_csv("../data/clean_sales.csv")

print("Dataset Loaded Successfully!")

# ------------------------------------
# CREATE SQLITE DATABASE
# ------------------------------------

conn = sqlite3.connect("../data/sales.db")

# Save dataframe as SQL table
df.to_sql("sales", conn, if_exists="replace", index=False)

print("Database Created Successfully!")

# ------------------------------------
# BUSINESS QUESTION 1
# TOP 5 PRODUCTS BY REVENUE
# ------------------------------------

print("\nTOP 5 PRODUCTS BY REVENUE")

query1 = """
SELECT
    [Product Name],
    SUM(Sales) AS Revenue
FROM sales
GROUP BY [Product Name]
ORDER BY Revenue DESC
LIMIT 5
"""

print(pd.read_sql(query1, conn))

# ------------------------------------
# BUSINESS QUESTION 2
# MONTHLY SALES TREND
# ------------------------------------

print("\nMONTHLY SALES TREND")

query2 = """
SELECT
    strftime('%m', [Order Date]) AS Month,
    SUM(Sales) AS TotalSales
FROM sales
GROUP BY Month
ORDER BY Month
"""

print(pd.read_sql(query2, conn))

# ------------------------------------
# BUSINESS QUESTION 3
# MOST PROFITABLE CATEGORY
# ------------------------------------

print("\nMOST PROFITABLE CATEGORY")

query3 = """
SELECT
    Category,
    SUM(Profit) AS TotalProfit
FROM sales
GROUP BY Category
ORDER BY TotalProfit DESC
"""

print(pd.read_sql(query3, conn))

# ------------------------------------
# BUSINESS QUESTION 4
# AVERAGE ORDER VALUE
# ------------------------------------

print("\nAVERAGE ORDER VALUE")

query4 = """
SELECT
    AVG(Sales) AS AvgOrderValue
FROM sales
"""

print(pd.read_sql(query4, conn))

# ------------------------------------
# BUSINESS QUESTION 5
# BEST SALES MONTH
# ------------------------------------

print("\nBEST SALES MONTH")

query5 = """
SELECT
    strftime('%m', [Order Date]) AS Month,
    SUM(Sales) AS TotalSales
FROM sales
GROUP BY Month
ORDER BY TotalSales DESC
LIMIT 1
"""

print(pd.read_sql(query5, conn))

# ------------------------------------
# BUSINESS QUESTION 6
# TOP CUSTOMERS
# ------------------------------------

print("\nTOP CUSTOMERS")

query6 = """
SELECT
    [Customer Name],
    SUM(Sales) AS Revenue
FROM sales
GROUP BY [Customer Name]
ORDER BY Revenue DESC
LIMIT 10
"""

print(pd.read_sql(query6, conn))

# ------------------------------------
# BUSINESS QUESTION 7
# REGION PERFORMANCE
# ------------------------------------

print("\nREGION PERFORMANCE")

query7 = """
SELECT
    Region,
    SUM(Sales) AS TotalSales,
    SUM(Profit) AS TotalProfit
FROM sales
GROUP BY Region
"""

print(pd.read_sql(query7, conn))

conn.close()

print("\nAnalysis Completed Successfully!")