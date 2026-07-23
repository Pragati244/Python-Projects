# Sales Data Cleaning and Visualization

This Python project cleans a sales dataset, calculates revenue, creates summary tables, and generates visualizations using Pandas and Matplotlib.

## Features

* Loads sales data from a CSV file
* Checks dataset shape, columns, data types, statistics, and missing values
* Fills missing quantity, price, product, and region values
* Removes records with invalid quantities
* Calculates revenue using:


Revenue = Quantity × Price

* Groups sales data by region, product, and category
* Saves five charts inside the `images` folder

## Charts Generated

* Revenue by Region
* Revenue by Product
* Units Sold by Category
* Revenue Share by Category
* Quantity Sold by Product

## Technologies Used

* Python
* Pandas
* Matplotlib

## How to Run

Install the required libraries:

```bash
pip install pandas matplotlib
```

Update the CSV file path in the Python script:

```python
data1 = pd.read_csv("path/to/dirty_sales_data.csv")
```

Run the script:

```bash
python sales_analysis.py
```

The generated charts will be saved in the `images` folder.

## Key Insights

* The East region generates the highest revenue.
* Laptops generate the highest product revenue.
* Electronics outperform furniture in both sales quantity and revenue.
* Headphones sell the most units but do not generate the highest revenue.

## Recommendations

Focus on growing sales in weaker regions, promote high-revenue products such as laptops, review headphone pricing, and introduce complementary or higher-margin products.
