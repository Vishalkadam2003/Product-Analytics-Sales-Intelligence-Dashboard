# Product-Analytics-Sales-Intelligence-Dashboard
# Product Analytics & Sales Intelligence Dashboard (Power BI + Python)

## Project Overview

This project focuses on analyzing and visualizing retail sales data using real-world Superstore data. The goal is to uncover actionable business insights about products, regions, customer segments, and sales trends, and to present them through an interactive Power BI dashboard.

---

##  Dataset

- **Source**: Superstore Dataset (Kaggle)
- **Rows**: ~10,000
- **Fields**: Order Date, Sales, Category, Segment, Region, Customer Info, etc.

---

##  Tools & Technologies

| Tool           | Purpose                          |
|----------------|----------------------------------|
| **Python (pandas, matplotlib, seaborn)** | Data Cleaning, EDA |
| **Power BI**   | Interactive Dashboard & Reporting |
| Excel/CSV      | Data Storage (source format)     |

---

##  Key Analysis Performed

- Sales by Product **Category** and **Sub-Category**
- Regional Sales Performance
- Customer **Segment Analysis**
- Monthly and Yearly Sales Trends
- Top 10 Best-Selling Products
- Segment-wise Contribution to Regional Sales

---

##  Power BI Dashboard Features

-  **Slicers** to filter by:
  - Category
  - Segment
  - Region
  - Date Range

-  **KPI Cards** for:
  - Total Sales
  - Total Orders
  - Unique Products Sold
  - Average Order Value

-  **Visuals Used**:
  - Clustered Column Chart
  - 100% Stacked Bar Chart
  - Line Chart for Monthly Trends
  - Pie Chart for Segment Share
  - Card Visuals for KPIs

---

##  Sample Visuals

> Include screenshots here after uploading them  
> Example:
> ![Sales by Category](images/sales_by_category.png)

---

## Real-World Impact

This dashboard simulates what a real data analyst would deliver to product or sales teams. It helps identify:
- High-performing regions or categories
- Underperforming segments
- Seasonal trends
- Strategic product insights

---

## How to Use

1. Clone/download the repository
2. Open `.pbix` file in Power BI Desktop
3. Explore, filter, and interact with the visuals
4. Optional: Modify or connect to your own dataset

---

## Files Included

| File | Description |
|------|-------------|
| `explore_data.py` | Python script for data cleaning and exploration |
| `superstore_sales.csv` | Source dataset |
| `Superstore_Analytics_Dashboard.pbix` | Final Power BI report file |
| `README.md` | Project documentation |

---

##  Future Enhancements

- Integration with SQL-based data source
- Dynamic drill-through pages
- Streamlit version for web sharing
- Advanced DAX-based KPIs (Profit Margin, ROI)

