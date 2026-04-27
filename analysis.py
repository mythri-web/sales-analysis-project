import pandas as pd

# Load dataset
df = pd.read_csv("SampleSuperstore.csv")

# Show first 5 rows
print(df.head())
# Check missing values
print(df.isnull().sum())

# Drop missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

print("Cleaned data shape:", df.shape)
# Total sales
print("Total Sales:", df['Sales'].sum())

# Average sales
print("Average Sales:", df['Sales'].mean())

# Sales by category
print(df.groupby('Category')['Sales'].sum())
import matplotlib.pyplot as plt

# Sales by Category
df.groupby('Category')['Sales'].sum().plot(kind='bar')

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()
# -------------------------
# -------------------------
# Profit by Category
# -------------------------
profit_category = df.groupby('Category')['Profit'].sum()

print("\nProfit by Category:")
print(profit_category)

profit_category.plot(kind='bar')

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.show()
# -------------------------
# Top 10 Products
# -------------------------
top_products = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Sub-Categories by Sales:")
print(top_products)

top_products.plot(kind='bar')

plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Sub-Category")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()
# -------------------------
# Loss Making Sub-Categories
# -------------------------
loss_products = df.groupby('Sub-Category')['Profit'].sum().sort_values().head(10)

print("\nLoss Making Sub-Categories:")
print(loss_products)

loss_products.plot(kind='barh')

plt.title("Loss Making Sub-Categories")
plt.xlabel("Profit")
plt.show()
# -------------------------
# Sales by Region
# -------------------------
region_sales = df.groupby('Region')['Sales'].sum()

print("\nSales by Region:")
print(region_sales)

region_sales.plot(kind='bar')

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()
print("\n--- KEY INSIGHTS ---")
print("1. Identify which category has highest sales and profit")
print("2. Check sub-categories with losses")
print("3. Compare performance across regions")