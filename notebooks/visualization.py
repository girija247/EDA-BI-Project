import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("UNIVARIATE ANALYSIS & VISUALIZATION")
print("=" * 60)

# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

try:
    df = pd.read_csv("../data/clean_sales.csv")
    print("Dataset Loaded Successfully!")
except Exception as e:
    print("Error loading dataset:", e)
    exit()

# --------------------------------------------------
# SALES HISTOGRAM
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(df["Sales"], bins=50)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("../reports/sales_histogram.png")
plt.close()

print("✓ Sales Histogram Saved")

# --------------------------------------------------
# CATEGORY BAR CHART
# --------------------------------------------------

plt.figure(figsize=(8, 5))

df["Category"].value_counts().plot(kind="bar")

plt.title("Product Categories")
plt.xlabel("Category")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("../reports/category_bar_chart.png")
plt.close()

print("✓ Category Bar Chart Saved")

# --------------------------------------------------
# REGION BAR CHART
# --------------------------------------------------

if "Region" in df.columns:

    plt.figure(figsize=(8, 5))

    df["Region"].value_counts().plot(kind="bar")

    plt.title("Orders by Region")
    plt.xlabel("Region")
    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig("../reports/region_bar_chart.png")
    plt.close()

    print("✓ Region Bar Chart Saved")

# --------------------------------------------------
# REGION PIE CHART
# --------------------------------------------------

if "Region" in df.columns:

    plt.figure(figsize=(8, 6))

    df["Region"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.title("Region Distribution")
    plt.ylabel("")

    plt.tight_layout()

    plt.savefig("../reports/region_pie_chart.png")
    plt.close()

    print("✓ Region Pie Chart Saved")

# --------------------------------------------------
# SALES BOXPLOT
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.boxplot(df["Sales"])

plt.title("Sales Box Plot")

plt.tight_layout()

plt.savefig("../reports/sales_boxplot.png")
plt.close()

print("✓ Sales Boxplot Saved")

# --------------------------------------------------
# SUMMARY
# --------------------------------------------------

print("\n" + "=" * 60)
print("ALL VISUALIZATIONS CREATED SUCCESSFULLY")
print("=" * 60)

print("""
Generated Files:

1. sales_histogram.png
2. category_bar_chart.png
3. region_bar_chart.png
4. region_pie_chart.png
5. sales_boxplot.png
""")