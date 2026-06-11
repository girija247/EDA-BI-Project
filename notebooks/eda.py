import pandas as pd

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS PROJECT")
print("=" * 60)

# ==================================================
# LOAD DATASET
# ==================================================

try:
    df = pd.read_csv("../data/SampleSuperstore.csv", encoding="latin1")
    print("\nDataset Loaded Successfully!")
except Exception as e:
    print("\nError Loading Dataset:")
    print(e)
    exit()

# ==================================================
# DATASET INFORMATION
# ==================================================

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print(df.info())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

# ==================================================
# MISSING VALUES
# ==================================================

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

print(df.isnull().sum())

# ==================================================
# DUPLICATE ROWS
# ==================================================

print("\n" + "=" * 60)
print("DUPLICATE ROWS")
print("=" * 60)

duplicates = df.duplicated().sum()
print("Duplicate Rows Found:", duplicates)

if duplicates > 0:
    df.drop_duplicates(inplace=True)
    print("Duplicates Removed Successfully")
else:
    print("No Duplicates Found")

# ==================================================
# HANDLE MISSING VALUES
# ==================================================

print("\n" + "=" * 60)
print("HANDLING MISSING VALUES")
print("=" * 60)

df.fillna(0, inplace=True)

print(df.isnull().sum())

# ==================================================
# DATE CONVERSION
# ==================================================

print("\n" + "=" * 60)
print("DATE CONVERSION")
print("=" * 60)

if "Order Date" in df.columns:
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    print("Order Date Converted")

if "Ship Date" in df.columns:
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])
    print("Ship Date Converted")

# ==================================================
# SAVE CLEAN DATASET
# ==================================================

df.to_csv("../data/clean_sales.csv", index=False)

print("\nClean Dataset Saved Successfully!")

# ==================================================
# DESCRIPTIVE STATISTICS
# ==================================================

print("\n" + "=" * 60)
print("DESCRIPTIVE STATISTICS")
print("=" * 60)

print(df[["Sales", "Profit"]].describe())

# ==================================================
# MEAN
# ==================================================

print("\nAverage Sales:")
print(df["Sales"].mean())

print("\nAverage Profit:")
print(df["Profit"].mean())

# ==================================================
# MEDIAN
# ==================================================

print("\nMedian Sales:")
print(df["Sales"].median())

print("\nMedian Profit:")
print(df["Profit"].median())

# ==================================================
# MINIMUM VALUES
# ==================================================

print("\nMinimum Sales:")
print(df["Sales"].min())

print("\nMinimum Profit:")
print(df["Profit"].min())

# ==================================================
# MAXIMUM VALUES
# ==================================================

print("\nMaximum Sales:")
print(df["Sales"].max())

print("\nMaximum Profit:")
print(df["Profit"].max())

# ==================================================
# STANDARD DEVIATION
# ==================================================

print("\nSales Standard Deviation:")
print(df["Sales"].std())

print("\nProfit Standard Deviation:")
print(df["Profit"].std())

# ==================================================
# CATEGORY ANALYSIS
# ==================================================

print("\n" + "=" * 60)
print("CATEGORY COUNTS")
print("=" * 60)

print(df["Category"].value_counts())

# ==================================================
# REGION ANALYSIS
# ==================================================

if "Region" in df.columns:

    print("\n" + "=" * 60)
    print("REGION COUNTS")
    print("=" * 60)

    print(df["Region"].value_counts())

# ==================================================
# TOP 10 PRODUCTS
# ==================================================

if "Product Name" in df.columns:

    print("\n" + "=" * 60)
    print("TOP 10 PRODUCTS")
    print("=" * 60)

    print(df["Product Name"].value_counts().head(10))

# ==================================================
# TOTAL SALES & PROFIT
# ==================================================

print("\n" + "=" * 60)
print("BUSINESS KPIs")
print("=" * 60)

print("Total Sales :", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))

# ==================================================
# SAVE REPORT
# ==================================================

report_file = "../reports/statistics_report.txt"

with open(report_file, "w") as f:

    f.write("DESCRIPTIVE STATISTICS REPORT\n")
    f.write("=" * 50 + "\n\n")

    f.write(f"Total Sales: {df['Sales'].sum():.2f}\n")
    f.write(f"Total Profit: {df['Profit'].sum():.2f}\n")
    f.write(f"Average Sales: {df['Sales'].mean():.2f}\n")
    f.write(f"Average Profit: {df['Profit'].mean():.2f}\n")
    f.write(f"Median Sales: {df['Sales'].median():.2f}\n")
    f.write(f"Median Profit: {df['Profit'].median():.2f}\n")

print("\nStatistics Report Saved Successfully!")
print(report_file)

print("\nEDA Phase 3 Completed Successfully!")