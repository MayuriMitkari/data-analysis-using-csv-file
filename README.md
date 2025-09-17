# Data-analysis-on-csv-file
Sales Data Analysis using Pandas
🔹 Objective

The goal of this project is to analyze sales data from a CSV file using Python and Pandas. The analysis helps us extract meaningful business insights such as total revenue, profit trends, and product-wise performance.

🔹 Tools & Technologies

Python 🐍

Pandas (Data analysis)

Matplotlib / Seaborn (Data visualization)

Jupyter Notebook / Google Colab (for interactive execution)

🔹 Steps Performed

Load the dataset

Used pandas.read_csv() to import the sales CSV file.

Explore the dataset

Checked the first few rows using .head().

Verified column names and data types.

Data Cleaning (if needed)

Handled missing values (like blank Sales entries).

Corrected any typos (e.g., “Mopbile” → “Mobile”).

Analysis Performed

✅ Total Revenue → df["Sales"].sum()

✅ Total Profit → df["Profit"].sum()

✅ Group by Month → Find monthly sales trends

✅ Group by Product → Find best-selling products

✅ Group by Category → Understand performance across categories

Visualization

Bar charts for Product-wise sales

Line chart for Month-wise sales

Pie chart for Product contribution

🔹 Outcomes / Insights

Found total sales revenue and profit.

Identified top-performing products (e.g., Laptop, Mobile, Tablet).

Observed sales seasonality across months.

Discovered how discounts impact overall sales.

🔹 Deliverables

Python Script (data_analysis.py)

Jupyter Notebook (data_analysis.ipynb) with code + charts

Charts (saved as PNGs or displayed in notebook)
