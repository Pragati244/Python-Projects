import pandas as pd
import matplotlib.pyplot as plt
import os
data1 = pd.read_csv('C:\\Users\\admin\\Python-Projects\\09_DataCleaning\\dirty_sales_data.csv')
print(data1)
data1["Revenue"] = data1["Quantity"] * data1["Price"]
# Create a folder to save graphs
os.makedirs("images", exist_ok=True)
data1 = pd.DataFrame(data1)

print(f'data1 shape: {data1.shape}\n')

print(f'data1 head:\n {data1.head(5)}\n')

print(f'data1 types: \n {data1.dtypes}\n')

print(f'data1 columns: \n {data1.columns}\n')

print(f'data1 null values:\n{data1.isnull().sum()}')




print(f'----------------data1 info:------------\n {data1.info()}\n')

print(f'----------------data1 statistics:------------\n {data1.describe()}\n')

print(data1.isnull())

print(data1.isnull().mean())
data1["Quantity"] = data1["Quantity"].fillna(data1["Quantity"].median())
data1["Price"] = data1["Price"].fillna(data1["Price"].mean())
data1["Region"] = data1["Region"].fillna("Unknown")
data1["Product"] = data1["Product"].fillna("Unknown")
# # Remove invalid negative or zero quantities
data1 = data1[data1["Quantity"] > 0].copy()
print(data1)
# # Prepare summaries
revenue_by_region = data1.groupby("Region")["Revenue"].sum()
revenue_by_product = data1.groupby("Product")["Revenue"].sum()
quantity_by_category = data1.groupby("Category")["Quantity"].sum()
revenue_by_category = data1.groupby("Category")["Revenue"].sum()


# Graph 1
plt.figure(figsize=(8, 5))
revenue_by_region.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("images/revenue_by_region.png")


# Graph 2
plt.figure(figsize=(8, 5))
revenue_by_product.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/revenue_by_product.png")


# Graph 3
plt.figure(figsize=(8, 5))
quantity_by_category.plot(kind="bar")
plt.title("Units Sold by Category")
plt.xlabel("Category")
plt.ylabel("Quantity")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("images/units_by_category.png")


# Graph 4
plt.figure(figsize=(7, 7))
revenue_by_category.plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Revenue Share by Category")
plt.ylabel("")
plt.tight_layout()
plt.savefig("images/revenue_by_category.png")


plt.figure(figsize=(8, 5))
plt.bar(data1["Product"],data1["Quantity"])
plt.title("Quantity Sold by Product")
plt.xticks(rotation=45)
plt.xlabel("Product")
plt.ylabel("Quantity")  
plt.savefig("images/quantity_by_product.png")

# Display all graph windows
plt.show()