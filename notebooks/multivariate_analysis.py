import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 60)
print("MULTIVARIATE ANALYSIS")
print("=" * 60)

# ------------------------------------
# LOAD DATA
# ------------------------------------

try:
    df = pd.read_csv("../data/clean_sales.csv")
    print("Dataset Loaded Successfully!")
except Exception as e:
    print("Error:", e)
    exit()

# ------------------------------------
# SCATTER PLOT
# SALES VS PROFIT
# ------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(df["Sales"], df["Profit"])

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("../reports/scatter_sales_profit.png")
plt.close()

print("✓ Scatter Plot Saved")

# ------------------------------------
# PAIR PLOT
# ------------------------------------

pair_df = df[["Sales", "Profit", "Quantity"]]

sns.pairplot(pair_df)

plt.savefig("../reports/pairplot.png")
plt.close()

print("✓ Pair Plot Saved")

# ------------------------------------
# CORRELATION MATRIX
# ------------------------------------

corr = df.corr(numeric_only=True)

print("\nCorrelation Matrix")
print(corr)

# Save correlation matrix
corr.to_csv("../reports/correlation_matrix.csv")

print("✓ Correlation Matrix Saved")

# ------------------------------------
# HEATMAP
# ------------------------------------

plt.figure(figsize=(8, 6))

sns.heatmap(
    corr,
    annot=True
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("../reports/correlation_heatmap.png")
plt.close()

print("✓ Heatmap Saved")

# ------------------------------------
# STRONGEST CORRELATION
# ------------------------------------

print("\nAnalysis Summary")

sales_profit_corr = corr.loc["Sales", "Profit"]

print(f"Sales vs Profit Correlation: {sales_profit_corr:.2f}")

if sales_profit_corr > 0.7:
    print("Strong Positive Correlation")

elif sales_profit_corr > 0.3:
    print("Moderate Positive Correlation")

elif sales_profit_corr > 0:
    print("Weak Positive Correlation")

else:
    print("Negative Correlation")

print("\nMultivariate Analysis Completed!")