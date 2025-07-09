import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 

df = pd.read_csv(r"D:\Data Analytics Project\Data\archive (15)\superstore_sales.csv.csv")

print("First 5 rows of data : \n",df.head())
print("information of data : \n",df.info())
print("Missing values of Data per column. : \n",df.isnull().sum())
print("Summaray Statistics of Data is \n: ",df.describe())

#  i converting it  to dates
df['Order Date'] = pd.to_datetime(df['Order Date'],dayfirst = True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'],dayfirst=True)

# now i checked missing values again to ensure
print("Missing values per column after loading :\n ",df.isnull().sum()) 

# now we just removed or Drop the rows where Customer ID is missing (if any)
df = df.dropna(subset=['Customer ID'])

# lets see column list of dataset
print(df.columns.tolist())

#Sales by category 
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=True)
print("\nSales by Category : \n",category_sales) 

#Sales by Region 
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=True)
print("\nSales by Region : \n",region_sales)

#Sales by segment 
segment_sales = df.groupby('Segment')['Sales'].sum().sort_values(ascending=True)
print("\nSales by Segments : \n",segment_sales)

# monthly Sales trends 
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum() 
print("\nSales by Month : \n",monthly_sales)

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

# now we are going to plot so it will be easy for me to understand data 

# Line Plot
plt.figure(figsize=(10,6))
monthly_sales.plot(kind='line',marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

#Bar Plot
plt.figure(figsize=(10,6))
top_products.plot(kind='barh',color='skyblue')
plt.title('Top 10 Products by Sales')
plt.xlabel('Total Sales')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Pie Plot 
region_sales = df.groupby('Region')['Sales'].sum()
plt.figure(figsize=(10,6))
plt.pie(region_sales, labels= region_sales.index, autopct='%1.1f%%',startangle = 140)
plt.title('Sales Share by Region')
plt.axis('equal')
plt.show()

# Box Plot 
plt.figure(figsize=(8,5))
sns.boxplot(data=df,x='Category',y='Sales')
plt.title('Sales Distribution by Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show() 

# Heatmap - Sales Correlation Matrix 
plt.figure(figsize=(6,4))
num_data = df[['Sales']]
sns.heatmap(num_data.corr(),annot=True,cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Histogram - Sales Distribution 
plt.figure(figsize=(8,4))
plt.hist(df['Sales'],bins=50, color='coral',edgecolor='black')
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

